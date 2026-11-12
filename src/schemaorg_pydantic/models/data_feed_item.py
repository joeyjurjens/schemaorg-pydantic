from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref, Url
from .intangible import Intangible

if TYPE_CHECKING:
    from .thing import Thing

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    Thing_Url_Ref = Union[Thing, Url, Ref]
else:
    Thing_Url_Ref = Union[Is["Thing"], Url, Ref]


class DataFeedItem(Intangible):
    """A single item within a larger data feed."""
    schema_type: ClassVar[str] = "DataFeedItem"
    date_created: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="dateCreated", serialization_alias="dateCreated")
    date_deleted: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="dateDeleted", serialization_alias="dateDeleted")
    date_modified: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="dateModified", serialization_alias="dateModified")
    item: Thing_Url_Ref | list[Thing_Url_Ref] | None = Field(default=None)
