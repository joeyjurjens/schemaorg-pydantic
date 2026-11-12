from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .bio_chem_entity import BioChemEntity


class Protein(BioChemEntity):
    """Protein is here used in its widest possible definition, as classes of amino acid based molecules. Amyloid-beta Protein in human (UniProt P05067), eukaryota (e.g. an OrthoDB group) or even a single molecule that one can point to are all of type :Protein. A protein can thus be a subclass of another protein, e.g. :Protein as a UniProt record can have multiple isoforms inside it which would also be :Protein. They can be imagined, synthetic, hypothetical or naturally occurring."""
    schema_type: ClassVar[str] = "Protein"
    has_bio_polymer_sequence: Text | list[Text] | None = Field(default=None, validation_alias="hasBioPolymerSequence", serialization_alias="hasBioPolymerSequence")
