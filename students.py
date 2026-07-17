# students.py - data module for the student records demo app
# Adaptive maintenance: updated for Python 3.12 (modern type hints) and
# Pydantic v2 is now used for data validation of student records.

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


def add_student(name: str, score: float) -> None:
    # Adaptive maintenance: validation now delegated to the Pydantic model
    try:
        student = Student(name=name, score=score)
    except ValidationError as exc:
        raise ValueError(f"Invalid student record: {exc}") from exc
    students.append(student.model_dump())
