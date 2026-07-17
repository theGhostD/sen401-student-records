# students.py - data module for the student records demo app

students = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Amina", "score": 67},
    {"name": "Chinedu", "score": 91},
    {"name": "Fatima", "score": 58},
]


def average_score(data):
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def add_student(name, score):
    students.append({"name": name, "score": score})
