from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .software_application import SoftwareApplication


class RuntimePlatform(SoftwareApplication):
    """Specialized software environment that provides the essential infrastructure, libraries, and services required to execute a program."""
    schema_type: ClassVar[str] = "RuntimePlatform"
