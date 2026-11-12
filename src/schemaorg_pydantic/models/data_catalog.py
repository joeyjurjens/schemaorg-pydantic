from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork
from .measurement_method_enum import MeasurementMethodEnum

if TYPE_CHECKING:
    from .dataset import Dataset
    from .defined_term import DefinedTerm

if TYPE_CHECKING:
    Dataset_Ref = Union[Dataset, Ref]
else:
    Dataset_Ref = Union[Is["Dataset"], Ref]

if TYPE_CHECKING:
    DefinedTerm_MeasurementMethodEnum_Text_Ref = Union[DefinedTerm, MeasurementMethodEnum, Text, Ref]
else:
    DefinedTerm_MeasurementMethodEnum_Text_Ref = Union[Is["DefinedTerm"], MeasurementMethodEnum, Text, Ref]


class DataCatalog(CreativeWork):
    """A collection of datasets."""
    schema_type: ClassVar[str] = "DataCatalog"
    dataset: Dataset_Ref | list[Dataset_Ref] | None = Field(default=None)
    measurement_method: DefinedTerm_MeasurementMethodEnum_Text_Ref | list[DefinedTerm_MeasurementMethodEnum_Text_Ref] | None = Field(default=None, validation_alias="measurementMethod", serialization_alias="measurementMethod")
    measurement_technique: DefinedTerm_MeasurementMethodEnum_Text_Ref | list[DefinedTerm_MeasurementMethodEnum_Text_Ref] | None = Field(default=None, validation_alias="measurementTechnique", serialization_alias="measurementTechnique")
