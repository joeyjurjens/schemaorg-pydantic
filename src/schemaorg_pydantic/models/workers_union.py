from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class WorkersUnion(Organization):
    """A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization that promotes the interests of its worker members by collectively bargaining with management, organizing, and political lobbying."""
    schema_type: ClassVar[str] = "WorkersUnion"
