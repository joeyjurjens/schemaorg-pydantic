import datetime as dt
from decimal import Decimal

import pytest
from pydantic import ValidationError

from schemaorg_pydantic import Article, Brand, ItemAvailability, Offer, Product, Recipe
from schemaorg_pydantic.jsonld import JsonLd


def test_a_product_writes_its_type_and_nested_types():
    product = Product(
        name="Blue bag",
        brand=Brand(name="Northwind"),
        offers=Offer(price=79, price_currency="EUR", availability=ItemAvailability.IN_STOCK),
    )
    data = JsonLd.encode(product)
    assert data["@context"] == "https://schema.org"
    assert data["@type"] == "Product"
    assert data["brand"] == {"@type": "Brand", "name": "Northwind"}
    assert data["offers"]["availability"] == "https://schema.org/InStock"


def test_the_name_comes_before_the_other_properties():
    assert list(JsonLd.encode(Product(sku="BAG-1", name="Blue bag")))[:4] == [
        "@context",
        "@type",
        "name",
        "sku",
    ]


def test_empty_values_are_left_out():
    product = Product(name="Blue bag", description="", sku=None, image=[])
    assert JsonLd.encode_node(product) == {"@type": "Product", "name": "Blue bag"}


def test_dates_and_decimals_are_written_as_json_wants_them():
    data = JsonLd.encode_node(Offer(price=Decimal("79.00"), priceValidUntil=dt.date(2026, 12, 31)))
    assert data["price"] == 79.0
    assert data["priceValidUntil"] == "2026-12-31"


def test_a_property_that_is_a_python_keyword_is_renamed_and_keeps_its_name_in_json():
    assert Recipe.model_fields["yield_"].serialization_alias == "yield"
    assert "yield" in JsonLd.encode_node(Recipe(name="Soup", yield_="4 bowls"))


def test_a_field_can_be_given_by_its_python_name_or_its_schema_org_name():
    assert Offer(price_currency="EUR") == Offer(priceCurrency="EUR")
    assert Offer(price_currency="EUR").price_currency == "EUR"


def test_json_keeps_the_schema_org_name():
    assert JsonLd.encode_node(Offer(price_currency="EUR")) == {
        "@type": "Offer",
        "priceCurrency": "EUR",
    }


def test_an_enum_member_is_upper_case_and_writes_the_schema_org_address():
    assert ItemAvailability.OUT_OF_STOCK.value == "https://schema.org/OutOfStock"


def test_a_wrong_type_is_refused():
    with pytest.raises(ValidationError):
        Product(name=5)


def test_an_unknown_property_is_refused():
    with pytest.raises(ValidationError):
        Product(name="Blue bag", colour="blue")


def test_a_relative_address_is_refused():
    with pytest.raises(ValidationError):
        Product(name="Blue bag", url="/blue-bag/")


def test_an_availability_must_be_a_schema_org_value():
    with pytest.raises(ValidationError):
        Offer(availability="InStock")


def test_a_value_of_the_wrong_class_is_refused():
    with pytest.raises(ValidationError):
        Product(name="Blue bag", offers=Brand(name="Northwind"))


def test_a_value_can_be_assigned_later_but_is_still_checked():
    product = Product(name="Blue bag")
    product.sku = "BAG-1"
    with pytest.raises(ValidationError):
        product.sku = 5


def test_a_node_needs_an_id_to_be_referenced():
    with pytest.raises(ValueError):
        Product(name="Blue bag").ref()


def test_a_date_is_a_date_or_an_iso_8601_string():
    assert (
        Offer(price_valid_until=dt.date(2026, 12, 31)).to_jsonld()["priceValidUntil"]
        == "2026-12-31"
    )
    assert Offer(price_valid_until="2026-12-31").to_jsonld()["priceValidUntil"] == "2026-12-31"


def test_a_date_and_time_is_a_datetime_or_an_iso_8601_string():
    for value in (
        dt.datetime(2026, 11, 12, 10, 0),
        "2026-11-12T10:00:00+01:00",
        "2026-11-12T10:00:00Z",
    ):
        assert Article(date_published=value).to_jsonld()["datePublished"]


def test_a_string_that_is_not_a_date_is_refused():
    for value in ("tomorrow", "12-31-2026", "2026-13-01"):
        with pytest.raises(ValidationError):
            Offer(price_valid_until=value)


def test_a_search_action_carries_the_query_input_google_asks_for():
    from schemaorg_pydantic import EntryPoint, Graph, SearchAction, WebSite

    action = SearchAction(
        target=EntryPoint(url_template="https://shop.example/search?q={search_term_string}"),
        query_input="required name=search_term_string",
    )
    site = WebSite(
        id="https://shop.example/#website", url="https://shop.example/", potential_action=action
    )
    encoded = Graph(site).encode()["@graph"][0]["potentialAction"]
    assert encoded["query-input"] == "required name=search_term_string"
    assert encoded["target"]["urlTemplate"] == "https://shop.example/search?q={search_term_string}"
