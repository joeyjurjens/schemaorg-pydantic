from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .audio_object import AudioObject


class AudioObjectSnapshot(AudioObject):
    """A specific and exact (byte-for-byte) version of an [[AudioObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity."""
    schema_type: ClassVar[str] = "AudioObjectSnapshot"
