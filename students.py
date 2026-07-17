"""Data module for the student records demo application.

This module owns the in-memory student data set and every operation that
reads or mutates it. It was refactored during preventive maintenance to
improve modularity: a shared ``StudentRecord`` type alias, one public
function per responsibility, and docstrings throughout.

Requires Python 3.12+ and Pydantic v2 (see requirements.txt).
"""

import statistics

from pydantic import BaseModel, Field, ValidationError

# A single student entry as stored in the data set.
type StudentRecord = dict[str, str | float]


class Student(BaseModel):
    """A validated student record.

    Pydantic v2 enforces that ``name`` is a non-empty string and that
    ``score`` falls within the 0-100 grading range.
    """

    name: str = Field(min_length=1)
    score: float = Field(ge=0, le=100)


#: The demo data set. Mutated only through :func:`add_student`.
students: list[StudentRecord] = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Amina", "score": 67},
    {"name": "Chinedu", "score": 91},
    {"name": "Fatima", "score": 58},
]


def average_score(data: list[StudentRecord]) -> float:
    """Return the mean score of ``data``, or 0 for an empty list.

    Returning 0 (rather than raising ``ZeroDivisionError``) was the
    corrective-maintenance fix applied in v1.1.
    """
    if not data:
        return 0.0
    return statistics.mean(d["score"] for d in data)


def score_statistics(data: list[StudentRecord]) -> dict[str, float]:
    """Return average, median, min and max scores for ``data``.

    All values are 0 when the list is empty so callers never need to
    special-case an empty data set.
    """
    if not data:
        return {"average": 0.0, "median": 0.0, "min": 0.0, "max": 0.0}
    scores = [d["score"] for d in data]
    return {
        "average": statistics.mean(scores),
        "median": statistics.median(scores),
        "min": min(scores),
        "max": max(scores),
    }


def format_students_table(data: list[StudentRecord]) -> str:
    """Render ``data`` as an aligned, human-readable console table."""
    if not data:
        return "(no students recorded)"
    lines = [f"{'#':<3} {'Name':<12} {'Score':>6}", "-" * 23]
    for i, d in enumerate(data, start=1):
        lines.append(f"{i:<3} {d['name']:<12} {d['score']:>6.1f}")
    return "\n".join(lines)


def add_student(name: str, score: float) -> None:
    """Validate and append a new student to the data set.

    Raises:
        ValueError: if the record fails :class:`Student` validation.
    """
    try:
        student = Student(name=name, score=score)
    except ValidationError as exc:
        raise ValueError(f"Invalid student record: {exc}") from exc
    students.append(student.model_dump())
