from ..base import SchemaEnum


class GovernmentBenefitsType(SchemaEnum):
    BASIC_INCOME = "https://schema.org/BasicIncome"
    BUSINESS_SUPPORT = "https://schema.org/BusinessSupport"
    DISABILITY_SUPPORT = "https://schema.org/DisabilitySupport"
    HEALTH_CARE = "https://schema.org/HealthCare"
    ONE_TIME_PAYMENTS = "https://schema.org/OneTimePayments"
    PAID_LEAVE = "https://schema.org/PaidLeave"
    PARENTAL_SUPPORT = "https://schema.org/ParentalSupport"
    UNEMPLOYMENT_SUPPORT = "https://schema.org/UnemploymentSupport"
