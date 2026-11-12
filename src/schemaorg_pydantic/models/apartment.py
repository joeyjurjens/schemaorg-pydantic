from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .accommodation import Accommodation


class Apartment(Accommodation):
    """An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/Apartment\">http://en.wikipedia.org/wiki/Apartment</a>)."""
    schema_type: ClassVar[str] = "Apartment"
