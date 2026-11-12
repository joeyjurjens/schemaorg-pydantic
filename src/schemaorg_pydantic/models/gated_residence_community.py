from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .residence import Residence


class GatedResidenceCommunity(Residence):
    """Residence type: Gated community."""
    schema_type: ClassVar[str] = "GatedResidenceCommunity"
