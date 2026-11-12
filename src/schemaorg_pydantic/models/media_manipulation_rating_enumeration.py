from ..base import SchemaEnum


class MediaManipulationRatingEnumeration(SchemaEnum):
    DECONTEXTUALIZED_CONTENT = "https://schema.org/DecontextualizedContent"
    EDITED_OR_CROPPED_CONTENT = "https://schema.org/EditedOrCroppedContent"
    ORIGINAL_MEDIA_CONTENT = "https://schema.org/OriginalMediaContent"
    SATIRE_OR_PARODY_CONTENT = "https://schema.org/SatireOrParodyContent"
    STAGED_CONTENT = "https://schema.org/StagedContent"
    TRANSFORMED_CONTENT = "https://schema.org/TransformedContent"
