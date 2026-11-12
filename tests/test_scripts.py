import importlib
import json
import shutil
import sys
from pathlib import Path

import pytest

from scripts.generator import Generator
from scripts.vocabulary import Vocabulary

ROOT = Path(__file__).resolve().parent.parent
MINI = json.loads((ROOT / "tests" / "fixtures" / "mini.jsonld").read_text())["@graph"]


@pytest.fixture
def vocabulary():
    return Vocabulary(MINI)


@pytest.fixture
def files():
    return Generator(Vocabulary(MINI), {}).files("30.1")


def test_the_vocabulary_knows_the_hierarchy(vocabulary):
    assert vocabulary.ancestors("schema:ItemAvailability") == {"schema:Enumeration", "schema:Thing"}


def test_it_tells_datatypes_from_classes(vocabulary):
    assert vocabulary.kind("schema:Text") == "basic"
    assert vocabulary.kind("schema:Offer") == "class"


def test_an_enumeration_has_its_members(vocabulary):
    assert vocabulary.is_enum("schema:ItemAvailability")
    assert not vocabulary.is_enum("schema:Offer")


def test_a_superseded_property_is_not_offered(vocabulary):
    assert "schema:oldName" not in vocabulary.own_properties["schema:Product"]


def test_it_writes_a_module_for_every_wanted_type_and_the_enum_it_needs(files):
    assert "class Product(Thing):" in files["models/product.py"]
    assert "class Offer(Thing):" in files["models/offer.py"]
    assert "class ItemAvailability(SchemaEnum):" in files["models/item_availability.py"]
    assert 'IN_STOCK = "https://schema.org/InStock"' in files["models/item_availability.py"]


def test_a_type_only_imports_what_it_inherits_and_the_enums_it_uses(files):
    assert "from .thing import Thing" in files["models/product.py"]
    assert "from .item_availability import ItemAvailability" in files["models/offer.py"]
    assert "from .offer import Offer" in files["models/product.py"].split("else:")[0]


def test_a_reference_to_another_type_is_checked_by_name_not_imported(files):
    product = files["models/product.py"]
    assert 'Is["Offer"]' in product
    assert "import Offer" in product.split("if TYPE_CHECKING:")[1].split("\n\n")[0]


def test_a_python_keyword_is_renamed_and_keeps_its_alias(files):
    assert "yield_:" in files["models/product.py"]
    assert 'serialization_alias="yield"' in files["models/product.py"]


def test_a_superseded_property_is_left_out(files):
    assert "oldName" not in files["models/product.py"]


def test_the_index_maps_every_name_to_its_module_and_names_the_release(files):
    assert '"Offer": "offer",' in files["__init__.py"]
    assert 'RELEASE = "30.1"' in files["__init__.py"]
    assert "from .models.product import Product" in files["__init__.py"]


def test_the_output_is_deterministic(files):
    assert Generator(Vocabulary(MINI), {}).files("30.1") == files


def test_the_output_imports_and_works(files, tmp_path):
    package = tmp_path / "mini_pkg"
    for path, source in files.items():
        (package / path).parent.mkdir(parents=True, exist_ok=True)
        (package / path).write_text(source)
    for name in ("base.py", "lazy.py", "jsonld.py"):
        shutil.copy(ROOT / "src" / "schemaorg_pydantic" / name, package / name)
    sys.path.insert(0, str(tmp_path))
    try:
        mini = importlib.import_module("mini_pkg")
        offer = mini.Offer(price=5, availability=mini.ItemAvailability.OUT_OF_STOCK)
        product = mini.Product(name="A", offers=offer)
        assert product.offers.availability.value == "https://schema.org/OutOfStock"
        with pytest.raises(Exception, match="expected an instance of Offer"):
            mini.Product(name="A", offers=mini.Thing(name="B"))
    finally:
        sys.path.remove(str(tmp_path))
        for name in [m for m in sys.modules if m == "mini_pkg" or m.startswith("mini_pkg.")]:
            del sys.modules[name]


def test_without_a_list_of_types_it_writes_every_type_and_enumeration():
    generator = Generator(Vocabulary(MINI), {})
    files = generator.files("30.1")
    assert "class Thing(Node):" in files["models/thing.py"]
    assert "class Enumeration(Thing):" in files["models/enumeration.py"]
    assert "class ItemAvailability(SchemaEnum):" in files["models/item_availability.py"]
    assert generator.stats()["models"] == 4


def test_a_module_is_named_in_snake_case_and_never_like_a_python_keyword():
    generator = Generator(Vocabulary(MINI), {})
    assert generator.module_name("Class") == "class_"
    assert generator.module_name("ProductGroup") == "product_group"
    assert generator.module_name("QAPage") == "qa_page"


def test_a_field_is_snake_case_and_keeps_the_schema_org_name_as_alias(files):
    offer = files["models/offer.py"]
    assert "price_currency: Text | list[Text] | None = Field(" in offer
    assert 'validation_alias="priceCurrency"' in offer
    assert 'serialization_alias="priceCurrency"' in offer
    assert "yield_:" in files["models/product.py"]


def test_an_enum_member_is_upper_case_and_its_value_is_the_schema_org_address(files):
    assert 'OUT_OF_STOCK = "https://schema.org/OutOfStock"' in files["models/item_availability.py"]


def with_node(node):
    return Vocabulary([*MINI, node])


def test_a_class_name_that_is_not_plain_letters_and_digits_is_refused():
    evil = {"@id": "schema:Evil(object): import os #", "@type": "rdfs:Class"}
    with pytest.raises(ValueError, match="not plain letters and digits"):
        Generator(with_node(evil), {})


def test_a_property_name_that_is_not_plain_letters_and_digits_is_refused():
    evil = {
        "@id": "schema:x = __import__('os')",
        "@type": "rdf:Property",
        "schema:domainIncludes": {"@id": "schema:Thing"},
        "schema:rangeIncludes": {"@id": "schema:Text"},
    }
    with pytest.raises(ValueError, match="not plain letters and digits"):
        Generator(with_node(evil), {})


def test_an_enum_member_that_is_not_plain_letters_and_digits_is_refused():
    evil = {"@id": "schema:Bad-Member", "@type": "schema:ItemAvailability"}
    with pytest.raises(ValueError, match="not plain letters and digits"):
        Generator(with_node(evil), {})
