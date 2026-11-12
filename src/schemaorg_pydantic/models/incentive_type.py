from ..base import SchemaEnum


class IncentiveType(SchemaEnum):
    INCENTIVE_TYPE_LOAN = "https://schema.org/IncentiveTypeLoan"
    INCENTIVE_TYPE_REBATE_OR_SUBSIDY = "https://schema.org/IncentiveTypeRebateOrSubsidy"
    INCENTIVE_TYPE_TAX_CREDIT = "https://schema.org/IncentiveTypeTaxCredit"
    INCENTIVE_TYPE_TAX_DEDUCTION = "https://schema.org/IncentiveTypeTaxDeduction"
    INCENTIVE_TYPE_TAX_WAIVER = "https://schema.org/IncentiveTypeTaxWaiver"
