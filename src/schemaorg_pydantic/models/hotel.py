from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .lodging_business import LodgingBusiness


class Hotel(LodgingBusiness):
    """A hotel is an establishment that provides lodging paid on a short-term basis (source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Hotel).\n<br /><br />\nSee also the <a href=\"/docs/hotels.html\">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>."""
    schema_type: ClassVar[str] = "Hotel"
