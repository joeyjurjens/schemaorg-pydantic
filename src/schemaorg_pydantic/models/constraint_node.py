from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Url
from .intangible import Intangible

if TYPE_CHECKING:
    from .property import Property

if TYPE_CHECKING:
    Property_Url_Ref = Union[Property, Url, Ref]
else:
    Property_Url_Ref = Union[Is["Property"], Url, Ref]


class ConstraintNode(Intangible):
    """The ConstraintNode type is provided to support usecases in which a node in a structured data graph is described with properties which appear to describe a single entity, but are being used in a situation where they serve a more abstract purpose. A [[ConstraintNode]] can be described using [[constraintProperty]] and [[numConstraints]]. These constraint properties can serve a\n    variety of purposes, and their values may sometimes be understood to indicate sets of possible values rather than single, exact and specific values."""
    schema_type: ClassVar[str] = "ConstraintNode"
    constraint_property: Property_Url_Ref | list[Property_Url_Ref] | None = Field(default=None, validation_alias="constraintProperty", serialization_alias="constraintProperty")
    num_constraints: Integer | list[Integer] | None = Field(default=None, validation_alias="numConstraints", serialization_alias="numConstraints")
