from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Url
from .service import Service

if TYPE_CHECKING:
    from .creative_work import CreativeWork

if TYPE_CHECKING:
    CreativeWork_Url_Ref = Union[CreativeWork, Url, Ref]
else:
    CreativeWork_Url_Ref = Union[Is["CreativeWork"], Url, Ref]


class WebAPI(Service):
    """An application programming interface accessible over Web/Internet technologies."""
    schema_type: ClassVar[str] = "WebAPI"
    documentation: CreativeWork_Url_Ref | list[CreativeWork_Url_Ref] | None = Field(default=None)
