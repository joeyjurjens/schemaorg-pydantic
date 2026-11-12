from ..base import SchemaEnum


class UKNonprofitType(SchemaEnum):
    CHARITABLE_INCORPORATED_ORGANIZATION = "https://schema.org/CharitableIncorporatedOrganization"
    LIMITED_BY_GUARANTEE_CHARITY = "https://schema.org/LimitedByGuaranteeCharity"
    UK_TRUST = "https://schema.org/UKTrust"
    UNINCORPORATED_ASSOCIATION_CHARITY = "https://schema.org/UnincorporatedAssociationCharity"
