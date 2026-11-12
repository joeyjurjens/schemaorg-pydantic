from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, Is, Ref, Text, Url
from .thing import Thing
from .gender_type import GenderType

if TYPE_CHECKING:
    from .brand import Brand
    from .certification import Certification
    from .contact_point import ContactPoint
    from .country import Country
    from .creative_work import CreativeWork
    from .credential import Credential
    from .defined_term import DefinedTerm
    from .demand import Demand
    from .educational_organization import EducationalOrganization
    from .event import Event
    from .grant import Grant
    from .interaction_counter import InteractionCounter
    from .language import Language
    from .member_program_tier import MemberProgramTier
    from .monetary_amount import MonetaryAmount
    from .occupation import Occupation
    from .offer import Offer
    from .offer_catalog import OfferCatalog
    from .organization import Organization
    from .place import Place
    from .postal_address import PostalAddress
    from .price_specification import PriceSpecification
    from .program_membership import ProgramMembership
    from .quantitative_value import QuantitativeValue
    from .structured_value import StructuredValue

if TYPE_CHECKING:
    Brand_Organization_Ref = Union[Brand, Organization, Ref]
else:
    Brand_Organization_Ref = Union[Is["Brand"], Is["Organization"], Ref]

if TYPE_CHECKING:
    Certification_Ref = Union[Certification, Ref]
else:
    Certification_Ref = Union[Is["Certification"], Ref]

if TYPE_CHECKING:
    ContactPoint_Place_Ref = Union[ContactPoint, Place, Ref]
else:
    ContactPoint_Place_Ref = Union[Is["ContactPoint"], Is["Place"], Ref]

if TYPE_CHECKING:
    ContactPoint_Ref = Union[ContactPoint, Ref]
else:
    ContactPoint_Ref = Union[Is["ContactPoint"], Ref]

if TYPE_CHECKING:
    Country_Ref = Union[Country, Ref]
else:
    Country_Ref = Union[Is["Country"], Ref]

if TYPE_CHECKING:
    CreativeWork_Url_Ref = Union[CreativeWork, Url, Ref]
else:
    CreativeWork_Url_Ref = Union[Is["CreativeWork"], Url, Ref]

if TYPE_CHECKING:
    Credential_Ref = Union[Credential, Ref]
else:
    Credential_Ref = Union[Is["Credential"], Ref]

if TYPE_CHECKING:
    DefinedTerm_StructuredValue_Text_Ref = Union[DefinedTerm, StructuredValue, Text, Ref]
else:
    DefinedTerm_StructuredValue_Text_Ref = Union[Is["DefinedTerm"], Is["StructuredValue"], Text, Ref]

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    Demand_Ref = Union[Demand, Ref]
else:
    Demand_Ref = Union[Is["Demand"], Ref]

if TYPE_CHECKING:
    EducationalOrganization_Organization_Ref = Union[EducationalOrganization, Organization, Ref]
else:
    EducationalOrganization_Organization_Ref = Union[Is["EducationalOrganization"], Is["Organization"], Ref]

if TYPE_CHECKING:
    Event_Ref = Union[Event, Ref]
else:
    Event_Ref = Union[Is["Event"], Ref]

GenderType_Text = Union[GenderType, Text]
if TYPE_CHECKING:
    Grant_Ref = Union[Grant, Ref]
else:
    Grant_Ref = Union[Is["Grant"], Ref]

if TYPE_CHECKING:
    InteractionCounter_Ref = Union[InteractionCounter, Ref]
