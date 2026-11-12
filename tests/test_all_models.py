import datetime as dt

import pytest
from pydantic import ValidationError

import schemaorg_pydantic as package
from schemaorg_pydantic import Node, SchemaEnum
from scripts.vocabulary import ids

pytestmark = pytest.mark.vocabulary

RENAMED = {"3DModel": "ThreeDModel"}
SAMPLES = {
    "Text": "x",
    "URL": "https://example.com/",
    "Number": 1.5,
    "Float": 1.5,
    "Integer": 1,
    "Boolean": True,
    "Date": dt.date(2026, 1, 2),
    "DateTime": dt.datetime(2026, 1, 2, 3, 4, 5, tzinfo=dt.timezone.utc),
    "Time": dt.time(3, 4, 5),
}


class Expected:
    def __init__(self, vocabulary):
        self.vocab = vocabulary
        self.types = {
            name
            for name in vocabulary.classes
            if vocabulary.kind(name) == "class"
            and not vocabulary.is_superseded(vocabulary.classes[name])
            and not vocabulary.is_enum(name)
        }
        self.enums = {name for name in vocabulary.classes if vocabulary.is_enum(name)}

    def name(self, schema_name):
        short = self.vocab.short(schema_name)
        return RENAMED.get(short, short)

    def model(self, schema_name):
        return getattr(package, self.name(schema_name))

    def sample(self, target):
        if target not in self.vocab.classes:
            return None
        kind = self.vocab.kind(target)
        if kind == "basic":
            short = self.vocab.short(target)
            return SAMPLES.get(short, SAMPLES["Number"])
        if kind == "text":
            return SAMPLES["Text"]
        family = self.vocab.enum_family(target)
        if self.vocab.is_enumeration_class(target) and family:
            return list(self.model(sorted(family)[0]))[0]
        if target in self.types:
            return self.model(target)()
        return None

    def field(self, model, short):
        for name, info in model.model_fields.items():
            if (info.serialization_alias or name) == short:
                return name
        return None


@pytest.fixture(scope="module")
def expected(vocabulary):
    return Expected(vocabulary)


def report(failures):
    assert not failures, f"{len(failures)} failures, first ones:\n" + "\n".join(failures[:15])


def test_every_type_and_enumeration_of_the_release_is_there(expected):
    names = {expected.name(n) for n in expected.types | expected.enums}
    assert names == set(package.MODULES)


def test_every_type_names_itself_and_builds_with_no_values(expected):
    failures = []
    for name in sorted(expected.types):
        model = expected.model(name)
        short = expected.vocab.short(name)
        if model.schema_type != short:
            failures.append(f"{short}: schema_type is {model.schema_type}")
        elif model().to_jsonld() != {"@context": "https://schema.org", "@type": short}:
            failures.append(f"{short}: an empty node writes {model().to_jsonld()}")
    report(failures)


def test_every_type_inherits_from_exactly_the_types_of_its_ancestors(expected):
    failures = []
    for name in sorted(expected.types):
        model = expected.model(name)
        have = {k.__name__ for k in model.__mro__ if issubclass(k, Node) and k is not Node}
        want = {expected.name(name)} | {
            expected.name(a) for a in expected.vocab.ancestors(name) if a in expected.types
        }
        if have != want:
            failures.append(f"{name}: missing {sorted(want - have)}, extra {sorted(have - want)}")
    report(failures)


def test_every_property_is_a_field_of_the_types_it_belongs_to(expected):
    failures = []
    for name in sorted(expected.types):
        model = expected.model(name)
        for prop in expected.vocab.own_properties.get(name, []):
            short = expected.vocab.short(prop)
            if expected.field(model, short) is None:
                failures.append(f"{name} has no field for {short}")
    report(failures)


def test_every_property_takes_every_type_of_value_that_schema_org_lists(expected):
    failures, tried = [], 0
    for name in sorted(expected.types):
        model = expected.model(name)
        for prop in expected.vocab.own_properties.get(name, []):
            short = expected.vocab.short(prop)
            field = expected.field(model, short)
            if field is None:
                continue
            for target in ids(expected.vocab.properties[prop].get("schema:rangeIncludes")):
                value = expected.sample(target)
                if value is None:
                    continue
                tried += 1
                try:
                    written = model(**{field: value}).to_jsonld()
                    listed = model(**{field: [value]}).to_jsonld()
                    if short not in written or short not in listed:
                        failures.append(f"{name}.{short} writes nothing for {target}")
                except ValidationError as error:
                    failures.append(f"{name}.{short} refuses {target}: {str(error)[:80]}")
    assert tried > 2000
    report(failures)


def test_every_property_refuses_a_value_that_is_nothing_schema_org_lists(expected):
    failures = []
    for name in sorted(expected.types):
        model = expected.model(name)
        for prop in expected.vocab.own_properties.get(name, []):
            field = expected.field(model, expected.vocab.short(prop))
            if field is None:
                continue
            try:
                model(**{field: object()})
                failures.append(f"{name}.{field} accepts any object")
            except ValidationError:
                pass
    report(failures)


def test_every_enumeration_has_the_members_of_the_release(expected):
    failures = []
    for name in sorted(expected.enums):
        enum = expected.model(name)
        want = {
            "https://schema.org/" + expected.vocab.short(m["@id"])
            for m in expected.vocab.members[name]
        }
        if not issubclass(enum, SchemaEnum) or {m.value for m in enum} != want:
            failures.append(f"{name}: {len(want)} members expected")
    report(failures)
