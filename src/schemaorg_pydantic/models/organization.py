from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, Is, Ref, Text, Url
from .thing import Thing
from .de_nonprofit_type import DENonprofitType
from .it_nonprofit_type import ITNonprofitType
from .nl_nonprofit_type import NLNonprofitType
from .uk_nonprofit_type import UKNonprofitType
from .us_nonprofit_type import USNonprofitType

if TYPE_CHECKING:
    from .about_page import AboutPage
    from .administrative_area import AdministrativeArea
    from .aggregate_rating import AggregateRating
    from .article import Article
    from .brand import Brand
    from .certification import Certification
    from .contact_point import ContactPoint
    from .creative_work import CreativeWork
    from .credential import Credential
    from .defined_term import DefinedTerm
    from .demand import Demand
    from .event import Event
    from .geo_shape import GeoShape
    from .grant import Grant
    from .image_object import ImageObject
    from .interaction_counter import InteractionCounter
    from .language import Language
    from .loan_or_credit import LoanOrCredit
    from .member_program import MemberProgram
    from .member_program_tier import MemberProgramTier
    from .merchant_return_policy import MerchantReturnPolicy
    from .offer import Offer
    from .offer_catalog import OfferCatalog
    from .payment_method import PaymentMethod
    from .person import Person
    from .place import Place
    from .postal_address import PostalAddress
    from .program_membership import ProgramMembership
    from .quantitative_value import QuantitativeValue
    from .review import Review
    from .shipping_service import ShippingService
    from .virtual_location import VirtualLocation

if TYPE_CHECKING:
    AboutPage_CreativeWork_Text_Ref = Union[AboutPage, CreativeWork, Text, Ref]
else:
    AboutPage_CreativeWork_Text_Ref = Union[Is["AboutPage"], Is["CreativeWork"], Text, Ref]

if TYPE_CHECKING:
    R3fcc4ec8 = Union[AdministrativeArea, GeoShape, Place, Text, Ref]
else:
    R3fcc4ec8 = Union[Is["AdministrativeArea"], Is["GeoShape"], Is["Place"], Text, Ref]

if TYPE_CHECKING:
    AggregateRating_Ref = Union[AggregateRating, Ref]
else:
    AggregateRating_Ref = Union[Is["AggregateRating"], Ref]

if TYPE_CHECKING:
    Article_Url_Ref = Union[Article, Url, Ref]
else:
    Article_Url_Ref = Union[Is["Article"], Url, Ref]

if TYPE_CHECKING:
    Brand_Organization_Ref = Union[Brand, "Organization", Ref]
else:
    Brand_Organization_Ref = Union[Is["Brand"], Is["Organization"], Ref]

if TYPE_CHECKING:
    Certification_Ref = Union[Certification, Ref]
else:
    Certification_Ref = Union[Is["Certification"], Ref]

if TYPE_CHECKING:
    ContactPoint_Ref = Union[ContactPoint, Ref]
else:
    ContactPoint_Ref = Union[Is["ContactPoint"], Ref]

if TYPE_CHECKING:
    CreativeWork_Url_Ref = Union[CreativeWork, Url, Ref]
else:
    CreativeWork_Url_Ref = Union[Is["CreativeWork"], Url, Ref]

if TYPE_CHECKING:
    Credential_Ref = Union[Credential, Ref]
else:
    Credential_Ref = Union[Is["Credential"], Ref]

Rd4d13d4d = Union[DENonprofitType, ITNonprofitType, NLNonprofitType, UKNonprofitType, USNonprofitType]
if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    Demand_Ref = Union[Demand, Ref]
else:
    Demand_Ref = Union[Is["Demand"], Ref]

if TYPE_CHECKING:
    Event_Ref = Union[Event, Ref]
else:
    Event_Ref = Union[Is["Event"], Ref]

if TYPE_CHECKING:
    Grant_Ref = Union[Grant, Ref]
else:
    Grant_Ref = Union[Is["Grant"], Ref]

if TYPE_CHECKING:
    ImageObject_Url_Ref = Union[ImageObject, Url, Ref]
else:
    ImageObject_Url_Ref = Union[Is["ImageObject"], Url, Ref]

if TYPE_CHECKING:
    InteractionCounter_Ref = Union[InteractionCounter, Ref]
