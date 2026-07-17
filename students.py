# students.py - data module for the student records demo app
# Adaptive maintenance: updated for Python 3.12 (modern type hints) and
# Pydantic v2 is now used for data validation of student records.

import statistics

from pydantic import BaseModel, Field, ValidationError


class Student(BaseModel):
    """A validated student record (adaptive maintenance: Pydantic v2)."""

    name: str = Field(min_length=1)
    score: float = Field(ge=0, le=100)


students: list[dict[str, str | float]] = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Amina", "score": 67},
    {"name": "Chinedu", "score": 91},
    {"name": "Fatima", "score": 58},
]


def average_score(data: list[dict[str, str | float]]) -> float:
    if len(data) == 0:
        return 0  # Corrective maintenance: avoid ZeroDivisionError on empty list
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def score_statistics(data: list[dict[str, str | float]]) -> dict[str, float]:
    # Perfective maintenance: richer statistics via the stdlib statistics module
    if len(data) == 0:
        return {"average": 0, "median": 0, "min": 0, "max": 0}
    scores = [d["score"] for d in data]
    return {
        "average": statistics.mean(scores),
        "median": statistics.median(scores),
        "min": min(scores),
        "max": max(scores),
    }


def format_students_table(data: list[dict[str, str | float]]) -> str:
    # Perfective maintenance: human-readable table instead of raw dict dumps
    if len(data) == 0:
        return "(no students recorded)"
    lines = [f"{'#':<3} {'Name':<12} {'Score':>6}", "-" * 23]
    for i, d in enumerate(data, start=1):
        lines.append(f"{i:<3} {d['name']:<12} {d['score']:>6.1f}")
    return "\n".join(lines)


def add_student(name: str, score: float) -> None:
    # Adaptive maintenance: validation now delegated to the Pydantic model
    try:
        student = Student(name=name, score=score)
    except ValidationError as exc:
        raise ValueError(f"Invalid student record: {exc}") from exc
    students.append(student.model_dump())
