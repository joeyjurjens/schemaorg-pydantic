from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .review import Review


class UserReview(Review):
    """A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast with [[CriticReview]]."""
    schema_type: ClassVar[str] = "UserReview"
