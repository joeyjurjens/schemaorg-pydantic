from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .comment import Comment


class CorrectionComment(Comment):
    """A [[comment]] that corrects [[CreativeWork]]."""
    schema_type: ClassVar[str] = "CorrectionComment"
