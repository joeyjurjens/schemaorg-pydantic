from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .digital_document import DigitalDocument


class SpreadsheetDigitalDocument(DigitalDocument):
    """A spreadsheet file."""
    schema_type: ClassVar[str] = "SpreadsheetDigitalDocument"
