import importlib
import subprocess
import sys

import pytest

import schemaorg_pydantic
from schemaorg_pydantic.lazy import LazyExports


def test_importing_the_package_loads_no_models():
    code = (
        "import sys, schemaorg_pydantic;"
        "print(len([m for m in sys.modules if m.startswith('schemaorg_pydantic.models.')]))"
    )
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
    assert out.stdout.strip() == "0"


def test_a_type_is_loaded_when_it_is_asked_for_and_then_stays():
    product = schemaorg_pydantic.Product
    assert product is importlib.import_module("schemaorg_pydantic.models.product").Product
    assert "Product" in vars(schemaorg_pydantic)


def test_a_name_that_is_not_a_type_is_an_attribute_error():
    with pytest.raises(AttributeError):
        schemaorg_pydantic.NoSuchThing


def test_dir_lists_the_types_without_loading_them():
    assert {"Product", "Offer", "ItemAvailability"} <= set(dir(schemaorg_pydantic))


def test_a_type_of_the_wrong_class_is_refused_even_when_that_class_was_never_loaded():
    from schemaorg_pydantic import Brand, Product

    with pytest.raises(ValueError):
        Product(name="x", offers=Brand(name="y"))


def test_every_name_of_the_index_has_a_module():
    for name, module_name in schemaorg_pydantic.MODULES.items():
        module = importlib.import_module(f"schemaorg_pydantic.models.{module_name}")
        assert hasattr(module, name)


def test_lazy_exports_know_only_their_names():
    lazy = LazyExports("schemaorg_pydantic", {"Product": "product"})
    with pytest.raises(AttributeError):
        lazy.get("Offer")


def test_the_graph_and_the_writer_come_from_the_package_too():
    from schemaorg_pydantic import Graph, GraphConflict, JsonLd, jsonld

    assert (Graph, GraphConflict, JsonLd) == (jsonld.Graph, jsonld.GraphConflict, jsonld.JsonLd)
