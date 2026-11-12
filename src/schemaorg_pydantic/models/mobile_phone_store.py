from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class MobilePhoneStore(Store):
    """A store that sells mobile phones and related accessories."""
    schema_type: ClassVar[str] = "MobilePhoneStore"
