from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_indication import MedicalIndication


class ApprovedIndication(MedicalIndication):
    """An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US."""
    schema_type: ClassVar[str] = "ApprovedIndication"