else:
    InteractionCounter_Ref = Union[Is["InteractionCounter"], Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    LoanOrCredit_PaymentMethod_Text_Ref = Union[LoanOrCredit, PaymentMethod, Text, Ref]
else:
    LoanOrCredit_PaymentMethod_Text_Ref = Union[Is["LoanOrCredit"], Is["PaymentMethod"], Text, Ref]

if TYPE_CHECKING:
    MemberProgram_Ref = Union[MemberProgram, Ref]
else:
    MemberProgram_Ref = Union[Is["MemberProgram"], Ref]

if TYPE_CHECKING:
    MemberProgramTier_Organization_ProgramMembership_Ref = Union[MemberProgramTier, "Organization", ProgramMembership, Ref]
else:
    MemberProgramTier_Organization_ProgramMembership_Ref = Union[Is["MemberProgramTier"], Is["Organization"], Is["ProgramMembership"], Ref]

if TYPE_CHECKING:
    MerchantReturnPolicy_Ref = Union[MerchantReturnPolicy, Ref]
else:
    MerchantReturnPolicy_Ref = Union[Is["MerchantReturnPolicy"], Ref]

if TYPE_CHECKING:
    Offer_Ref = Union[Offer, Ref]
else:
    Offer_Ref = Union[Is["Offer"], Ref]

if TYPE_CHECKING:
    OfferCatalog_Ref = Union[OfferCatalog, Ref]
else:
    OfferCatalog_Ref = Union[Is["OfferCatalog"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union["Organization", Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union["Organization", Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

if TYPE_CHECKING:
    R2967d0a9 = Union[Place, PostalAddress, VirtualLocation, Text, Ref]
else:
    R2967d0a9 = Union[Is["Place"], Is["PostalAddress"], Is["VirtualLocation"], Text, Ref]

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    PostalAddress_Ref = Union[PostalAddress, Ref]
else:
    PostalAddress_Ref = Union[Is["PostalAddress"], Ref]

if TYPE_CHECKING:
    PostalAddress_Text_Ref = Union[PostalAddress, Text, Ref]
else:
    PostalAddress_Text_Ref = Union[Is["PostalAddress"], Text, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

if TYPE_CHECKING:
    Review_Ref = Union[Review, Ref]
else:
    Review_Ref = Union[Is["Review"], Ref]

if TYPE_CHECKING:
    ShippingService_Ref = Union[ShippingService, Ref]
else:
    ShippingService_Ref = Union[Is["ShippingService"], Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]

if TYPE_CHECKING:
    Thing_Text_Ref = Union[Thing, Text, Ref]
else:
    Thing_Text_Ref = Union[Is["Thing"], Text, Ref]


class Organization(Thing):
    """An organization such as a school, NGO, corporation, club, etc."""
    schema_type: ClassVar[str] = "Organization"
    accepted_payment_method: LoanOrCredit_PaymentMethod_Text_Ref | list[LoanOrCredit_PaymentMethod_Text_Ref] | None = Field(default=None, validation_alias="acceptedPaymentMethod", serialization_alias="acceptedPaymentMethod")
    actionable_feedback_policy: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="actionableFeedbackPolicy", serialization_alias="actionableFeedbackPolicy")
    address: PostalAddress_Text_Ref | list[PostalAddress_Text_Ref] | None = Field(default=None)
    agent_interaction_statistic: InteractionCounter_Ref | list[InteractionCounter_Ref] | None = Field(default=None, validation_alias="agentInteractionStatistic", serialization_alias="agentInteractionStatistic")
    aggregate_rating: AggregateRating_Ref | list[AggregateRating_Ref] | None = Field(default=None, validation_alias="aggregateRating", serialization_alias="aggregateRating")
    alumni: Person_Ref | list[Person_Ref] | None = Field(default=None)
    area_served: R3fcc4ec8 | list[R3fcc4ec8] | None = Field(default=None, validation_alias="areaServed", serialization_alias="areaServed")
    authorized_representative: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="authorizedRepresentative", serialization_alias="authorizedRepresentative")
    award: Text | list[Text] | None = Field(default=None)
    brand: Brand_Organization_Ref | list[Brand_Organization_Ref] | None = Field(default=None)
    company_registration: Certification_Ref | list[Certification_Ref] | None = Field(default=None, validation_alias="companyRegistration", serialization_alias="companyRegistration")
    contact_point: ContactPoint_Ref | list[ContactPoint_Ref] | None = Field(default=None, validation_alias="contactPoint", serialization_alias="contactPoint")
    corrections_policy: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="correctionsPolicy", serialization_alias="correctionsPolicy")
    department: Organization_Ref | list[Organization_Ref] | None = Field(default=None)
    dissolution_date: Date | list[Date] | None = Field(default=None, validation_alias="dissolutionDate", serialization_alias="dissolutionDate")
    diversity_policy: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="diversityPolicy", serialization_alias="diversityPolicy")
    diversity_staffing_report: Article_Url_Ref | list[Article_Url_Ref] | None = Field(default=None, validation_alias="diversityStaffingReport", serialization_alias="diversityStaffingReport")
    duns: Text | list[Text] | None = Field(default=None)
    email: Text | list[Text] | None = Field(default=None)
    employee: Person_Ref | list[Person_Ref] | None = Field(default=None)
    ethics_policy: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="ethicsPolicy", serialization_alias="ethicsPolicy")
    event: Event_Ref | list[Event_Ref] | None = Field(default=None)
    fax_number: Text | list[Text] | None = Field(default=None, validation_alias="faxNumber", serialization_alias="faxNumber")
    founder: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    founding_date: Date | list[Date] | None = Field(default=None, validation_alias="foundingDate", serialization_alias="foundingDate")
    founding_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="foundingLocation", serialization_alias="foundingLocation")
    funder: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    funding: Grant_Ref | list[Grant_Ref] | None = Field(default=None)
    global_location_number: Text | list[Text] | None = Field(default=None, validation_alias="globalLocationNumber", serialization_alias="globalLocationNumber")
    has_certification: Certification_Ref | list[Certification_Ref] | None = Field(default=None, validation_alias="hasCertification", serialization_alias="hasCertification")
    has_credential: Credential_Ref | list[Credential_Ref] | None = Field(default=None, validation_alias="hasCredential", serialization_alias="hasCredential")
    has_gs1_digital_link: Url | list[Url] | None = Field(default=None, validation_alias="hasGS1DigitalLink", serialization_alias="hasGS1DigitalLink")
    has_member_program: MemberProgram_Ref | list[MemberProgram_Ref] | None = Field(default=None, validation_alias="hasMemberProgram", serialization_alias="hasMemberProgram")
    has_merchant_return_policy: MerchantReturnPolicy_Ref | list[MerchantReturnPolicy_Ref] | None = Field(default=None, validation_alias="hasMerchantReturnPolicy", serialization_alias="hasMerchantReturnPolicy")
    has_offer_catalog: OfferCatalog_Ref | list[OfferCatalog_Ref] | None = Field(default=None, validation_alias="hasOfferCatalog", serialization_alias="hasOfferCatalog")
    has_pos: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="hasPOS", serialization_alias="hasPOS")
    has_shipping_service: ShippingService_Ref | list[ShippingService_Ref] | None = Field(default=None, validation_alias="hasShippingService", serialization_alias="hasShippingService")
    interaction_statistic: InteractionCounter_Ref | list[InteractionCounter_Ref] | None = Field(default=None, validation_alias="interactionStatistic", serialization_alias="interactionStatistic")
    isic_v4: Text | list[Text] | None = Field(default=None, validation_alias="isicV4", serialization_alias="isicV4")
    iso_6523_code: Text | list[Text] | None = Field(default=None, validation_alias="iso6523Code", serialization_alias="iso6523Code")
    keywords: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    knows_about: Thing_Text_Ref | list[Thing_Text_Ref] | None = Field(default=None, validation_alias="knowsAbout", serialization_alias="knowsAbout")
    knows_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="knowsLanguage", serialization_alias="knowsLanguage")
    legal_address: PostalAddress_Ref | list[PostalAddress_Ref] | None = Field(default=None, validation_alias="legalAddress", serialization_alias="legalAddress")
    legal_name: Text | list[Text] | None = Field(default=None, validation_alias="legalName", serialization_alias="legalName")
    legal_representative: Person_Ref | list[Person_Ref] | None = Field(default=None, validation_alias="legalRepresentative", serialization_alias="legalRepresentative")
    lei_code: Text | list[Text] | None = Field(default=None, validation_alias="leiCode", serialization_alias="leiCode")
    location: R2967d0a9 | list[R2967d0a9] | None = Field(default=None)
    logo: ImageObject_Url_Ref | list[ImageObject_Url_Ref] | None = Field(default=None)
    makes_offer: Offer_Ref | list[Offer_Ref] | None = Field(default=None, validation_alias="makesOffer", serialization_alias="makesOffer")
    member: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    member_of: MemberProgramTier_Organization_ProgramMembership_Ref | list[MemberProgramTier_Organization_ProgramMembership_Ref] | None = Field(default=None, validation_alias="memberOf", serialization_alias="memberOf")
    naics: Text | list[Text] | None = Field(default=None)
    nonprofit_status: Rd4d13d4d | list[Rd4d13d4d] | None = Field(default=None, validation_alias="nonprofitStatus", serialization_alias="nonprofitStatus")
    number_of_employees: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="numberOfEmployees", serialization_alias="numberOfEmployees")
    ownership_funding_info: AboutPage_CreativeWork_Text_Ref | list[AboutPage_CreativeWork_Text_Ref] | None = Field(default=None, validation_alias="ownershipFundingInfo", serialization_alias="ownershipFundingInfo")
    owns: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    parent_organization: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="parentOrganization", serialization_alias="parentOrganization")
    publishing_principles: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="publishingPrinciples", serialization_alias="publishingPrinciples")
    review: Review_Ref | list[Review_Ref] | None = Field(default=None)
    seeks: Demand_Ref | list[Demand_Ref] | None = Field(default=None)
    skills: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    slogan: Text | list[Text] | None = Field(default=None)
    sponsor: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    sub_organization: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="subOrganization", serialization_alias="subOrganization")
    tax_id: Text | list[Text] | None = Field(default=None, validation_alias="taxID", serialization_alias="taxID")
    telephone: Text | list[Text] | None = Field(default=None)
    unnamed_sources_policy: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="unnamedSourcesPolicy", serialization_alias="unnamedSourcesPolicy")
    vat_id: Text | list[Text] | None = Field(default=None, validation_alias="vatID", serialization_alias="vatID")
