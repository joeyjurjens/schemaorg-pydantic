from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .project import Project


class FundingAgency(Project):
    """A FundingAgency is an organization that implements one or more [[FundingScheme]]s and manages\n    the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s).\n    A funding agency is not always required for grant funding, e.g. philanthropic giving, corporate sponsorship etc.\n    \nExamples of funding agencies include ERC, REA, NIH, Bill and Melinda Gates Foundation, ..."""
    schema_type: ClassVar[str] = "FundingAgency"
