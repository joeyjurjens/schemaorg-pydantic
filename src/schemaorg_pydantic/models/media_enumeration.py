from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class MediaEnumeration(Enumeration):
    """MediaEnumeration enumerations are lists of codes, labels etc. useful for describing media objects. They may be reflections of externally developed lists, or created at schema.org, or a combination."""
    schema_type: ClassVar[str] = "MediaEnumeration"
