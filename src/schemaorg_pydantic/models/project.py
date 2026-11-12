from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class Project(Organization):
    """An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.\nUse properties from [[Organization]], [[subOrganization]]/[[parentOrganization]] to indicate project sub-structures."""
    schema_type: ClassVar[str] = "Project"
