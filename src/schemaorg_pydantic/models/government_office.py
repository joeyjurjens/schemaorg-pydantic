from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class GovernmentOffice(LocalBusiness):
    """A government office&#x2014;for example, an IRS or DMV office."""
    schema_type: ClassVar[str] = "GovernmentOffice"
