from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, DateTime, Integer, Is, Number, Ref, Text, Url
from .thing import Thing
from .iptc_digital_source_enumeration import IPTCDigitalSourceEnumeration

if TYPE_CHECKING:
    from .aggregate_rating import AggregateRating
    from .alignment_object import AlignmentObject
    from .audience import Audience
    from .audio_object import AudioObject
    from .claim import Claim
    from .clip import Clip
    from .comment import Comment
    from .correction_comment import CorrectionComment
    from .country import Country
    from .defined_term import DefinedTerm
    from .demand import Demand
    from .event import Event
    from .grant import Grant
    from .image_object import ImageObject
    from .interaction_counter import InteractionCounter
    from .item_list import ItemList
    from .language import Language
    from .media_object import MediaObject
    from .music_recording import MusicRecording
    from .offer import Offer
    from .organization import Organization
    from .person import Person
    from .place import Place
    from .product import Product
    from .publication_event import PublicationEvent
    from .quantitative_value import QuantitativeValue
    from .rating import Rating
    from .review import Review
    from .size_specification import SizeSpecification
    from .video_object import VideoObject
    from .web_page import WebPage

if TYPE_CHECKING:
    AggregateRating_Ref = Union[AggregateRating, Ref]
else:
    AggregateRating_Ref = Union[Is["AggregateRating"], Ref]

if TYPE_CHECKING:
    AlignmentObject_Ref = Union[AlignmentObject, Ref]
else:
    AlignmentObject_Ref = Union[Is["AlignmentObject"], Ref]

if TYPE_CHECKING:
    Audience_Ref = Union[Audience, Ref]
else:
    Audience_Ref = Union[Is["Audience"], Ref]

if TYPE_CHECKING:
    AudioObject_Clip_MusicRecording_Ref = Union[AudioObject, Clip, MusicRecording, Ref]
else:
    AudioObject_Clip_MusicRecording_Ref = Union[Is["AudioObject"], Is["Clip"], Is["MusicRecording"], Ref]

if TYPE_CHECKING:
    Claim_Ref = Union[Claim, Ref]
else:
    Claim_Ref = Union[Is["Claim"], Ref]

if TYPE_CHECKING:
    Clip_VideoObject_Ref = Union[Clip, VideoObject, Ref]
else:
    Clip_VideoObject_Ref = Union[Is["Clip"], Is["VideoObject"], Ref]

if TYPE_CHECKING:
    Comment_Ref = Union[Comment, Ref]
else:
    Comment_Ref = Union[Is["Comment"], Ref]

if TYPE_CHECKING:
    CorrectionComment_Text_Ref = Union[CorrectionComment, Text, Ref]
else:
    CorrectionComment_Text_Ref = Union[Is["CorrectionComment"], Text, Ref]

if TYPE_CHECKING:
    Country_Ref = Union[Country, Ref]
else:
    Country_Ref = Union[Is["Country"], Ref]

if TYPE_CHECKING:
    CreativeWork_Product_Url_Ref = Union["CreativeWork", Product, Url, Ref]
else:
    CreativeWork_Product_Url_Ref = Union[Is["CreativeWork"], Is["Product"], Url, Ref]

if TYPE_CHECKING:
    CreativeWork_Ref = Union["CreativeWork", Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]

if TYPE_CHECKING:
    CreativeWork_Text_Ref = Union["CreativeWork", Text, Ref]
else:
    CreativeWork_Text_Ref = Union[Is["CreativeWork"], Text, Ref]

if TYPE_CHECKING:
    CreativeWork_Url_Ref = Union["CreativeWork", Url, Ref]
else:
    CreativeWork_Url_Ref = Union[Is["CreativeWork"], Url, Ref]

Date_DateTime = Union[Date, DateTime]
DateTime_Text = Union[DateTime, Text]
if TYPE_CHECKING:
    R5bddb616 = Union[DefinedTerm, QuantitativeValue, SizeSpecification, Text, Ref]
else:
    R5bddb616 = Union[Is["DefinedTerm"], Is["QuantitativeValue"], Is["SizeSpecification"], Text, Ref]

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    Demand_Offer_Ref = Union[Demand, Offer, Ref]
else:
    Demand_Offer_Ref = Union[Is["Demand"], Is["Offer"], Ref]

