from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .certification import Certification


class DeclarationOfConformity(Certification):
    """A Declaration of Conformity (DoC), a formal document issued by a manufacturer declaring that a product meets specific regulatory requirements."""
    schema_type: ClassVar[str] = "DeclarationOfConformity"
