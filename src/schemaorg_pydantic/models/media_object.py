from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, DateTime, Is, Ref, Text, Time, Url
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .geo_shape import GeoShape
    from .media_subscription import MediaSubscription
    from .news_article import NewsArticle
    from .organization import Organization
    from .place import Place
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    CreativeWork_Ref = Union[CreativeWork, Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]

Date_DateTime = Union[Date, DateTime]
DateTime_Time = Union[DateTime, Time]
if TYPE_CHECKING:
    GeoShape_Place_Text_Ref = Union[GeoShape, Place, Text, Ref]
else:
    GeoShape_Place_Text_Ref = Union[Is["GeoShape"], Is["Place"], Text, Ref]

if TYPE_CHECKING:
    MediaSubscription_Boolean_Ref = Union[MediaSubscription, Boolean, Ref]
else:
    MediaSubscription_Boolean_Ref = Union[Is["MediaSubscription"], Boolean, Ref]

if TYPE_CHECKING:
    NewsArticle_Ref = Union[NewsArticle, Ref]
else:
    NewsArticle_Ref = Union[Is["NewsArticle"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class MediaObject(CreativeWork):
    """A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset i.e. DataDownload. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's)."""
    schema_type: ClassVar[str] = "MediaObject"
    associated_article: NewsArticle_Ref | list[NewsArticle_Ref] | None = Field(default=None, validation_alias="associatedArticle", serialization_alias="associatedArticle")
    bitrate: Text | list[Text] | None = Field(default=None)
    content_size: Text | list[Text] | None = Field(default=None, validation_alias="contentSize", serialization_alias="contentSize")
    content_url: Url | list[Url] | None = Field(default=None, validation_alias="contentUrl", serialization_alias="contentUrl")
    duration: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    embed_url: Url | list[Url] | None = Field(default=None, validation_alias="embedUrl", serialization_alias="embedUrl")
    encodes_creative_work: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="encodesCreativeWork", serialization_alias="encodesCreativeWork")
    end_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="endTime", serialization_alias="endTime")
    height: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    ineligible_region: GeoShape_Place_Text_Ref | list[GeoShape_Place_Text_Ref] | None = Field(default=None, validation_alias="ineligibleRegion", serialization_alias="ineligibleRegion")
    player_type: Text | list[Text] | None = Field(default=None, validation_alias="playerType", serialization_alias="playerType")
    production_company: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="productionCompany", serialization_alias="productionCompany")
    regions_allowed: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="regionsAllowed", serialization_alias="regionsAllowed")
    requires_subscription: MediaSubscription_Boolean_Ref | list[MediaSubscription_Boolean_Ref] | None = Field(default=None, validation_alias="requiresSubscription", serialization_alias="requiresSubscription")
    sha_256: Text | list[Text] | None = Field(default=None, validation_alias="sha256", serialization_alias="sha256")
    start_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="startTime", serialization_alias="startTime")
    upload_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="uploadDate", serialization_alias="uploadDate")
    width: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
