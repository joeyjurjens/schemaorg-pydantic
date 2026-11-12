from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class ProfessionalService(LocalBusiness):
    """Original definition: \"provider of professional services.\""""
    schema_type: ClassVar[str] = "ProfessionalService"
