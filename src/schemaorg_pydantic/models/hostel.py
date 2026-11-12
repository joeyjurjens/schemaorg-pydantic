from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .lodging_business import LodgingBusiness


class Hostel(LodgingBusiness):
    """A hostel - cheap accommodation, often in shared dormitories.\n<br /><br />\nSee also the <a href=\"/docs/hotels.html\">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>."""
    schema_type: ClassVar[str] = "Hostel"
