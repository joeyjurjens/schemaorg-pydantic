from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Boolean
from .media_object import MediaObject


class ThreeDModel(MediaObject):
    """A 3D model represents some kind of 3D content, which may have [[encoding]]s in one or more [[MediaObject]]s. Many 3D formats are available (e.g. see [Wikipedia](https://en.wikipedia.org/wiki/Category:3D_graphics_file_formats)); specific encoding formats can be represented using the [[encodingFormat]] property applied to the relevant [[MediaObject]]. For the\ncase of a single file published after Zip compression, the convention of appending '+zip' to the [[encodingFormat]] can be used. Geospatial, AR/VR, artistic/animation, gaming, engineering and scientific content can all be represented using [[3DModel]]."""
    schema_type: ClassVar[str] = "3DModel"
    is_resizable: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isResizable", serialization_alias="isResizable")
