import json

import pytest

from schemaorg_pydantic import Brand, BreadcrumbList, ListItem, Organization, Product
from schemaorg_pydantic.jsonld import Graph, GraphConflict, JsonLd


def test_dumps_writes_json():
    data = json.loads(JsonLd.dumps(Product(name="Blue bag")))
    assert data == {"@context": "https://schema.org", "@type": "Product", "name": "Blue bag"}


def test_a_node_used_twice_is_written_once_and_then_referenced():
    shop = Organization(id="https://example.com/#organization", name="Northwind")
    one = Product(id="https://example.com/a/#product", name="A", manufacturer=shop)
    two = Product(id="https://example.com/b/#product", name="B", manufacturer=shop)
    graph = Graph(one, two).encode()["@graph"]
    by_id = {node["@id"]: node for node in graph}
    assert len(graph) == 3
    assert by_id[one.id]["manufacturer"] == {"@id": shop.id}
    assert by_id[shop.id]["name"] == "Northwind"


def test_two_nodes_with_one_id_that_disagree_are_refused():
    first = Organization(id="https://example.com/#o", name="Northwind")
    second = Organization(id="https://example.com/#o", name="Southwind")
    with pytest.raises(GraphConflict):
        Graph(first, second)


def test_two_nodes_with_one_id_are_merged():
    first = Organization(id="https://example.com/#o", name="Northwind")
    second = Organization(id="https://example.com/#o", url="https://example.com/")
    node = Graph(first, second).encode()["@graph"][0]
    assert node["name"] == "Northwind"
    assert node["url"] == "https://example.com/"


def test_a_node_without_an_id_stays_where_it_is():
    crumbs = BreadcrumbList(itemListElement=[ListItem(position=1, name="Home")])
    graph = Graph(crumbs).encode()["@graph"]
    assert graph[0]["itemListElement"][0]["name"] == "Home"


def test_the_graph_dumps_json():
    text = Graph(Product(name="Blue bag", brand=Brand(name="N"))).dumps(indent=2)
    assert json.loads(text)["@graph"][0]["brand"] == {"@type": "Brand", "name": "N"}


def test_a_node_writes_itself():
    product = Product(name="Blue bag")
    assert product.to_jsonld() == JsonLd.encode(product)
    assert product.to_jsonld()["@type"] == "Product"


def test_a_script_tag_cannot_be_ended_by_a_value():
    script = Product(name="</script><b>&").to_script()
    assert script.startswith('<script type="application/ld+json">')
    assert script.endswith("</script>")
    assert script.count("</script>") == 1
    assert "<b>" not in script
    body = script[len('<script type="application/ld+json">') : -len("</script>")]
    assert json.loads(body)["name"] == "</script><b>&"


def test_a_graph_has_a_script_too():
    assert Graph(Product(name="Blue bag")).script().count("<script") == 1


def test_a_node_that_refers_to_itself_does_not_loop():
    shop = Organization(id="https://example.com/#o", name="Northwind")
    shop.parent_organization = shop
    graph = Graph(shop).encode()["@graph"]
    assert graph[0]["parentOrganization"] == {"@id": "https://example.com/#o"}
