from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .action import Action

if TYPE_CHECKING:
    from .action_access_specification import ActionAccessSpecification
    from .offer import Offer

if TYPE_CHECKING:
    ActionAccessSpecification_Ref = Union[ActionAccessSpecification, Ref]
else:
    ActionAccessSpecification_Ref = Union[Is["ActionAccessSpecification"], Ref]

if TYPE_CHECKING:
    Offer_Ref = Union[Offer, Ref]
else:
    Offer_Ref = Union[Is["Offer"], Ref]


class ConsumeAction(Action):
    """The act of ingesting information/resources/food."""
    schema_type: ClassVar[str] = "ConsumeAction"
    action_accessibility_requirement: ActionAccessSpecification_Ref | list[ActionAccessSpecification_Ref] | None = Field(default=None, validation_alias="actionAccessibilityRequirement", serialization_alias="actionAccessibilityRequirement")
    expects_acceptance_of: Offer_Ref | list[Offer_Ref] | None = Field(default=None, validation_alias="expectsAcceptanceOf", serialization_alias="expectsAcceptanceOf")