else:
    InteractionCounter_Ref = Union[Is["InteractionCounter"], Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    MemberProgramTier_Organization_ProgramMembership_Ref = Union[MemberProgramTier, Organization, ProgramMembership, Ref]
else:
    MemberProgramTier_Organization_ProgramMembership_Ref = Union[Is["MemberProgramTier"], Is["Organization"], Is["ProgramMembership"], Ref]

if TYPE_CHECKING:
    MonetaryAmount_PriceSpecification_Ref = Union[MonetaryAmount, PriceSpecification, Ref]
else:
    MonetaryAmount_PriceSpecification_Ref = Union[Is["MonetaryAmount"], Is["PriceSpecification"], Ref]

if TYPE_CHECKING:
    Occupation_Ref = Union[Occupation, Ref]
else:
    Occupation_Ref = Union[Is["Occupation"], Ref]

if TYPE_CHECKING:
    Offer_Ref = Union[Offer, Ref]
else:
    Offer_Ref = Union[Is["Offer"], Ref]

if TYPE_CHECKING:
    OfferCatalog_Ref = Union[OfferCatalog, Ref]
else:
    OfferCatalog_Ref = Union[Is["OfferCatalog"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, "Person", Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    Person_Ref = Union["Person", Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

if TYPE_CHECKING:
    Person_Url_Ref = Union["Person", Url, Ref]
else:
    Person_Url_Ref = Union[Is["Person"], Url, Ref]

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    PostalAddress_Text_Ref = Union[PostalAddress, Text, Ref]
else:
    PostalAddress_Text_Ref = Union[Is["PostalAddress"], Text, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]

if TYPE_CHECKING:
    Thing_Text_Ref = Union[Thing, Text, Ref]
else:
    Thing_Text_Ref = Union[Is["Thing"], Text, Ref]


class Person(Thing):
    """A person (alive, dead, undead, or fictional)."""
    schema_type: ClassVar[str] = "Person"
    additional_name: Text | list[Text] | None = Field(default=None, validation_alias="additionalName", serialization_alias="additionalName")
    address: PostalAddress_Text_Ref | list[PostalAddress_Text_Ref] | None = Field(default=None)
    affiliation: Organization_Ref | list[Organization_Ref] | None = Field(default=None)
    agent_interaction_statistic: InteractionCounter_Ref | list[InteractionCounter_Ref] | None = Field(default=None, validation_alias="agentInteractionStatistic", serialization_alias="agentInteractionStatistic")
    alumni_of: EducationalOrganization_Organization_Ref | list[EducationalOrganization_Organization_Ref] | None = Field(default=None, validation_alias="alumniOf", serialization_alias="alumniOf")
    award: Text | list[Text] | None = Field(default=None)
    birth_date: Date | list[Date] | None = Field(default=None, validation_alias="birthDate", serialization_alias="birthDate")
    birth_place: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="birthPlace", serialization_alias="birthPlace")
    brand: Brand_Organization_Ref | list[Brand_Organization_Ref] | None = Field(default=None)
    call_sign: Text | list[Text] | None = Field(default=None, validation_alias="callSign", serialization_alias="callSign")
    children: Person_Ref | list[Person_Ref] | None = Field(default=None)
    colleague: Person_Url_Ref | list[Person_Url_Ref] | None = Field(default=None)
    contact_point: ContactPoint_Ref | list[ContactPoint_Ref] | None = Field(default=None, validation_alias="contactPoint", serialization_alias="contactPoint")
    death_date: Date | list[Date] | None = Field(default=None, validation_alias="deathDate", serialization_alias="deathDate")
    death_place: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="deathPlace", serialization_alias="deathPlace")
    duns: Text | list[Text] | None = Field(default=None)
    email: Text | list[Text] | None = Field(default=None)
    family_name: Text | list[Text] | None = Field(default=None, validation_alias="familyName", serialization_alias="familyName")
    fax_number: Text | list[Text] | None = Field(default=None, validation_alias="faxNumber", serialization_alias="faxNumber")
    follows: Person_Ref | list[Person_Ref] | None = Field(default=None)
    funder: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    funding: Grant_Ref | list[Grant_Ref] | None = Field(default=None)
    gender: GenderType_Text | list[GenderType_Text] | None = Field(default=None)
    given_name: Text | list[Text] | None = Field(default=None, validation_alias="givenName", serialization_alias="givenName")
    global_location_number: Text | list[Text] | None = Field(default=None, validation_alias="globalLocationNumber", serialization_alias="globalLocationNumber")
    has_certification: Certification_Ref | list[Certification_Ref] | None = Field(default=None, validation_alias="hasCertification", serialization_alias="hasCertification")
    has_credential: Credential_Ref | list[Credential_Ref] | None = Field(default=None, validation_alias="hasCredential", serialization_alias="hasCredential")
    has_occupation: Occupation_Ref | list[Occupation_Ref] | None = Field(default=None, validation_alias="hasOccupation", serialization_alias="hasOccupation")
    has_offer_catalog: OfferCatalog_Ref | list[OfferCatalog_Ref] | None = Field(default=None, validation_alias="hasOfferCatalog", serialization_alias="hasOfferCatalog")
    has_pos: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="hasPOS", serialization_alias="hasPOS")
    height: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    home_location: ContactPoint_Place_Ref | list[ContactPoint_Place_Ref] | None = Field(default=None, validation_alias="homeLocation", serialization_alias="homeLocation")
    honorific_prefix: Text | list[Text] | None = Field(default=None, validation_alias="honorificPrefix", serialization_alias="honorificPrefix")
    honorific_suffix: Text | list[Text] | None = Field(default=None, validation_alias="honorificSuffix", serialization_alias="honorificSuffix")
    interaction_statistic: InteractionCounter_Ref | list[InteractionCounter_Ref] | None = Field(default=None, validation_alias="interactionStatistic", serialization_alias="interactionStatistic")
    isic_v4: Text | list[Text] | None = Field(default=None, validation_alias="isicV4", serialization_alias="isicV4")
    job_title: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None, validation_alias="jobTitle", serialization_alias="jobTitle")
    knows: Person_Ref | list[Person_Ref] | None = Field(default=None)
    knows_about: Thing_Text_Ref | list[Thing_Text_Ref] | None = Field(default=None, validation_alias="knowsAbout", serialization_alias="knowsAbout")
    knows_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="knowsLanguage", serialization_alias="knowsLanguage")
    life_event: Event_Ref | list[Event_Ref] | None = Field(default=None, validation_alias="lifeEvent", serialization_alias="lifeEvent")
    makes_offer: Offer_Ref | list[Offer_Ref] | None = Field(default=None, validation_alias="makesOffer", serialization_alias="makesOffer")
    member_of: MemberProgramTier_Organization_ProgramMembership_Ref | list[MemberProgramTier_Organization_ProgramMembership_Ref] | None = Field(default=None, validation_alias="memberOf", serialization_alias="memberOf")
    naics: Text | list[Text] | None = Field(default=None)
    nationality: Country_Ref | list[Country_Ref] | None = Field(default=None)
    net_worth: MonetaryAmount_PriceSpecification_Ref | list[MonetaryAmount_PriceSpecification_Ref] | None = Field(default=None, validation_alias="netWorth", serialization_alias="netWorth")
    owns: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    parent: Person_Ref | list[Person_Ref] | None = Field(default=None)
    performer_in: Event_Ref | list[Event_Ref] | None = Field(default=None, validation_alias="performerIn", serialization_alias="performerIn")
    pronouns: DefinedTerm_StructuredValue_Text_Ref | list[DefinedTerm_StructuredValue_Text_Ref] | None = Field(default=None)
    publishing_principles: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None, validation_alias="publishingPrinciples", serialization_alias="publishingPrinciples")
    related_to: Person_Ref | list[Person_Ref] | None = Field(default=None, validation_alias="relatedTo", serialization_alias="relatedTo")
    seeks: Demand_Ref | list[Demand_Ref] | None = Field(default=None)
    sibling: Person_Ref | list[Person_Ref] | None = Field(default=None)
    skills: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    sponsor: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    spouse: Person_Ref | list[Person_Ref] | None = Field(default=None)
    tax_id: Text | list[Text] | None = Field(default=None, validation_alias="taxID", serialization_alias="taxID")
    telephone: Text | list[Text] | None = Field(default=None)
    vat_id: Text | list[Text] | None = Field(default=None, validation_alias="vatID", serialization_alias="vatID")
    weight: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    work_location: ContactPoint_Place_Ref | list[ContactPoint_Place_Ref] | None = Field(default=None, validation_alias="workLocation", serialization_alias="workLocation")
    works_for: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="worksFor", serialization_alias="worksFor")
