from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .review import Review


class EmployerReview(Review):
    """An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer, written by a current or former employee of that organization."""
    schema_type: ClassVar[str] = "EmployerReview"
