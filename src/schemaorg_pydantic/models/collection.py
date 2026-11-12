from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Integer
from .creative_work import CreativeWork


class Collection(CreativeWork):
    """A collection of items, e.g. creative works or products."""
    schema_type: ClassVar[str] = "Collection"
    collection_size: Integer | list[Integer] | None = Field(default=None, validation_alias="collectionSize", serialization_alias="collectionSize")
