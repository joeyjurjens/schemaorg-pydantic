from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Node


class DataType(Node):
    """The basic data types such as Integers, Strings, etc."""
    schema_type: ClassVar[str] = "DataType"
