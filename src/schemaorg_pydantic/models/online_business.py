from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class OnlineBusiness(Organization):
    """A particular online business, either standalone or the online part of a broader organization. Examples include an eCommerce site, an online travel booking site, an online learning site, an online logistics and shipping provider, an online (virtual) doctor, etc."""
    schema_type: ClassVar[str] = "OnlineBusiness"
