from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .physician import Physician


class PhysiciansOffice(Physician):
    """A doctor's office or clinic."""
    schema_type: ClassVar[str] = "PhysiciansOffice"
