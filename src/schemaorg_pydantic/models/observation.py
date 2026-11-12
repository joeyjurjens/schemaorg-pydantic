from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref, Text
from .quantitative_value import QuantitativeValue
from .measurement_method_enum import MeasurementMethodEnum

if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .enumeration import Enumeration
    from .place import Place
    from .property import Property
    from .property_value import PropertyValue
    from .statistical_variable import StatisticalVariable
    from .thing import Thing

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    DefinedTerm_MeasurementMethodEnum_Text_Ref = Union[DefinedTerm, MeasurementMethodEnum, Text, Ref]
else:
    DefinedTerm_MeasurementMethodEnum_Text_Ref = Union[Is["DefinedTerm"], MeasurementMethodEnum, Text, Ref]

if TYPE_CHECKING:
    Enumeration_Ref = Union[Enumeration, Ref]
else:
    Enumeration_Ref = Union[Is["Enumeration"], Ref]

if TYPE_CHECKING:
    Place_Thing_Ref = Union[Place, Thing, Ref]
else:
    Place_Thing_Ref = Union[Is["Place"], Is["Thing"], Ref]

if TYPE_CHECKING:
    R553323fd = Union[Property, PropertyValue, StatisticalVariable, Text, Ref]
else:
    R553323fd = Union[Is["Property"], Is["PropertyValue"], Is["StatisticalVariable"], Text, Ref]

if TYPE_CHECKING:
    Property_Ref = Union[Property, Ref]
else:
    Property_Ref = Union[Is["Property"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

if TYPE_CHECKING:
    StatisticalVariable_Ref = Union[StatisticalVariable, Ref]
else:
    StatisticalVariable_Ref = Union[Is["StatisticalVariable"], Ref]


class Observation(QuantitativeValue):
    """Instances of the class [[Observation]] are used to specify observations about an entity at a particular time. The principal properties of an [[Observation]] are [[observationAbout]], [[measuredProperty]], [[statType]], [[value] and [[observationDate]]  and [[measuredProperty]]. Some but not all Observations represent a [[QuantitativeValue]]. Quantitative observations can be about a [[StatisticalVariable]], which is an abstract specification about which we can make observations that are grounded at a particular location and time."""
    schema_type: ClassVar[str] = "Observation"
    margin_of_error: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="marginOfError", serialization_alias="marginOfError")
    measured_property: Property_Ref | list[Property_Ref] | None = Field(default=None, validation_alias="measuredProperty", serialization_alias="measuredProperty")
    measurement_denominator: StatisticalVariable_Ref | list[StatisticalVariable_Ref] | None = Field(default=None, validation_alias="measurementDenominator", serialization_alias="measurementDenominator")
    measurement_method: DefinedTerm_MeasurementMethodEnum_Text_Ref | list[DefinedTerm_MeasurementMethodEnum_Text_Ref] | None = Field(default=None, validation_alias="measurementMethod", serialization_alias="measurementMethod")
    measurement_qualifier: Enumeration_Ref | list[Enumeration_Ref] | None = Field(default=None, validation_alias="measurementQualifier", serialization_alias="measurementQualifier")
    measurement_technique: DefinedTerm_MeasurementMethodEnum_Text_Ref | list[DefinedTerm_MeasurementMethodEnum_Text_Ref] | None = Field(default=None, validation_alias="measurementTechnique", serialization_alias="measurementTechnique")
    observation_about: Place_Thing_Ref | list[Place_Thing_Ref] | None = Field(default=None, validation_alias="observationAbout", serialization_alias="observationAbout")
    observation_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="observationDate", serialization_alias="observationDate")
    observation_period: Text | list[Text] | None = Field(default=None, validation_alias="observationPeriod", serialization_alias="observationPeriod")
    variable_measured: R553323fd | list[R553323fd] | None = Field(default=None, validation_alias="variableMeasured", serialization_alias="variableMeasured")
