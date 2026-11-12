from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .educational_organization import EducationalOrganization


class ElementarySchool(EducationalOrganization):
    """An elementary school."""
    schema_type: ClassVar[str] = "ElementarySchool"
