from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .web_content import WebContent
from .health_aspect_enumeration import HealthAspectEnumeration


class HealthTopicContent(WebContent):
    """[[HealthTopicContent]] is [[WebContent]] that is about some aspect of a health topic, e.g. a condition, its symptoms or treatments. Such content may be comprised of several parts or sections and use different types of media. Multiple instances of [[WebContent]] (and hence [[HealthTopicContent]]) can be related using [[hasPart]] / [[isPartOf]] where there is some kind of content hierarchy, and their content described with [[about]] and [[mentions]] e.g. building upon the existing [[MedicalCondition]] vocabulary."""
    schema_type: ClassVar[str] = "HealthTopicContent"
    has_health_aspect: HealthAspectEnumeration | list[HealthAspectEnumeration] | None = Field(default=None, validation_alias="hasHealthAspect", serialization_alias="hasHealthAspect")
