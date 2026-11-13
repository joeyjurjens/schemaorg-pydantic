from __future__ import annotations

import datetime as dt
import json
from decimal import Decimal
from typing import Any

from pydantic import ValidationError
from pydantic.fields import FieldInfo

from .base import Node, Ref, SchemaEnum

CONTEXT = "https://schema.org"
FIRST = ["name", "url", "headline", "description", "image", "logo"]


class GraphConflict(ValueError):
    pass


class JsonLdError(ValueError):
    """JSON-LD that is not valid schema.org, with one message for each fault,
    each starting with where in the document it is."""

    def __init__(self, errors: list[str]) -> None:
        super().__init__("; ".join(errors))
        self.errors = errors


class JsonLd:
    @classmethod
    def read(cls, data: Any) -> list[Node]:
        """Reads JSON-LD that is already parsed (a dict or a list, with or
        without @context and @graph) into models. Anything that is not valid
        schema.org raises one JsonLdError that lists every fault."""
        errors: list[str] = []
        nodes: list[Node] = []
        for item in cls.documents(data):
            value = cls.read_value(item, errors, "")
            nodes += value if isinstance(value, list) else [value]
        if errors:
            raise JsonLdError(errors)
        return nodes

    @classmethod
    def documents(cls, data: Any) -> list[Any]:
        items = data if isinstance(data, list) else [data]
        found: list[Any] = []
        for item in items:
            if isinstance(item, dict) and "@graph" in item:
                found += item["@graph"] if isinstance(item["@graph"], list) else [item["@graph"]]
            else:
                found.append(item)
        return found

    @classmethod
    def read_value(cls, value: Any, errors: list[str], path: str) -> Any:
        if isinstance(value, list):
            return [
                cls.read_value(item, errors, f"{path}[{index}]") for index, item in enumerate(value)
            ]
        if isinstance(value, dict):
            if "@type" in value:
                return cls.read_node(value, errors, path)
            if "@value" in value:
                return value["@value"]
            if set(value) == {"@id"}:
                return Ref(id=value["@id"])
            errors.append(f"{path or 'the document'}: an object needs an @type")
            return None
        if isinstance(value, str) and value.startswith("http://schema.org/"):
            return "https://schema.org/" + value[len("http://schema.org/") :]
        return value

    @classmethod
    def enums_of(cls, annotation: Any) -> list[type[SchemaEnum]]:
        found: list[type[SchemaEnum]] = []
        if isinstance(annotation, type) and issubclass(annotation, SchemaEnum):
            found.append(annotation)
        for part in getattr(annotation, "__args__", ()):
            found += cls.enums_of(part)
        return found

    @classmethod
    def to_enum(cls, value: Any, annotation: Any) -> Any:
        if isinstance(value, list):
            return [cls.to_enum(item, annotation) for item in value]
        if isinstance(value, str):
            for enum in cls.enums_of(annotation):
                try:
                    return enum(value)
                except ValueError:
                    continue
        return value

    @classmethod
    def type_class(cls, name: Any) -> type[Node] | None:
        import schemaorg_pydantic as package

        if not isinstance(name, str):
            return None
        short = name.rsplit("/", 1)[-1].rsplit(":", 1)[-1]
        if short not in package.MODULES:
            return None
        found = getattr(package, short)
        return found if isinstance(found, type) and issubclass(found, Node) else None

    @classmethod
    def read_node(cls, data: dict[str, Any], errors: list[str], path: str) -> Node | None:
        names = data["@type"] if isinstance(data["@type"], list) else [data["@type"]]
        known = [found for found in map(cls.type_class, names) if found]
        where = path or "the document"
        if not known:
            errors.append(f"{where}: {names[0]!r} is not a schema.org type")
            return None
        node_class = max(known, key=lambda found: len(found.__mro__))
        label = f"{path}.{node_class.__name__}" if path else node_class.__name__
        properties: dict[str, Any] = {}
        fields = {
            (info.serialization_alias or name): info
            for name, info in node_class.model_fields.items()
        }
        for key, value in data.items():
            if key in ("@context", "@type"):
                continue
            value = cls.read_value(value, errors, f"{label}.{key}")
            properties[key] = cls.to_enum(value, fields[key].annotation) if key in fields else value
        try:
            return node_class(**properties)
        except ValidationError as error:
            faults: dict[str, list[str]] = {}
            for fault in error.errors():
                name = str(fault["loc"][0]) if fault["loc"] else ""
                if fault["type"] == "extra_forbidden":
                    errors.append(f"{label}: {name} is not a property of {node_class.__name__}")
                    continue
                faults.setdefault(name, []).append(fault["msg"].removeprefix("Value error, "))
            for name, messages in faults.items():
                chosen = next((m for m in messages if m.startswith("expected")), messages[0])
                errors.append(f"{label}.{name}: {chosen}")
            return None

    @classmethod
    def encode(cls, node: Node) -> dict[str, Any]:
        return {"@context": CONTEXT, **cls.encode_node(node)}

    @classmethod
    def dumps(cls, node: Node, **options: Any) -> str:
        return json.dumps(cls.encode(node), **options)

    @classmethod
    def script(cls, document: dict[str, Any]) -> str:
        text = json.dumps(document, ensure_ascii=False, indent=2)
        text = text.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
        return f'<script type="application/ld+json">{text}</script>'

    @classmethod
    def encode_node(
        cls, node: Node, graph: Graph | None = None, root: bool = True
    ) -> dict[str, Any]:
        if graph is not None and node.id and not root:
            graph.register(node)
            return {"@id": node.id}
        out: dict[str, Any] = {"@type": node.schema_type}
        if node.id:
            out["@id"] = node.id
        for name, field in cls.ordered_fields(node):
            if name == "id":
                continue
            value = cls.encode_value(getattr(node, name), graph)
            if not cls.is_empty(value):
                out[field.serialization_alias or name] = value
        return out

    @classmethod
    def encode_value(cls, value: Any, graph: Graph | None = None) -> Any:
        if isinstance(value, Node):
            return cls.encode_node(value, graph, root=False)
        if isinstance(value, Ref):
            return {"@id": value.id}
        if isinstance(value, SchemaEnum):
            return value.value
        if isinstance(value, Decimal):
            as_float = float(value)
            return as_float if Decimal(repr(as_float)) == value else str(value)
        if isinstance(value, (dt.datetime, dt.date, dt.time)):
            return value.isoformat()
        if isinstance(value, list):
            items = [cls.encode_value(item, graph) for item in value]
            return [item for item in items if not cls.is_empty(item)]
        return value

    @classmethod
    def ordered_fields(cls, node: Node) -> list[tuple[str, FieldInfo]]:
        def position(item: tuple[str, FieldInfo]) -> int:
            return FIRST.index(item[0]) if item[0] in FIRST else len(FIRST)

        return sorted(type(node).model_fields.items(), key=position)

    @staticmethod
    def is_empty(value: Any) -> bool:
        return value is None or value == "" or value == [] or value == {}


