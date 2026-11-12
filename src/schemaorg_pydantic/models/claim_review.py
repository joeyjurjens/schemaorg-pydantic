from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .review import Review


class ClaimReview(Review):
    """A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed)."""
    schema_type: ClassVar[str] = "ClaimReview"
    claim_reviewed: Text | list[Text] | None = Field(default=None, validation_alias="claimReviewed", serialization_alias="claimReviewed")
