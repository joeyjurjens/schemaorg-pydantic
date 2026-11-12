from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .category_code import CategoryCode
    from .credential import Credential
    from .defined_term import DefinedTerm
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .monetary_amount import MonetaryAmount
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .occupational_experience_requirements import OccupationalExperienceRequirements

if TYPE_CHECKING:
    AdministrativeArea_Ref = Union[AdministrativeArea, Ref]
else:
    AdministrativeArea_Ref = Union[Is["AdministrativeArea"], Ref]

if TYPE_CHECKING:
    CategoryCode_Text_Ref = Union[CategoryCode, Text, Ref]
else:
    CategoryCode_Text_Ref = Union[Is["CategoryCode"], Text, Ref]

if TYPE_CHECKING:
    Credential_Text_Ref = Union[Credential, Text, Ref]
else:
    Credential_Text_Ref = Union[Is["Credential"], Text, Ref]

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    EducationalOccupationalCredential_Text_Ref = Union[EducationalOccupationalCredential, Text, Ref]
else:
    EducationalOccupationalCredential_Text_Ref = Union[Is["EducationalOccupationalCredential"], Text, Ref]

if TYPE_CHECKING:
    MonetaryAmount_MonetaryAmountDistribution_Number_Ref = Union[MonetaryAmount, MonetaryAmountDistribution, Number, Ref]
else:
    MonetaryAmount_MonetaryAmountDistribution_Number_Ref = Union[Is["MonetaryAmount"], Is["MonetaryAmountDistribution"], Number, Ref]

if TYPE_CHECKING:
    OccupationalExperienceRequirements_Text_Ref = Union[OccupationalExperienceRequirements, Text, Ref]
else:
    OccupationalExperienceRequirements_Text_Ref = Union[Is["OccupationalExperienceRequirements"], Text, Ref]


class Occupation(Intangible):
    """A profession, may involve prolonged training and/or a formal qualification."""
    schema_type: ClassVar[str] = "Occupation"
    education_requirements: EducationalOccupationalCredential_Text_Ref | list[EducationalOccupationalCredential_Text_Ref] | None = Field(default=None, validation_alias="educationRequirements", serialization_alias="educationRequirements")
    estimated_salary: MonetaryAmount_MonetaryAmountDistribution_Number_Ref | list[MonetaryAmount_MonetaryAmountDistribution_Number_Ref] | None = Field(default=None, validation_alias="estimatedSalary", serialization_alias="estimatedSalary")
    experience_requirements: OccupationalExperienceRequirements_Text_Ref | list[OccupationalExperienceRequirements_Text_Ref] | None = Field(default=None, validation_alias="experienceRequirements", serialization_alias="experienceRequirements")
    occupation_location: AdministrativeArea_Ref | list[AdministrativeArea_Ref] | None = Field(default=None, validation_alias="occupationLocation", serialization_alias="occupationLocation")
    occupational_category: CategoryCode_Text_Ref | list[CategoryCode_Text_Ref] | None = Field(default=None, validation_alias="occupationalCategory", serialization_alias="occupationalCategory")
    qualifications: Credential_Text_Ref | list[Credential_Text_Ref] | None = Field(default=None)
    responsibilities: Text | list[Text] | None = Field(default=None)
    skills: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
