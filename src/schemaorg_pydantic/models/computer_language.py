from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .intangible import Intangible


class ComputerLanguage(Intangible):
    """This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type."""
    schema_type: ClassVar[str] = "ComputerLanguage"
