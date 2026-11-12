from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    CreativeWork_Ref = Union[CreativeWork, Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class Claim(CreativeWork):
    """A [[Claim]] in Schema.org represents a specific, factually-oriented claim that could be the [[itemReviewed]] in a [[ClaimReview]]. The content of a claim can be summarized with the [[text]] property. Variations on well known claims can have their common identity indicated via [[sameAs]] links, and summarized with a [[name]]. Ideally, a [[Claim]] description includes enough contextual information to minimize the risk of ambiguity or inclarity. In practice, many claims are better understood in the context in which they appear or the interpretations provided by claim reviews."""
    schema_type: ClassVar[str] = "Claim"
    appearance: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None)
    claim_interpreter: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="claimInterpreter", serialization_alias="claimInterpreter")
    first_appearance: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="firstAppearance", serialization_alias="firstAppearance")
