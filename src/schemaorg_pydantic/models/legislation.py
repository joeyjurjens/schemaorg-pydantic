from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, Is, Ref, Text
from .creative_work import CreativeWork
from .legal_force_status import LegalForceStatus

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .category_code import CategoryCode
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    AdministrativeArea_Text_Ref = Union[AdministrativeArea, Text, Ref]
else:
    AdministrativeArea_Text_Ref = Union[Is["AdministrativeArea"], Text, Ref]

if TYPE_CHECKING:
    CategoryCode_Text_Ref = Union[CategoryCode, Text, Ref]
else:
    CategoryCode_Text_Ref = Union[Is["CategoryCode"], Text, Ref]

if TYPE_CHECKING:
    Legislation_Ref = Union["Legislation", Ref]
else:
    Legislation_Ref = Union[Is["Legislation"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class Legislation(CreativeWork):
    """A legal document such as an act, decree, bill, etc. (enforceable or not) or a component of a legal act (like an article)."""
    schema_type: ClassVar[str] = "Legislation"
    jurisdiction: AdministrativeArea_Text_Ref | list[AdministrativeArea_Text_Ref] | None = Field(default=None)
    legislation_amends: Legislation_Ref | list[Legislation_Ref] | None = Field(default=None, validation_alias="legislationAmends", serialization_alias="legislationAmends")
    legislation_applies: Legislation_Ref | list[Legislation_Ref] | None = Field(default=None, validation_alias="legislationApplies", serialization_alias="legislationApplies")
    legislation_changes: Legislation_Ref | list[Legislation_Ref] | None = Field(default=None, validation_alias="legislationChanges", serialization_alias="legislationChanges")
    legislation_commences: Legislation_Ref | list[Legislation_Ref] | None = Field(default=None, validation_alias="legislationCommences", serialization_alias="legislationCommences")
    legislation_consolidates: Legislation_Ref | list[Legislation_Ref] | None = Field(default=None, validation_alias="legislationConsolidates", serialization_alias="legislationConsolidates")
    legislation_corrects: Legislation_Ref | list[Legislation_Ref] | None = Field(default=None, validation_alias="legislationCorrects", serialization_alias="legislationCorrects")
    legislation_countersigned_by: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="legislationCountersignedBy", serialization_alias="legislationCountersignedBy")
    legislation_date: Date | list[Date] | None = Field(default=None, validation_alias="legislationDate", serialization_alias="legislationDate")
    legislation_date_of_applicability: Date | list[Date] | None = Field(default=None, validation_alias="legislationDateOfApplicability", serialization_alias="legislationDateOfApplicability")
    legislation_date_version: Date | list[Date] | None = Field(default=None, validation_alias="legislationDateVersion", serialization_alias="legislationDateVersion")
    legislation_ensures_implementation_of: Legislation_Ref | list[Legislation_Ref] | None = Field(default=None, validation_alias="legislationEnsuresImplementationOf", serialization_alias="legislationEnsuresImplementationOf")
    legislation_identifier: Text | list[Text] | None = Field(default=None, validation_alias="legislationIdentifier", serialization_alias="legislationIdentifier")
    legislation_jurisdiction: AdministrativeArea_Text_Ref | list[AdministrativeArea_Text_Ref] | None = Field(default=None, validation_alias="legislationJurisdiction", serialization_alias="legislationJurisdiction")
    legislation_legal_force: LegalForceStatus | list[LegalForceStatus] | None = Field(default=None, validation_alias="legislationLegalForce", serialization_alias="legislationLegalForce")
    legislation_passed_by: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="legislationPassedBy", serialization_alias="legislationPassedBy")
    legislation_repeals: Legislation_Ref | list[Legislation_Ref] | None = Field(default=None, validation_alias="legislationRepeals", serialization_alias="legislationRepeals")
    legislation_responsible: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="legislationResponsible", serialization_alias="legislationResponsible")
    legislation_transposes: Legislation_Ref | list[Legislation_Ref] | None = Field(default=None, validation_alias="legislationTransposes", serialization_alias="legislationTransposes")
    legislation_type: CategoryCode_Text_Ref | list[CategoryCode_Text_Ref] | None = Field(default=None, validation_alias="legislationType", serialization_alias="legislationType")
