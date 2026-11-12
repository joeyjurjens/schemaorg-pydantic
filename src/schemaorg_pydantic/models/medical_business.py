from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class MedicalBusiness(LocalBusiness):
    """A particular physical or virtual business of an organization for medical purposes. Examples of MedicalBusiness include different businesses run by health professionals."""
    schema_type: ClassVar[str] = "MedicalBusiness"
