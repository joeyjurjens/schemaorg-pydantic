from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .educational_occupational_program import EducationalOccupationalProgram


class WorkBasedProgram(EducationalOccupationalProgram):
    """A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs."""
    schema_type: ClassVar[str] = "WorkBasedProgram"
