# students.py - data module for the student records demo app

students = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Amina", "score": 67},
    {"name": "Chinedu", "score": 91},
    {"name": "Fatima", "score": 58},
]


def average_score(data):
    if len(data) == 0:
        return 0  # Corrective maintenance: avoid ZeroDivisionError on empty list
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def add_student(name, score):
    # Corrective maintenance: reject invalid input instead of storing bad data
    if not name or not isinstance(name, str):
        raise ValueError("Student name must be a non-empty string")
    if not isinstance(score, (int, float)) or not 0 <= score <= 100:
        raise ValueError("Score must be a number between 0 and 100")
    students.append({"name": name, "score": score})
