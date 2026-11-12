from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .article import Article


class NewsArticle(Article):
    """A NewsArticle is an article whose content reports news, or provides background context and supporting materials for understanding the news."""
    schema_type: ClassVar[str] = "NewsArticle"
    dateline: Text | list[Text] | None = Field(default=None)
    print_column: Text | list[Text] | None = Field(default=None, validation_alias="printColumn", serialization_alias="printColumn")
    print_edition: Text | list[Text] | None = Field(default=None, validation_alias="printEdition", serialization_alias="printEdition")
    print_page: Text | list[Text] | None = Field(default=None, validation_alias="printPage", serialization_alias="printPage")
    print_section: Text | list[Text] | None = Field(default=None, validation_alias="printSection", serialization_alias="printSection")
