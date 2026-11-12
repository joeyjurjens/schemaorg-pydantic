from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .rating import Rating


class EndorsementRating(Rating):
    """An EndorsementRating is a rating that expresses some level of endorsement, for example inclusion in a \"critic's pick\" blog, a\n\"Like\" or \"+1\" on a social network. It can be considered the [[result]] of an [[EndorseAction]] in which the [[object]] of the action is rated positively by\nsome [[agent]]. As is common elsewhere in schema.org, it is sometimes more useful to describe the results of such an action without explicitly describing the [[Action]]."""
    schema_type: ClassVar[str] = "EndorsementRating"
