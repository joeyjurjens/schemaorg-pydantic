from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .transfer_action import TransferAction


class TakeAction(TransferAction):
    """The act of gaining ownership of an object from an origin. Reciprocal of GiveAction."""
    schema_type: ClassVar[str] = "TakeAction"
