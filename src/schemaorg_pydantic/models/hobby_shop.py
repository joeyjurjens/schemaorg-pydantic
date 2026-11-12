from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class HobbyShop(Store):
    """A store that sells materials useful or necessary for various hobbies."""
    schema_type: ClassVar[str] = "HobbyShop"
