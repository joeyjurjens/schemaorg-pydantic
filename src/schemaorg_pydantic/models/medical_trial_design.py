from ..base import SchemaEnum


class MedicalTrialDesign(SchemaEnum):
    DOUBLE_BLINDED_TRIAL = "https://schema.org/DoubleBlindedTrial"
    INTERNATIONAL_TRIAL = "https://schema.org/InternationalTrial"
    MULTI_CENTER_TRIAL = "https://schema.org/MultiCenterTrial"
    OPEN_TRIAL = "https://schema.org/OpenTrial"
    PLACEBO_CONTROLLED_TRIAL = "https://schema.org/PlaceboControlledTrial"
    RANDOMIZED_TRIAL = "https://schema.org/RandomizedTrial"
    SINGLE_BLINDED_TRIAL = "https://schema.org/SingleBlindedTrial"
    SINGLE_CENTER_TRIAL = "https://schema.org/SingleCenterTrial"
    TRIPLE_BLINDED_TRIAL = "https://schema.org/TripleBlindedTrial"
