from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work_series import CreativeWorkSeries


class Periodical(CreativeWorkSeries):
    """A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper."""
    schema_type: ClassVar[str] = "Periodical"
