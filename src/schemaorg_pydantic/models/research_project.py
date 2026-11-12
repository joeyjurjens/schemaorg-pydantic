from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .project import Project


class ResearchProject(Project):
    """A Research project."""
    schema_type: ClassVar[str] = "ResearchProject"
