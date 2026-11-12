from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .church import Church


class CatholicChurch(Church):
    """A Catholic church."""
    schema_type: ClassVar[str] = "CatholicChurch"
