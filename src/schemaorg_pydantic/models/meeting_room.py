from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .room import Room


class MeetingRoom(Room):
    """A meeting room, conference room, or conference hall is a room provided for singular events such as business conferences and meetings (source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/Conference_hall\">http://en.wikipedia.org/wiki/Conference_hall</a>).\n<br /><br />\nSee also the <a href=\"/docs/hotels.html\">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>."""
    schema_type: ClassVar[str] = "MeetingRoom"
