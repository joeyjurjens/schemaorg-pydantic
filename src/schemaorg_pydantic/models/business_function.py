from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class BusinessFunction(Enumeration):
    """The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class."""
    schema_type: ClassVar[str] = "BusinessFunction"
