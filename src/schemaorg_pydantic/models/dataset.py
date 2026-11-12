from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork
from .measurement_method_enum import MeasurementMethodEnum

if TYPE_CHECKING:
    from .data_catalog import DataCatalog
    from .data_download import DataDownload
    from .defined_term import DefinedTerm
    from .property import Property
    from .property_value import PropertyValue
    from .statistical_variable import StatisticalVariable

if TYPE_CHECKING:
    DataCatalog_Ref = Union[DataCatalog, Ref]
else:
    DataCatalog_Ref = Union[Is["DataCatalog"], Ref]

if TYPE_CHECKING:
    DataDownload_Ref = Union[DataDownload, Ref]
else:
    DataDownload_Ref = Union[Is["DataDownload"], Ref]

if TYPE_CHECKING:
    DefinedTerm_MeasurementMethodEnum_Text_Ref = Union[DefinedTerm, MeasurementMethodEnum, Text, Ref]
else:
    DefinedTerm_MeasurementMethodEnum_Text_Ref = Union[Is["DefinedTerm"], MeasurementMethodEnum, Text, Ref]

if TYPE_CHECKING:
    R553323fd = Union[Property, PropertyValue, StatisticalVariable, Text, Ref]
else:
    R553323fd = Union[Is["Property"], Is["PropertyValue"], Is["StatisticalVariable"], Text, Ref]


class Dataset(CreativeWork):
    """A body of structured information describing some topic(s) of interest."""
    schema_type: ClassVar[str] = "Dataset"
    distribution: DataDownload_Ref | list[DataDownload_Ref] | None = Field(default=None)
    included_in_data_catalog: DataCatalog_Ref | list[DataCatalog_Ref] | None = Field(default=None, validation_alias="includedInDataCatalog", serialization_alias="includedInDataCatalog")
    issn: Text | list[Text] | None = Field(default=None)
    measurement_method: DefinedTerm_MeasurementMethodEnum_Text_Ref | list[DefinedTerm_MeasurementMethodEnum_Text_Ref] | None = Field(default=None, validation_alias="measurementMethod", serialization_alias="measurementMethod")
    measurement_technique: DefinedTerm_MeasurementMethodEnum_Text_Ref | list[DefinedTerm_MeasurementMethodEnum_Text_Ref] | None = Field(default=None, validation_alias="measurementTechnique", serialization_alias="measurementTechnique")
    variable_measured: R553323fd | list[R553323fd] | None = Field(default=None, validation_alias="variableMeasured", serialization_alias="variableMeasured")
