from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .room import Room


class HotelRoom(Room):
    """A hotel room is a single room in a hotel.\n<br /><br />\nSee also the <a href=\"/docs/hotels.html\">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>."""
    schema_type: ClassVar[str] = "HotelRoom"
