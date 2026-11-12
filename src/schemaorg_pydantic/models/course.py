from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Text
from .learning_resource import LearningResource

if TYPE_CHECKING:
    from .alignment_object import AlignmentObject
    from .course_instance import CourseInstance
    from .defined_term import DefinedTerm
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .language import Language
    from .structured_value import StructuredValue
    from .syllabus import Syllabus

if TYPE_CHECKING:
    AlignmentObject_Course_Text_Ref = Union[AlignmentObject, "Course", Text, Ref]
else:
    AlignmentObject_Course_Text_Ref = Union[Is["AlignmentObject"], Is["Course"], Text, Ref]

if TYPE_CHECKING:
    CourseInstance_Ref = Union[CourseInstance, Ref]
else:
    CourseInstance_Ref = Union[Is["CourseInstance"], Ref]

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    EducationalOccupationalCredential_Text_Ref = Union[EducationalOccupationalCredential, Text, Ref]
else:
    EducationalOccupationalCredential_Text_Ref = Union[Is["EducationalOccupationalCredential"], Text, Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    StructuredValue_Integer_Ref = Union[StructuredValue, Integer, Ref]
else:
    StructuredValue_Integer_Ref = Union[Is["StructuredValue"], Integer, Ref]

if TYPE_CHECKING:
    Syllabus_Ref = Union[Syllabus, Ref]
else:
    Syllabus_Ref = Union[Is["Syllabus"], Ref]


class Course(LearningResource):
    """A description of an educational course which may be offered as distinct instances which take place at different times or take place at different locations, or be offered through different media or modes of study. An educational course is a sequence of one or more educational events and/or creative works which aims to build knowledge, competence or ability of learners."""
    schema_type: ClassVar[str] = "Course"
    available_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="availableLanguage", serialization_alias="availableLanguage")
    course_code: Text | list[Text] | None = Field(default=None, validation_alias="courseCode", serialization_alias="courseCode")
    course_prerequisites: AlignmentObject_Course_Text_Ref | list[AlignmentObject_Course_Text_Ref] | None = Field(default=None, validation_alias="coursePrerequisites", serialization_alias="coursePrerequisites")
    educational_credential_awarded: EducationalOccupationalCredential_Text_Ref | list[EducationalOccupationalCredential_Text_Ref] | None = Field(default=None, validation_alias="educationalCredentialAwarded", serialization_alias="educationalCredentialAwarded")
    financial_aid_eligible: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="financialAidEligible", serialization_alias="financialAidEligible")
    has_course_instance: CourseInstance_Ref | list[CourseInstance_Ref] | None = Field(default=None, validation_alias="hasCourseInstance", serialization_alias="hasCourseInstance")
    number_of_credits: StructuredValue_Integer_Ref | list[StructuredValue_Integer_Ref] | None = Field(default=None, validation_alias="numberOfCredits", serialization_alias="numberOfCredits")
    occupational_credential_awarded: EducationalOccupationalCredential_Text_Ref | list[EducationalOccupationalCredential_Text_Ref] | None = Field(default=None, validation_alias="occupationalCredentialAwarded", serialization_alias="occupationalCredentialAwarded")
    syllabus_sections: Syllabus_Ref | list[Syllabus_Ref] | None = Field(default=None, validation_alias="syllabusSections", serialization_alias="syllabusSections")
    total_historical_enrollment: Integer | list[Integer] | None = Field(default=None, validation_alias="totalHistoricalEnrollment", serialization_alias="totalHistoricalEnrollment")
