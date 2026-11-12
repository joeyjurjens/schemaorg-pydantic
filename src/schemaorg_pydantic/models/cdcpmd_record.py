from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Date, DateTime, Number, Text
from .structured_value import StructuredValue

Date_DateTime = Union[Date, DateTime]
DateTime_Text = Union[DateTime, Text]

class CDCPMDRecord(StructuredValue):
    """A CDCPMDRecord is a data structure representing a record in a CDC tabular data format\n      used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for details, and the linked CDC materials for authoritative\n      definitions used as the source here."""
    schema_type: ClassVar[str] = "CDCPMDRecord"
    cvd_collection_date: DateTime_Text | list[DateTime_Text] | None = Field(default=None, validation_alias="cvdCollectionDate", serialization_alias="cvdCollectionDate")
    cvd_facility_county: Text | list[Text] | None = Field(default=None, validation_alias="cvdFacilityCounty", serialization_alias="cvdFacilityCounty")
    cvd_facility_id: Text | list[Text] | None = Field(default=None, validation_alias="cvdFacilityId", serialization_alias="cvdFacilityId")
    cvd_num_beds: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumBeds", serialization_alias="cvdNumBeds")
    cvd_num_beds_occ: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumBedsOcc", serialization_alias="cvdNumBedsOcc")
    cvd_num_c19_died: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumC19Died", serialization_alias="cvdNumC19Died")
    cvd_num_c19_ho_pats: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumC19HOPats", serialization_alias="cvdNumC19HOPats")
    cvd_num_c19_hosp_pats: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumC19HospPats", serialization_alias="cvdNumC19HospPats")
    cvd_num_c19_mech_vent_pats: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumC19MechVentPats", serialization_alias="cvdNumC19MechVentPats")
    cvd_num_c19_of_mech_vent_pats: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumC19OFMechVentPats", serialization_alias="cvdNumC19OFMechVentPats")
    cvd_num_c19_overflow_pats: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumC19OverflowPats", serialization_alias="cvdNumC19OverflowPats")
    cvd_num_icu_beds: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumICUBeds", serialization_alias="cvdNumICUBeds")
    cvd_num_icu_beds_occ: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumICUBedsOcc", serialization_alias="cvdNumICUBedsOcc")
    cvd_num_tot_beds: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumTotBeds", serialization_alias="cvdNumTotBeds")
    cvd_num_vent: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumVent", serialization_alias="cvdNumVent")
    cvd_num_vent_use: Number | list[Number] | None = Field(default=None, validation_alias="cvdNumVentUse", serialization_alias="cvdNumVentUse")
    date_posted: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="datePosted", serialization_alias="datePosted")
