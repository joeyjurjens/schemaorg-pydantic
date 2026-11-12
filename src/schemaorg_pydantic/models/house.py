from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .accommodation import Accommodation


class House(Accommodation):
    """A house is a building or structure that has the ability to be occupied for habitation by humans or other creatures (source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/House\">http://en.wikipedia.org/wiki/House</a>)."""
    schema_type: ClassVar[str] = "House"
