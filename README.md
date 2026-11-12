# schemaorg-pydantic

[schema.org](https://schema.org) types as strict [pydantic](https://docs.pydantic.dev) models, generated from the schema.org vocabulary, with a JSON-LD writer. Python 3.10 and newer, and pydantic 2.7 or newer.

## Install

```bash
pip install schemaorg-pydantic
```

## Use

```python
from schemaorg_pydantic import Brand, Graph, ItemAvailability, Offer, Organization, Product

shop = Organization(id="https://example.com/#organization", name="Northwind")
product = Product(
    id="https://example.com/p/blue-bag/#product",
    name="Blue bag",
    brand=Brand(name="Northwind"),
    manufacturer=shop,
    offers=Offer(price=79, price_currency="EUR", availability=ItemAvailability.IN_STOCK),
)

product.to_jsonld()  # a dict, with @context
product.to_script()  # <script type="application/ld+json">...</script>, safe to put in HTML
Graph(shop, product).script()  # several nodes as one @graph
```

`to_jsonld()` and `to_script()` are short for `JsonLd` in `schemaorg_pydantic.jsonld` (also importable from `schemaorg_pydantic`), the one place that writes a node as JSON-LD. The models themselves are plain pydantic models, so `model_dump()` works as for any other, and another format would be another module. `Graph` writes nodes that are used more than once as a reference.

## What is checked

Fields are snake_case (`price_currency`) and written to JSON-LD under the schema.org name (`priceCurrency`). Both spellings are accepted when you build a model, so a property can be copied from schema.org as it is, but a type checker only knows the Python names. Enumeration members are upper case (`ItemAvailability.IN_STOCK`), and a module is named like its type in snake_case (`product_group.py`).

A date is a `date` or `datetime`, or an ISO 8601 string (`"2026-12-31"`, `"2026-11-12T10:00:00+01:00"`). A wrong type, an unknown property, a relative URL, a date that is not ISO 8601, a value of the wrong class and an availability that is not a schema.org value all raise a `ValidationError` when the model is built, and again when a value is assigned later. Enumerations are enums whose value is the schema.org address, so `ItemAvailability.IN_STOCK` is written as the text `https://schema.org/InStock`, the way Google's documentation writes it. A strict JSON-LD processor reads that as a text value and not as an IRI, because the schema.org context does not say otherwise.

This package writes JSON-LD and does not read it: a nested value must be a model, not a dict, so `Product.model_validate({...})` only works for flat data. To read JSON-LD use [TRLD](https://pypi.org/project/trld/), [PyLD](https://pypi.org/project/PyLD/) or RDFLib.

In a `Graph`, a node with an `@id` that is used more than once is written once and referenced everywhere else. Two nodes with one `@id` that disagree raise `GraphConflict`; two that complement each other are merged. A property whose name is a Python keyword gets a trailing underscore (`yield_`) and is written under its own name.

For other formats, hand the JSON-LD to an RDF library: [RDFLib](https://rdflib.readthedocs.io) (`Graph().parse(data=..., format="json-ld")`, then `serialize(format="turtle")`) or [TRLD](https://pypi.org/project/trld/). The tests read the output with TRLD to check that it is valid JSON-LD 1.1 and that every reference points at a node that exists.

Every type and every property is tested against the pinned schema.org release: each type exists and inherits from exactly its ancestors, each property is a field of the types it belongs to and takes every kind of value schema.org lists for it, each enumeration has its members. The release is downloaded once into `.cache`.

This package does not know what Google requires for a rich result. schema.org does not carry that, so it is data for whoever consumes the models.

## The models are generated

`src/schemaorg_pydantic/models/` and `__init__.py` are generated from a pinned schema.org release (`scripts/pin.json`) and holds the whole vocabulary: 825 types and 80 enumerations as of 30.1, including the pending and the health and life sciences parts, one module for each, in one folder. Types that schema.org has superseded are left out.

A type is imported when it is first used, so `import schemaorg_pydantic` loads none of them (about 31 MB with pydantic, against 19 MB for pydantic alone) and a product with an offer and a brand loads ten small modules. A reference from one type to another is checked by name, so it does not pull the other type in. To regenerate:

```bash
uv run python -m scripts.update
```

`scripts/range_overrides.json` holds the few places where Google accepts more than schema.org lists, each with the page that says so.

A weekly workflow takes the newest schema.org release, regenerates the models, runs the tests, bumps the patch version and tags it. CI checks that the committed models are what the pinned release generates.

## Licence

The code is MIT. The descriptions in the docstrings of the models are taken from schema.org and are available under the [Creative Commons Attribution-ShareAlike License (CC BY-SA 3.0)](https://schema.org/docs/terms.html).