class Graph:
    def __init__(self, *nodes: Node) -> None:
        self.nodes: dict[str, dict[str, Any]] = {}
        self.anonymous: list[dict[str, Any]] = []
        for node in nodes:
            self.add(node)

    def add(self, node: Node) -> None:
        if node.id and node.id not in self.nodes:
            self.nodes[node.id] = {}
        data = JsonLd.encode_node(node, self)
        if not node.id:
            self.anonymous.append(data)
        elif self.nodes[node.id]:
            self.nodes[node.id] = self.merge(self.nodes[node.id], data)
        else:
            self.nodes[node.id] = data

    def register(self, node: Node) -> None:
        if node.id and node.id not in self.nodes:
            self.add(node)

    def merge(self, first: dict[str, Any], second: dict[str, Any]) -> dict[str, Any]:
        merged = dict(first)
        for key, value in second.items():
            if key in merged and merged[key] != value:
                raise GraphConflict(
                    f"{first.get('@id')}: {key} differs: {merged[key]!r} vs {value!r}"
                )
            merged[key] = value
        return merged

    def encode(self) -> dict[str, Any]:
        return {"@context": CONTEXT, "@graph": list(self.nodes.values()) + self.anonymous}

    def dumps(self, **options: Any) -> str:
        return json.dumps(self.encode(), **options)

    def script(self) -> str:
        return JsonLd.script(self.encode())
