from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Integer, Is, Number, Ref, Text
from .intangible import Intangible
from .day_of_week import DayOfWeek

if TYPE_CHECKING:
    from .alignment_object import AlignmentObject
    from .category_code import CategoryCode
    from .course import Course
    from .defined_term import DefinedTerm
    from .demand import Demand
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .offer import Offer
    from .organization import Organization
    from .person import Person
    from .structured_value import StructuredValue

if TYPE_CHECKING:
    R35a3a573 = Union[AlignmentObject, Course, EducationalOccupationalCredential, Text, Ref]
else:
    R35a3a573 = Union[Is["AlignmentObject"], Is["Course"], Is["EducationalOccupationalCredential"], Text, Ref]

if TYPE_CHECKING:
    CategoryCode_Text_Ref = Union[CategoryCode, Text, Ref]
else:
    CategoryCode_Text_Ref = Union[Is["CategoryCode"], Text, Ref]

if TYPE_CHECKING:
    Course_Ref = Union[Course, Ref]
else:
    Course_Ref = Union[Is["Course"], Ref]

Date_DateTime = Union[Date, DateTime]
Date_Text = Union[Date, Text]
if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    Demand_Offer_Ref = Union[Demand, Offer, Ref]
else:
    Demand_Offer_Ref = Union[Is["Demand"], Is["Offer"], Ref]

if TYPE_CHECKING:
    EducationalOccupationalCredential_Text_Ref = Union[EducationalOccupationalCredential, Text, Ref]
else:
    EducationalOccupationalCredential_Text_Ref = Union[Is["EducationalOccupationalCredential"], Text, Ref]

if TYPE_CHECKING:
    MonetaryAmountDistribution_Ref = Union[MonetaryAmountDistribution, Ref]
else:
    MonetaryAmountDistribution_Ref = Union[Is["MonetaryAmountDistribution"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    StructuredValue_Integer_Ref = Union[StructuredValue, Integer, Ref]
else:
    StructuredValue_Integer_Ref = Union[Is["StructuredValue"], Integer, Ref]


class EducationalOccupationalProgram(Intangible):
    """A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree)."""
    schema_type: ClassVar[str] = "EducationalOccupationalProgram"
    application_deadline: Date_Text | list[Date_Text] | None = Field(default=None, validation_alias="applicationDeadline", serialization_alias="applicationDeadline")
    application_start_date: Date | list[Date] | None = Field(default=None, validation_alias="applicationStartDate", serialization_alias="applicationStartDate")
    day_of_week: DayOfWeek | list[DayOfWeek] | None = Field(default=None, validation_alias="dayOfWeek", serialization_alias="dayOfWeek")
    educational_credential_awarded: EducationalOccupationalCredential_Text_Ref | list[EducationalOccupationalCredential_Text_Ref] | None = Field(default=None, validation_alias="educationalCredentialAwarded", serialization_alias="educationalCredentialAwarded")
    educational_program_mode: Text | list[Text] | None = Field(default=None, validation_alias="educationalProgramMode", serialization_alias="educationalProgramMode")
    end_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="endDate", serialization_alias="endDate")
    financial_aid_eligible: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="financialAidEligible", serialization_alias="financialAidEligible")
    has_course: Course_Ref | list[Course_Ref] | None = Field(default=None, validation_alias="hasCourse", serialization_alias="hasCourse")
    maximum_enrollment: Integer | list[Integer] | None = Field(default=None, validation_alias="maximumEnrollment", serialization_alias="maximumEnrollment")
    number_of_credits: StructuredValue_Integer_Ref | list[StructuredValue_Integer_Ref] | None = Field(default=None, validation_alias="numberOfCredits", serialization_alias="numberOfCredits")
    occupational_category: CategoryCode_Text_Ref | list[CategoryCode_Text_Ref] | None = Field(default=None, validation_alias="occupationalCategory", serialization_alias="occupationalCategory")
    occupational_credential_awarded: EducationalOccupationalCredential_Text_Ref | list[EducationalOccupationalCredential_Text_Ref] | None = Field(default=None, validation_alias="occupationalCredentialAwarded", serialization_alias="occupationalCredentialAwarded")
    offers: Demand_Offer_Ref | list[Demand_Offer_Ref] | None = Field(default=None)
    program_prerequisites: R35a3a573 | list[R35a3a573] | None = Field(default=None, validation_alias="programPrerequisites", serialization_alias="programPrerequisites")
    program_type: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="programType", serialization_alias="programType")
    provider: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    salary_upon_completion: MonetaryAmountDistribution_Ref | list[MonetaryAmountDistribution_Ref] | None = Field(default=None, validation_alias="salaryUponCompletion", serialization_alias="salaryUponCompletion")
    start_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="startDate", serialization_alias="startDate")
    term_duration: Text | list[Text] | None = Field(default=None, validation_alias="termDuration", serialization_alias="termDuration")
    terms_per_year: Number | list[Number] | None = Field(default=None, validation_alias="termsPerYear", serialization_alias="termsPerYear")
    time_of_day: Text | list[Text] | None = Field(default=None, validation_alias="timeOfDay", serialization_alias="timeOfDay")
    time_to_complete: Text | list[Text] | None = Field(default=None, validation_alias="timeToComplete", serialization_alias="timeToComplete")
    training_salary: MonetaryAmountDistribution_Ref | list[MonetaryAmountDistribution_Ref] | None = Field(default=None, validation_alias="trainingSalary", serialization_alias="trainingSalary")
    typical_credits_per_term: StructuredValue_Integer_Ref | list[StructuredValue_Integer_Ref] | None = Field(default=None, validation_alias="typicalCreditsPerTerm", serialization_alias="typicalCreditsPerTerm")
