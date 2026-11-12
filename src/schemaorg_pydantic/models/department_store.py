from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class DepartmentStore(Store):
    """A department store."""
    schema_type: ClassVar[str] = "DepartmentStore"
