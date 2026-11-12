from ..base import SchemaEnum


class MedicalObservationalStudyDesign(SchemaEnum):
    CASE_SERIES = "https://schema.org/CaseSeries"
    COHORT_STUDY = "https://schema.org/CohortStudy"
    CROSS_SECTIONAL = "https://schema.org/CrossSectional"
    LONGITUDINAL = "https://schema.org/Longitudinal"
    OBSERVATIONAL = "https://schema.org/Observational"
    REGISTRY = "https://schema.org/Registry"
