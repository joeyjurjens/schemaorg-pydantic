from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .publication_event import PublicationEvent


class OnDemandEvent(PublicationEvent):
    """A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand."""
    schema_type: ClassVar[str] = "OnDemandEvent"
