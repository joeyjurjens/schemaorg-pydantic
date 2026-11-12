from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .message import Message


class EmailMessage(Message):
    """An email message."""
    schema_type: ClassVar[str] = "EmailMessage"
