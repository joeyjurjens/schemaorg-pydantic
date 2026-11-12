from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .image_object import ImageObject


class Barcode(ImageObject):
    """An image of a visual machine-readable code such as a barcode or QR code."""
    schema_type: ClassVar[str] = "Barcode"
