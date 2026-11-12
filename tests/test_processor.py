import json

from trld.jsonld.expansion import expand
from trld.jsonld.flattening import flatten

from schemaorg_pydantic import Brand, ItemAvailability, Offer, Organization, Product
from schemaorg_pydantic.jsonld import Graph

BASE = "https://example.com/"
VOCAB = {"@vocab": "https://schema.org/"}


def expanded(document):
    local = {**document, "@context": VOCAB}
    return expand(json.loads(json.dumps(local)), BASE)


def graph():
    shop = Organization(id=f"{BASE}#organization", name="Northwind")
    product = Product(
        id=f"{BASE}p/#product",
        name="Blue bag",
        brand=Brand(name="Northwind"),
        manufacturer=shop,
        offers=Offer(price=79, price_currency="EUR", availability=ItemAvailability.IN_STOCK),
    )
    return Graph(shop, product).encode()


def test_every_type_and_property_is_a_schema_org_term():
    nodes = expanded(graph())
    product = next(n for n in nodes if n["@id"] == f"{BASE}p/#product")
    assert product["@type"] == ["https://schema.org/Product"]
    assert "https://schema.org/name" in product
    assert "https://schema.org/offers" in product


def test_an_enumeration_is_the_schema_org_address_written_as_text():
    nodes = expanded(graph())
    product = next(n for n in nodes if n["@id"] == f"{BASE}p/#product")
    offer = product["https://schema.org/offers"][0]
    assert offer["https://schema.org/availability"] == [{"@value": "https://schema.org/InStock"}]


def test_every_reference_points_at_a_node_the_graph_defines():
    nodes = expanded(graph())
    defined = {n["@id"] for n in nodes if "@type" in n}
    for node in nodes:
        for key, values in node.items():
            if key.startswith("@"):
                continue
            for value in values:
                if set(value) == {"@id"} and value["@id"].startswith(BASE):
                    assert value["@id"] in defined


def test_flattening_gives_one_node_for_each_id():
    ids = [n["@id"] for n in flatten(expanded(graph())) if not n["@id"].startswith("_:")]
    assert len(ids) == len(set(ids)) == 2
