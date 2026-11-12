from ..base import SchemaEnum


class PhysicalActivityCategory(SchemaEnum):
    AEROBIC_ACTIVITY = "https://schema.org/AerobicActivity"
    ANAEROBIC_ACTIVITY = "https://schema.org/AnaerobicActivity"
    BALANCE = "https://schema.org/Balance"
    FLEXIBILITY = "https://schema.org/Flexibility"
    LEISURE_TIME_ACTIVITY = "https://schema.org/LeisureTimeActivity"
    OCCUPATIONAL_ACTIVITY = "https://schema.org/OccupationalActivity"
    STRENGTH_TRAINING = "https://schema.org/StrengthTraining"
