"""Utility helpers for the student records demo application.

Kept separate from the data module so that generic lookups can be reused
by any caller without importing the mutable data set itself.
"""

from students import StudentRecord


def highest_score(data: list[StudentRecord]) -> StudentRecord:
    """Return the record with the highest score.

    Raises:
        ValueError: if ``data`` is empty.
    """
    if not data:
        raise ValueError("Cannot find highest score of an empty list")
    return max(data, key=lambda d: d["score"])


def lowest_score(data: list[StudentRecord]) -> StudentRecord:
    """Return the record with the lowest score.

    Raises:
        ValueError: if ``data`` is empty.
    """
    if not data:
        raise ValueError("Cannot find lowest score of an empty list")
    return min(data, key=lambda d: d["score"])
