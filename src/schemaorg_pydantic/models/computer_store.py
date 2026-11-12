from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class ComputerStore(Store):
    """A computer store."""
    schema_type: ClassVar[str] = "ComputerStore"
