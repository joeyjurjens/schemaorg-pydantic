from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, DateTime, Integer, Is, Number, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .category_code import CategoryCode
    from .contact_point import ContactPoint
    from .credential import Credential
    from .defined_term import DefinedTerm
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .monetary_amount import MonetaryAmount
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .occupation import Occupation
    from .occupational_experience_requirements import OccupationalExperienceRequirements
    from .organization import Organization
    from .person import Person
    from .place import Place
    from .price_specification import PriceSpecification
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    AdministrativeArea_Ref = Union[AdministrativeArea, Ref]
else:
    AdministrativeArea_Ref = Union[Is["AdministrativeArea"], Ref]

if TYPE_CHECKING:
    CategoryCode_Text_Ref = Union[CategoryCode, Text, Ref]
else:
    CategoryCode_Text_Ref = Union[Is["CategoryCode"], Text, Ref]

if TYPE_CHECKING:
    ContactPoint_Ref = Union[ContactPoint, Ref]
else:
    ContactPoint_Ref = Union[Is["ContactPoint"], Ref]

if TYPE_CHECKING:
    Credential_Text_Ref = Union[Credential, Text, Ref]
else:
    Credential_Text_Ref = Union[Is["Credential"], Text, Ref]

Date_DateTime = Union[Date, DateTime]
Date_Text = Union[Date, Text]
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
    MonetaryAmount_PriceSpecification_Number_Ref = Union[MonetaryAmount, PriceSpecification, Number, Ref]
else:
    MonetaryAmount_PriceSpecification_Number_Ref = Union[Is["MonetaryAmount"], Is["PriceSpecification"], Number, Ref]

if TYPE_CHECKING:
    Occupation_Ref = Union[Occupation, Ref]
else:
    Occupation_Ref = Union[Is["Occupation"], Ref]

if TYPE_CHECKING:
    OccupationalExperienceRequirements_Text_Ref = Union[OccupationalExperienceRequirements, Text, Ref]
else:
    OccupationalExperienceRequirements_Text_Ref = Union[Is["OccupationalExperienceRequirements"], Text, Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class JobPosting(Intangible):
    """A listing that describes a job opening in a certain organization."""
    schema_type: ClassVar[str] = "JobPosting"
    applicant_location_requirements: AdministrativeArea_Ref | list[AdministrativeArea_Ref] | None = Field(default=None, validation_alias="applicantLocationRequirements", serialization_alias="applicantLocationRequirements")
    application_contact: ContactPoint_Ref | list[ContactPoint_Ref] | None = Field(default=None, validation_alias="applicationContact", serialization_alias="applicationContact")
    base_salary: MonetaryAmount_PriceSpecification_Number_Ref | list[MonetaryAmount_PriceSpecification_Number_Ref] | None = Field(default=None, validation_alias="baseSalary", serialization_alias="baseSalary")
    date_posted: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="datePosted", serialization_alias="datePosted")
    direct_apply: Boolean | list[Boolean] | None = Field(default=None, validation_alias="directApply", serialization_alias="directApply")
    education_requirements: EducationalOccupationalCredential_Text_Ref | list[EducationalOccupationalCredential_Text_Ref] | None = Field(default=None, validation_alias="educationRequirements", serialization_alias="educationRequirements")
    eligibility_to_work_requirement: Text | list[Text] | None = Field(default=None, validation_alias="eligibilityToWorkRequirement", serialization_alias="eligibilityToWorkRequirement")
    employer_overview: Text | list[Text] | None = Field(default=None, validation_alias="employerOverview", serialization_alias="employerOverview")
    employment_type: Text | list[Text] | None = Field(default=None, validation_alias="employmentType", serialization_alias="employmentType")
    employment_unit: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="employmentUnit", serialization_alias="employmentUnit")
    estimated_salary: MonetaryAmount_MonetaryAmountDistribution_Number_Ref | list[MonetaryAmount_MonetaryAmountDistribution_Number_Ref] | None = Field(default=None, validation_alias="estimatedSalary", serialization_alias="estimatedSalary")
    experience_in_place_of_education: Boolean | list[Boolean] | None = Field(default=None, validation_alias="experienceInPlaceOfEducation", serialization_alias="experienceInPlaceOfEducation")
    experience_requirements: OccupationalExperienceRequirements_Text_Ref | list[OccupationalExperienceRequirements_Text_Ref] | None = Field(default=None, validation_alias="experienceRequirements", serialization_alias="experienceRequirements")
    hiring_organization: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="hiringOrganization", serialization_alias="hiringOrganization")
    incentive_compensation: Text | list[Text] | None = Field(default=None, validation_alias="incentiveCompensation", serialization_alias="incentiveCompensation")
    industry: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    job_benefits: Text | list[Text] | None = Field(default=None, validation_alias="jobBenefits", serialization_alias="jobBenefits")
    job_duration: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="jobDuration", serialization_alias="jobDuration")
    job_immediate_start: Boolean | list[Boolean] | None = Field(default=None, validation_alias="jobImmediateStart", serialization_alias="jobImmediateStart")
    job_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="jobLocation", serialization_alias="jobLocation")
    job_location_type: Text | list[Text] | None = Field(default=None, validation_alias="jobLocationType", serialization_alias="jobLocationType")
    job_start_date: Date_Text | list[Date_Text] | None = Field(default=None, validation_alias="jobStartDate", serialization_alias="jobStartDate")
    occupational_category: CategoryCode_Text_Ref | list[CategoryCode_Text_Ref] | None = Field(default=None, validation_alias="occupationalCategory", serialization_alias="occupationalCategory")
    physical_requirement: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="physicalRequirement", serialization_alias="physicalRequirement")
    qualifications: Credential_Text_Ref | list[Credential_Text_Ref] | None = Field(default=None)
    relevant_occupation: Occupation_Ref | list[Occupation_Ref] | None = Field(default=None, validation_alias="relevantOccupation", serialization_alias="relevantOccupation")
    responsibilities: Text | list[Text] | None = Field(default=None)
    salary_currency: Text | list[Text] | None = Field(default=None, validation_alias="salaryCurrency", serialization_alias="salaryCurrency")
    security_clearance_requirement: Text | list[Text] | None = Field(default=None, validation_alias="securityClearanceRequirement", serialization_alias="securityClearanceRequirement")
    sensory_requirement: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="sensoryRequirement", serialization_alias="sensoryRequirement")
    skills: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    special_commitments: Text | list[Text] | None = Field(default=None, validation_alias="specialCommitments", serialization_alias="specialCommitments")
    title: Text | list[Text] | None = Field(default=None)
    total_job_openings: Integer | list[Integer] | None = Field(default=None, validation_alias="totalJobOpenings", serialization_alias="totalJobOpenings")
    valid_through: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validThrough", serialization_alias="validThrough")
    work_hours: Text | list[Text] | None = Field(default=None, validation_alias="workHours", serialization_alias="workHours")
