from ..base import SchemaEnum


class DENonprofitType(SchemaEnum):
    DE_COOPERATIVE_CHARITY = "https://schema.org/DECooperativeCharity"
    DE_FOUNDATION_CHARITY = "https://schema.org/DEFoundationCharity"
    DE_JOINT_STOCK_COMPANY_CHARITY = "https://schema.org/DEJointStockCompanyCharity"
    DE_LIMITED_LIABILITY_CHARITY = "https://schema.org/DELimitedLiabilityCharity"
    DE_NOT_REGISTERED_ASSOCIATION_CHARITY = "https://schema.org/DENotRegisteredAssociationCharity"
    DE_PUBLIC_CHARITY = "https://schema.org/DEPublicCharity"
    DE_REGISTERED_ASSOCIATION_CHARITY = "https://schema.org/DERegisteredAssociationCharity"
