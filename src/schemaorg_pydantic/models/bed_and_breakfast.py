from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .lodging_business import LodgingBusiness


class BedAndBreakfast(LodgingBusiness):
    """Bed and breakfast.\n<br /><br />\nSee also the <a href=\"/docs/hotels.html\">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>."""
    schema_type: ClassVar[str] = "BedAndBreakfast"
