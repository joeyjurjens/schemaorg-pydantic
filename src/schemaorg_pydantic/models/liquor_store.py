from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class LiquorStore(Store):
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits."""
    schema_type: ClassVar[str] = "LiquorStore"
