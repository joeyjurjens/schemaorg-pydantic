import hashlib
import json
import keyword
import re

from pydantic import BaseModel
from pydantic.alias_generators import to_snake

from .vocabulary import BASIC, ids

RENAME_CLASS = {"3DModel": "ThreeDModel"}
NAME = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")
MEMBER = re.compile(r"^[A-Za-z0-9]+$")
SCALARS = ("Text", "Url", "Number", "Integer", "Boolean", "Date", "DateTime", "Time")
RESERVED = set(dir(BaseModel)) | {"id", "ref", "schema_type", "to_jsonld", "to_script"}
TAKEN = {
    "list",
    "str",
    "int",
    "bool",
    "None",
    "Union",
    "ClassVar",
    "TYPE_CHECKING",
    "Field",
    "Node",
    "Ref",
    "Is",
    *SCALARS,
}


class Generator:
    def __init__(self, vocabulary, overrides):
        self.vocab = vocabulary
        self.overrides = overrides
        self.keep = self.choose_classes()
        self.order = self.sort_classes()
        self.enum_classes = {name for name in vocabulary.classes if vocabulary.is_enum(name)}
        self.ranges = self.collect_ranges()
        self.aliases = self.name_aliases()
        self.renamed = {}
        self.model_names = {self.class_name(name) for name in self.keep}
        self.enum_names = {self.class_name(name) for name in self.enum_classes}
        self.check_names()
        self.modules = self.collect_modules()
        self.check_field_names()

    def class_name(self, name):
        short = self.vocab.short(name)
        return RENAME_CLASS.get(short, short)

    def choose_classes(self):
        vocab = self.vocab
        return {
            name
            for name in vocab.classes
            if vocab.kind(name) == "class"
            and not vocab.is_superseded(vocab.classes[name])
            and not vocab.is_enum(name)
        }

    def bases(self, name):
        parents = [p for p in self.vocab.parents[name] if p in self.keep]
        parents = [
            p for p in parents if not any(p in self.vocab.ancestors(q) for q in parents if q != p)
        ]
        return sorted(parents, key=self.class_name)

    def sort_classes(self):
        order, seen = [], set()

        def visit(name):
            if name in seen:
                return
            seen.add(name)
            for base in self.bases(name):
                visit(base)
            order.append(name)

        for name in sorted(self.keep, key=self.class_name):
            visit(name)
        return order

    def own_fields(self, name):
        inherited = self.vocab.inherited_properties(name)
        return sorted(
            (p for p in self.vocab.own_properties.get(name, []) if p not in inherited),
            key=self.vocab.short,
        )

    def range_of(self, prop):
        vocab = self.vocab
        parts, has_class = [], False
        for extra in self.overrides.get(vocab.short(prop), {}).get("add", []):
            parts.append(BASIC[extra])
        for target in ids(vocab.properties[prop].get("schema:rangeIncludes")):
            if target not in vocab.classes:
                continue
            kind = vocab.kind(target)
            if kind == "basic":
                short = vocab.short(target)
                if short in BASIC:
                    parts.append(BASIC[short])
                else:
                    parts.append("Number")
            elif kind == "text":
                parts.append("Text")
            elif vocab.is_enumeration_class(target) and vocab.enum_family(target):
                parts += [self.class_name(member) for member in vocab.enum_family(target)]
            elif target in self.keep:
                parts.append(self.class_name(target))
                has_class = True
        if "Text" in parts and "Url" in parts:
            parts.remove("Url")
        if not parts:
            parts = ["Text", "Number"]
        if has_class or "Thing" in parts:
            parts.append("Ref")
        return tuple(
            sorted(
                set(parts),
                key=lambda part: (part == "Ref", part in SCALARS, part),
            )
        )

    def collect_ranges(self):
        ranges = {}
        for name in self.order:
            for prop in self.own_fields(name):
                ranges.setdefault(prop, None)
        return {prop: self.range_of(prop) for prop in sorted(ranges)}

    def name_aliases(self):
        models = {self.class_name(name) for name in self.keep}
        aliases = {}
        for given in sorted(set(self.ranges.values())):
            if len(given) == 1 and given[0] not in models:
                aliases[given] = given[0]
            elif len(given) <= 4:
                aliases[given] = "_".join(given) + ("_Only" if len(given) == 1 else "")
            else:
                digest = hashlib.sha1("|".join(given).encode()).hexdigest()[:8]
                aliases[given] = f"R{digest}"
        if len(set(aliases.values())) != len(aliases):
            raise ValueError("two ranges give one alias name")
        return aliases

    def field_name(self, prop):
        name = to_snake(self.vocab.short(prop))
        if (
            keyword.iskeyword(name)
            or name in RESERVED
            or name in TAKEN
            or name.startswith("model_")
        ):
            self.renamed[self.vocab.short(prop)] = f"{name}_"
            return f"{name}_"
        return name

    def module_name(self, class_name):
        name = to_snake(class_name)
        return f"{name}_" if keyword.iskeyword(name) else name

    def collect_modules(self):
        names = self.model_names | self.enum_names
        modules = {name: self.module_name(name) for name in names}
        if len(set(modules.values())) != len(modules):
            raise ValueError("two names give one module name")
        return modules

    def check_names(self):
        offenders = [name for name in self.model_names | self.enum_names if not NAME.match(name)]
        offenders += [
            self.vocab.short(prop)
            for prop in self.ranges
            if not NAME.match(self.vocab.short(prop))
            and self.vocab.short(prop) not in self.vocab.pseudo
        ]
        for enum in self.enum_classes:
            for member in self.vocab.members[enum]:
                if not MEMBER.match(self.vocab.short(member["@id"])):
                    offenders.append(self.vocab.short(member["@id"]))
        if offenders:
            raise ValueError(f"names that are not plain letters and digits: {sorted(offenders)}")

    def check_field_names(self):
        for name in self.order:
            kept = (self.vocab.ancestors(name) & self.keep) | {name}
            props = {p for kept_name in kept for p in self.vocab.own_properties.get(kept_name, [])}
            names = [to_snake(self.vocab.short(p)) for p in props]
            if len(set(names)) != len(names):
                raise ValueError(f"two properties of {self.class_name(name)} give one field name")

    def import_line(self, name):
        return f"from .{self.modules[name]} import {name}"

    def member_name(self, short):
        name = to_snake(short).upper()
        return name if name.isidentifier() else f"_{name}"

    def enum_module(self, enum):
        lines = [
            "from ..base import SchemaEnum",
            "",
            "",
            f"class {self.class_name(enum)}(SchemaEnum):",
        ]
        members = sorted(self.vocab.members.get(enum, []), key=lambda m: m["@id"])
        names = [self.member_name(self.vocab.short(m["@id"])) for m in members]
        if len(set(names)) != len(names):
            raise ValueError(f"two members of {self.class_name(enum)} give one name")
        for member, name in zip(members, names):
            short = self.vocab.short(member["@id"])
            lines.append(f"    {name} = {json.dumps('https://schema.org/' + short)}")
        return "\n".join(lines) + "\n"

    def alias_block(self, own_name, ranges):
        lines = []
        for given in sorted(ranges):
            name = self.aliases[given]
            if name == given[0]:
                continue
            models = [part for part in given if part in self.model_names]
            runtime = ", ".join(f'Is["{part}"]' if part in models else part for part in given)
            if not models:
                lines.append(f"{name} = Union[{runtime}]")
                continue
            typing = ", ".join(
                (f'"{part}"' if part == own_name else part) if part in models else part
                for part in given
            )
            lines += [
                "if TYPE_CHECKING:",
                f"    {name} = Union[{typing}]",
                "else:",
                f"    {name} = Union[{runtime}]",
                "",
            ]
        return lines

    def model_module(self, name):
        own = self.class_name(name)
        bases = [self.class_name(b) for b in self.bases(name)]
        fields = self.own_fields(name)
        ranges = {self.ranges[prop] for prop in fields}
        parts = {part for given in ranges for part in given}
        referenced = sorted(parts & self.model_names)
        from_base = sorted(
            (parts & set(SCALARS))
            | ({"Ref"} & parts)
            | ({"Is"} if referenced else set())
            | ({"Node"} if not bases else set())
        )
        typing_names = ["ClassVar"] + (["TYPE_CHECKING"] if referenced else [])
        if any(self.aliases[given] != given[0] for given in ranges):
            typing_names.append("Union")
        lines = [
            "from __future__ import annotations",
            "",
            f"from typing import {', '.join(sorted(typing_names))}",
            "",
            "from pydantic import Field",
            "",
        ]
        if from_base:
            lines.append(f"from ..base import {', '.join(from_base)}")
        for base in bases:
            lines.append(self.import_line(base))
        for enum in sorted(parts & self.enum_names):
            lines.append(self.import_line(enum))
        lines.append("")
        others = [part for part in referenced if part != own and part not in bases]
        if others:
            lines.append("if TYPE_CHECKING:")
            lines += [f"    {self.import_line(part)}" for part in others]
            lines.append("")
        lines += self.alias_block(own, ranges)
        lines += ["", f"class {own}({', '.join(bases) or 'Node'}):"]
        doc = json.dumps(self.vocab.description(name))[1:-1]
        lines.append(f'    """{doc}"""')
        lines.append(f"    schema_type: ClassVar[str] = {json.dumps(self.vocab.short(name))}")
        for prop in fields:
            short = self.vocab.short(prop)
            field = self.field_name(prop)
            quoted = json.dumps(short)
            alias = (
                f", validation_alias={quoted}, serialization_alias={quoted}"
                if field != short
                else ""
            )
            given = self.aliases[self.ranges[prop]]
            lines.append(
                f"    {field}: {given} | list[{given}] | None = Field(default=None{alias})"
            )
        return "\n".join(lines) + "\n"

    def index_module(self, release):
        names = sorted(self.model_names | self.enum_names)
        lines = [
            "from typing import TYPE_CHECKING",
            "",
            "from .base import Node, Ref, SchemaEnum",
            "from .jsonld import Graph, GraphConflict, JsonLd, JsonLdError",
            "from .lazy import LazyExports",
            "",
            f"RELEASE = {json.dumps(release)}",
            "",
            "MODULES = {",
            *[f"    {json.dumps(name)}: {json.dumps(self.modules[name])}," for name in names],
            "}",
            "",
            "lazy = LazyExports(__name__, MODULES)",
            "__getattr__ = lazy.get",
            "__dir__ = lazy.names",
            "",
            "if TYPE_CHECKING:",
            *[f"    from .models.{self.modules[name]} import {name}" for name in names],
        ]
        return "\n".join(lines) + "\n"

    def files(self, release):
        files = {"__init__.py": self.index_module(release), "models/__init__.py": ""}
        for enum in self.enum_classes:
            cname = self.class_name(enum)
            files[f"models/{self.modules[cname]}.py"] = self.enum_module(enum)
        for name in self.order:
            files[f"models/{self.modules[self.class_name(name)]}.py"] = self.model_module(name)
        return dict(sorted(files.items()))

    def stats(self):
        return {
            "models": len(self.order),
            "enums": len(self.enum_classes),
            "properties": len(self.ranges),
            "renamed_fields": self.renamed,
        }
