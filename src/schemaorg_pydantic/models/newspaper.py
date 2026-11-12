from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .periodical import Periodical


class Newspaper(Periodical):
    """A publication containing information about varied topics that are pertinent to general information, a geographic area, or a specific subject matter (i.e. business, culture, education). Often published daily."""
    schema_type: ClassVar[str] = "Newspaper"
