from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .dataset import Dataset

if TYPE_CHECKING:
    from .data_feed_item import DataFeedItem
    from .thing import Thing

if TYPE_CHECKING:
    DataFeedItem_Thing_Text_Ref = Union[DataFeedItem, Thing, Text, Ref]
else:
    DataFeedItem_Thing_Text_Ref = Union[Is["DataFeedItem"], Is["Thing"], Text, Ref]


class DataFeed(Dataset):
    """A single feed providing structured information about one or more entities or topics."""
    schema_type: ClassVar[str] = "DataFeed"
    data_feed_element: DataFeedItem_Thing_Text_Ref | list[DataFeedItem_Thing_Text_Ref] | None = Field(default=None, validation_alias="dataFeedElement", serialization_alias="dataFeedElement")
