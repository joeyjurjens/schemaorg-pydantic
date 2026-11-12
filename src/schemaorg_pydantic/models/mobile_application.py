from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .software_application import SoftwareApplication


class MobileApplication(SoftwareApplication):
    """A software application designed specifically to work well on a mobile device such as a telephone."""
    schema_type: ClassVar[str] = "MobileApplication"
    carrier_requirements: Text | list[Text] | None = Field(default=None, validation_alias="carrierRequirements", serialization_alias="carrierRequirements")
