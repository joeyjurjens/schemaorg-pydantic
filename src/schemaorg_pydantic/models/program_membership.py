from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .member_program import MemberProgram
    from .organization import Organization
    from .person import Person
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    MemberProgram_Ref = Union[MemberProgram, Ref]
else:
    MemberProgram_Ref = Union[Is["MemberProgram"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]


class ProgramMembership(Intangible):
    """Used to describe membership in a loyalty programs (e.g. \"StarAliance\"), traveler clubs (e.g. \"AAA\"), purchase clubs (\"Safeway Club\"), etc."""
    schema_type: ClassVar[str] = "ProgramMembership"
    hosting_organization: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="hostingOrganization", serialization_alias="hostingOrganization")
    member: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    membership_number: Text | list[Text] | None = Field(default=None, validation_alias="membershipNumber", serialization_alias="membershipNumber")
    membership_points_earned: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="membershipPointsEarned", serialization_alias="membershipPointsEarned")
    program: MemberProgram_Ref | list[MemberProgram_Ref] | None = Field(default=None)
    program_name: Text | list[Text] | None = Field(default=None, validation_alias="programName", serialization_alias="programName")
