from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .constraint_node import ConstraintNode
from .measurement_method_enum import MeasurementMethodEnum

if TYPE_CHECKING:
    from .class_ import Class
    from .defined_term import DefinedTerm
    from .enumeration import Enumeration
    from .property import Property

if TYPE_CHECKING:
    Class_Ref = Union[Class, Ref]
else:
    Class_Ref = Union[Is["Class"], Ref]

if TYPE_CHECKING:
    DefinedTerm_MeasurementMethodEnum_Text_Ref = Union[DefinedTerm, MeasurementMethodEnum, Text, Ref]
else:
    DefinedTerm_MeasurementMethodEnum_Text_Ref = Union[Is["DefinedTerm"], MeasurementMethodEnum, Text, Ref]

if TYPE_CHECKING:
    Enumeration_Ref = Union[Enumeration, Ref]
else:
    Enumeration_Ref = Union[Is["Enumeration"], Ref]

if TYPE_CHECKING:
    Property_Ref = Union[Property, Ref]
else:
    Property_Ref = Union[Is["Property"], Ref]

if TYPE_CHECKING:
    Property_Text_Ref = Union[Property, Text, Ref]
else:
    Property_Text_Ref = Union[Is["Property"], Text, Ref]

if TYPE_CHECKING:
    StatisticalVariable_Ref = Union["StatisticalVariable", Ref]
else:
    StatisticalVariable_Ref = Union[Is["StatisticalVariable"], Ref]


class StatisticalVariable(ConstraintNode):
    """[[StatisticalVariable]] represents any type of statistical metric that can be measured at a place and time. The usage pattern for [[StatisticalVariable]] is typically expressed using [[Observation]] with an explicit [[populationType]], which is a type, typically drawn from Schema.org. Each [[StatisticalVariable]] is marked as a [[ConstraintNode]], meaning that some properties (those listed using [[constraintProperty]]) serve in this setting solely to define the statistical variable rather than literally describe a specific person, place or thing. For example, a [[StatisticalVariable]] Median_Height_Person_Female representing the median height of women, could be written as follows: the population type is [[Person]]; the measuredProperty [[height]]; the [[statType]] [[median]]; the [[gender]] [[Female]]. It is important to note that there are many kinds of scientific quantitative observation which are not fully, perfectly or unambiguously described following this pattern, or with solely Schema.org terminology. The approach taken here is designed to allow partial, incremental or minimal description of [[StatisticalVariable]]s, and the use of detailed sets of entity and property IDs from external repositories. The [[measurementMethod]], [[unitCode]] and [[unitText]] properties can also be used to clarify the specific nature and notation of an observed measurement."""
    schema_type: ClassVar[str] = "StatisticalVariable"
    measured_property: Property_Ref | list[Property_Ref] | None = Field(default=None, validation_alias="measuredProperty", serialization_alias="measuredProperty")
    measurement_denominator: StatisticalVariable_Ref | list[StatisticalVariable_Ref] | None = Field(default=None, validation_alias="measurementDenominator", serialization_alias="measurementDenominator")
    measurement_method: DefinedTerm_MeasurementMethodEnum_Text_Ref | list[DefinedTerm_MeasurementMethodEnum_Text_Ref] | None = Field(default=None, validation_alias="measurementMethod", serialization_alias="measurementMethod")
    measurement_qualifier: Enumeration_Ref | list[Enumeration_Ref] | None = Field(default=None, validation_alias="measurementQualifier", serialization_alias="measurementQualifier")
    measurement_technique: DefinedTerm_MeasurementMethodEnum_Text_Ref | list[DefinedTerm_MeasurementMethodEnum_Text_Ref] | None = Field(default=None, validation_alias="measurementTechnique", serialization_alias="measurementTechnique")
    population_type: Class_Ref | list[Class_Ref] | None = Field(default=None, validation_alias="populationType", serialization_alias="populationType")
    stat_type: Property_Text_Ref | list[Property_Text_Ref] | None = Field(default=None, validation_alias="statType", serialization_alias="statType")
