from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .government_office import GovernmentOffice


class PostOffice(GovernmentOffice):
    """A post office."""
    schema_type: ClassVar[str] = "PostOffice"
