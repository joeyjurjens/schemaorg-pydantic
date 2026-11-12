from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .learning_resource import LearningResource


class Quiz(LearningResource):
    """Quiz: A test of knowledge, skills and abilities."""
    schema_type: ClassVar[str] = "Quiz"
