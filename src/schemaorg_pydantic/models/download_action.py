from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .transfer_action import TransferAction


class DownloadAction(TransferAction):
    """The act of downloading an object."""
    schema_type: ClassVar[str] = "DownloadAction"
