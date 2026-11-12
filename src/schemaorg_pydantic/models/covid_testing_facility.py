from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_clinic import MedicalClinic


class CovidTestingFacility(MedicalClinic):
    """A CovidTestingFacility is a [[MedicalClinic]] where testing for the COVID-19 Coronavirus\n      disease is available. If the facility is being made available from an established [[Pharmacy]], [[Hotel]], or other\n      non-medical organization, multiple types can be listed. This makes it easier to re-use existing schema.org information\n      about that place, e.g. contact info, address, opening hours. Note that in an emergency, such information may not always be reliable."""
    schema_type: ClassVar[str] = "CovidTestingFacility"
