from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .intangible import Intangible

if TYPE_CHECKING:
    from .member_program_tier import MemberProgramTier
    from .organization import Organization

if TYPE_CHECKING:
    MemberProgramTier_Ref = Union[MemberProgramTier, Ref]
else:
    MemberProgramTier_Ref = Union[Is["MemberProgramTier"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]


class MemberProgram(Intangible):
    """A MemberProgram defines a loyalty (or membership) program that provides its members with certain benefits, for example better pricing, free shipping or returns, or the ability to earn loyalty points. Member programs may have multiple tiers, for example silver and gold members, each with different benefits."""
    schema_type: ClassVar[str] = "MemberProgram"
    has_tiers: MemberProgramTier_Ref | list[MemberProgramTier_Ref] | None = Field(default=None, validation_alias="hasTiers", serialization_alias="hasTiers")
    hosting_organization: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="hostingOrganization", serialization_alias="hostingOrganization")