if TYPE_CHECKING:
    Event_Ref = Union[Event, Ref]
else:
    Event_Ref = Union[Is["Event"], Ref]

if TYPE_CHECKING:
    Grant_Ref = Union[Grant, Ref]
else:
    Grant_Ref = Union[Is["Grant"], Ref]

if TYPE_CHECKING:
    ImageObject_Ref = Union[ImageObject, Ref]
else:
    ImageObject_Ref = Union[Is["ImageObject"], Ref]

Integer_Text = Union[Integer, Text]
if TYPE_CHECKING:
    InteractionCounter_Ref = Union[InteractionCounter, Ref]
else:
    InteractionCounter_Ref = Union[Is["InteractionCounter"], Ref]

if TYPE_CHECKING:
    ItemList_Ref = Union[ItemList, Ref]
else:
    ItemList_Ref = Union[Is["ItemList"], Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    MediaObject_Ref = Union[MediaObject, Ref]
else:
    MediaObject_Ref = Union[Is["MediaObject"], Ref]

Number_Text = Union[Number, Text]
if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    Product_Text_Ref = Union[Product, Text, Ref]
else:
    Product_Text_Ref = Union[Is["Product"], Text, Ref]

if TYPE_CHECKING:
    PublicationEvent_Ref = Union[PublicationEvent, Ref]
else:
    PublicationEvent_Ref = Union[Is["PublicationEvent"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]

if TYPE_CHECKING:
    Rating_Text_Ref = Union[Rating, Text, Ref]
else:
    Rating_Text_Ref = Union[Is["Rating"], Text, Ref]

if TYPE_CHECKING:
    Review_Ref = Union[Review, Ref]
else:
    Review_Ref = Union[Is["Review"], Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]

if TYPE_CHECKING:
    WebPage_Url_Ref = Union[WebPage, Url, Ref]
else:
    WebPage_Url_Ref = Union[Is["WebPage"], Url, Ref]


class CreativeWork(Thing):
    """The most generic kind of creative work, including books, movies, photographs, software programs, etc."""
    schema_type: ClassVar[str] = "CreativeWork"
    about: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    abstract: Text | list[Text] | None = Field(default=None)
    access_mode: Text | list[Text] | None = Field(default=None, validation_alias="accessMode", serialization_alias="accessMode")
    access_mode_sufficient: ItemList_Ref | list[ItemList_Ref] | None = Field(default=None, validation_alias="accessModeSufficient", serialization_alias="accessModeSufficient")
    accessibility_api: Text | list[Text] | None = Field(default=None, validation_alias="accessibilityAPI", serialization_alias="accessibilityAPI")
    accessibility_control: Text | list[Text] | None = Field(default=None, validation_alias="accessibilityControl", serialization_alias="accessibilityControl")
    accessibility_feature: Text | list[Text] | None = Field(default=None, validation_alias="accessibilityFeature", serialization_alias="accessibilityFeature")
    accessibility_hazard: Text | list[Text] | None = Field(default=None, validation_alias="accessibilityHazard", serialization_alias="accessibilityHazard")
    accessibility_summary: Text | list[Text] | None = Field(default=None, validation_alias="accessibilitySummary", serialization_alias="accessibilitySummary")
    accountable_person: Person_Ref | list[Person_Ref] | None = Field(default=None, validation_alias="accountablePerson", serialization_alias="accountablePerson")
    acquire_license_page: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="acquireLicensePage", serialization_alias="acquireLicensePage")
    aggregate_rating: AggregateRating_Ref | list[AggregateRating_Ref] | None = Field(default=None, validation_alias="aggregateRating", serialization_alias="aggregateRating")
    alternative_headline: Text | list[Text] | None = Field(default=None, validation_alias="alternativeHeadline", serialization_alias="alternativeHeadline")
    archived_at: WebPage_Url_Ref | list[WebPage_Url_Ref] | None = Field(default=None, validation_alias="archivedAt", serialization_alias="archivedAt")
    assesses: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    associated_media: MediaObject_Ref | list[MediaObject_Ref] | None = Field(default=None, validation_alias="associatedMedia", serialization_alias="associatedMedia")
    audience: Audience_Ref | list[Audience_Ref] | None = Field(default=None)
    audio: AudioObject_Clip_MusicRecording_Ref | list[AudioObject_Clip_MusicRecording_Ref] | None = Field(default=None)
    author: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    award: Text | list[Text] | None = Field(default=None)
    character: Person_Ref | list[Person_Ref] | None = Field(default=None)
    citation: CreativeWork_Text_Ref | list[CreativeWork_Text_Ref] | None = Field(default=None)
    comment: Comment_Ref | list[Comment_Ref] | None = Field(default=None)
    comment_count: Integer | list[Integer] | None = Field(default=None, validation_alias="commentCount", serialization_alias="commentCount")
    conditions_of_access: Text | list[Text] | None = Field(default=None, validation_alias="conditionsOfAccess", serialization_alias="conditionsOfAccess")
    content_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="contentLocation", serialization_alias="contentLocation")
    content_rating: Rating_Text_Ref | list[Rating_Text_Ref] | None = Field(default=None, validation_alias="contentRating", serialization_alias="contentRating")
    content_reference_time: DateTime | list[DateTime] | None = Field(default=None, validation_alias="contentReferenceTime", serialization_alias="contentReferenceTime")
    contributor: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    copyright_holder: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="copyrightHolder", serialization_alias="copyrightHolder")
    copyright_notice: Text | list[Text] | None = Field(default=None, validation_alias="copyrightNotice", serialization_alias="copyrightNotice")
    copyright_year: Number | list[Number] | None = Field(default=None, validation_alias="copyrightYear", serialization_alias="copyrightYear")
    correction: CorrectionComment_Text_Ref | list[CorrectionComment_Text_Ref] | None = Field(default=None)
    country_of_origin: Country_Ref | list[Country_Ref] | None = Field(default=None, validation_alias="countryOfOrigin", serialization_alias="countryOfOrigin")
    creative_work_status: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="creativeWorkStatus", serialization_alias="creativeWorkStatus")
    creator: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    credit_text: Text | list[Text] | None = Field(default=None, validation_alias="creditText", serialization_alias="creditText")
    date_created: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="dateCreated", serialization_alias="dateCreated")
    date_modified: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="dateModified", serialization_alias="dateModified")
    date_published: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="datePublished", serialization_alias="datePublished")
    digital_source_type: IPTCDigitalSourceEnumeration | list[IPTCDigitalSourceEnumeration] | None = Field(default=None, validation_alias="digitalSourceType", serialization_alias="digitalSourceType")
    discussion_url: Url | list[Url] | None = Field(default=None, validation_alias="discussionUrl", serialization_alias="discussionUrl")
    display_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="displayLocation", serialization_alias="displayLocation")
    edit_eidr: Text | list[Text] | None = Field(default=None, validation_alias="editEIDR", serialization_alias="editEIDR")
    editor: Person_Ref | list[Person_Ref] | None = Field(default=None)
    educational_alignment: AlignmentObject_Ref | list[AlignmentObject_Ref] | None = Field(default=None, validation_alias="educationalAlignment", serialization_alias="educationalAlignment")
    educational_level: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="educationalLevel", serialization_alias="educationalLevel")
    educational_use: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="educationalUse", serialization_alias="educationalUse")
    encoding: MediaObject_Ref | list[MediaObject_Ref] | None = Field(default=None)
    encoding_format: Text | list[Text] | None = Field(default=None, validation_alias="encodingFormat", serialization_alias="encodingFormat")
    example_of_work: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="exampleOfWork", serialization_alias="exampleOfWork")
    expires: Date_DateTime | list[Date_DateTime] | None = Field(default=None)
    funder: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    funding: Grant_Ref | list[Grant_Ref] | None = Field(default=None)
    genre: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    has_part: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="hasPart", serialization_alias="hasPart")
    headline: Text | list[Text] | None = Field(default=None)
    in_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="inLanguage", serialization_alias="inLanguage")
    interaction_statistic: InteractionCounter_Ref | list[InteractionCounter_Ref] | None = Field(default=None, validation_alias="interactionStatistic", serialization_alias="interactionStatistic")
    interactivity_type: Text | list[Text] | None = Field(default=None, validation_alias="interactivityType", serialization_alias="interactivityType")
    interpreted_as_claim: Claim_Ref | list[Claim_Ref] | None = Field(default=None, validation_alias="interpretedAsClaim", serialization_alias="interpretedAsClaim")
    is_accessible_for_free: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isAccessibleForFree", serialization_alias="isAccessibleForFree")
    is_based_on: CreativeWork_Product_Url_Ref | list[CreativeWork_Product_Url_Ref] | None = Field(default=None, validation_alias="isBasedOn", serialization_alias="isBasedOn")
    is_family_friendly: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isFamilyFriendly", serialization_alias="isFamilyFriendly")
    is_part_of: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="isPartOf", serialization_alias="isPartOf")
    keywords: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    learning_resource_type: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="learningResourceType", serialization_alias="learningResourceType")
    license: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None)
    location_created: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="locationCreated", serialization_alias="locationCreated")
    main_entity: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="mainEntity", serialization_alias="mainEntity")
    maintainer: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    material: Product_Text_Ref | list[Product_Text_Ref] | None = Field(default=None)
    material_extent: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="materialExtent", serialization_alias="materialExtent")
    mentions: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    offers: Demand_Offer_Ref | list[Demand_Offer_Ref] | None = Field(default=None)
    pattern: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    position: Integer_Text | list[Integer_Text] | None = Field(default=None)
    producer: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    provider: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    publication: PublicationEvent_Ref | list[PublicationEvent_Ref] | None = Field(default=None)
    publisher: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    publisher_imprint: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="publisherImprint", serialization_alias="publisherImprint")
    publishing_principles: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="publishingPrinciples", serialization_alias="publishingPrinciples")
    recorded_at: Event_Ref | list[Event_Ref] | None = Field(default=None, validation_alias="recordedAt", serialization_alias="recordedAt")
    released_event: PublicationEvent_Ref | list[PublicationEvent_Ref] | None = Field(default=None, validation_alias="releasedEvent", serialization_alias="releasedEvent")
    review: Review_Ref | list[Review_Ref] | None = Field(default=None)
    schema_version: Text | list[Text] | None = Field(default=None, validation_alias="schemaVersion", serialization_alias="schemaVersion")
    sd_date_published: Date | list[Date] | None = Field(default=None, validation_alias="sdDatePublished", serialization_alias="sdDatePublished")
    sd_license: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="sdLicense", serialization_alias="sdLicense")
    sd_publisher: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="sdPublisher", serialization_alias="sdPublisher")
    size: R5bddb616 | list[R5bddb616] | None = Field(default=None)
    source_organization: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="sourceOrganization", serialization_alias="sourceOrganization")
    spatial: Place_Ref | list[Place_Ref] | None = Field(default=None)
    spatial_coverage: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="spatialCoverage", serialization_alias="spatialCoverage")
    sponsor: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    teaches: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    temporal: DateTime_Text | list[DateTime_Text] | None = Field(default=None)
    temporal_coverage: DateTime_Text | list[DateTime_Text] | None = Field(default=None, validation_alias="temporalCoverage", serialization_alias="temporalCoverage")
    text: Text | list[Text] | None = Field(default=None)
    thumbnail: ImageObject_Ref | list[ImageObject_Ref] | None = Field(default=None)
    thumbnail_url: Url | list[Url] | None = Field(default=None, validation_alias="thumbnailUrl", serialization_alias="thumbnailUrl")
    time_required: Text | list[Text] | None = Field(default=None, validation_alias="timeRequired", serialization_alias="timeRequired")
    translation_of_work: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="translationOfWork", serialization_alias="translationOfWork")
    translator: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    typical_age_range: Text | list[Text] | None = Field(default=None, validation_alias="typicalAgeRange", serialization_alias="typicalAgeRange")
    usage_info: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="usageInfo", serialization_alias="usageInfo")
    version: Number_Text | list[Number_Text] | None = Field(default=None)
    video: Clip_VideoObject_Ref | list[Clip_VideoObject_Ref] | None = Field(default=None)
    word_count: Integer | list[Integer] | None = Field(default=None, validation_alias="wordCount", serialization_alias="wordCount")
    work_example: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="workExample", serialization_alias="workExample")
    work_translation: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="workTranslation", serialization_alias="workTranslation")
