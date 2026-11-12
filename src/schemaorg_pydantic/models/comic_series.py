from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .periodical import Periodical


class ComicSeries(Periodical):
    """A sequential publication of comic stories under a\n    \tunifying title, for example \"The Amazing Spider-Man\" or \"Groo the\n    \tWanderer\"."""
    schema_type: ClassVar[str] = "ComicSeries"
