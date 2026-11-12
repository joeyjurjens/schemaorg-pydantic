from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .place import Place


class Landform(Place):
    """A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins."""
    schema_type: ClassVar[str] = "Landform"
