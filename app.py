# app.py - main script that runs the student records demo application
# Perfective maintenance: formatted table output and richer statistics.

from students import (
    add_student,
    average_score,
    format_students_table,
    score_statistics,
    students,
)
from utils.helpers import highest_score, lowest_score

print("=" * 30)
print("   Student Records Demo")
print("=" * 30)
print(format_students_table(students))

add_student("Tunde", 74)
print("\nAdded new student: Tunde (74.0)\n")
print(format_students_table(students))

stats = score_statistics(students)
print("\nScore Statistics")
print("-" * 23)
print(f"Average : {stats['average']:>6.2f}")
print(f"Median  : {stats['median']:>6.2f}")
print(f"Minimum : {stats['min']:>6.2f}")
print(f"Maximum : {stats['max']:>6.2f}")

top = highest_score(students)
bottom = lowest_score(students)
print(f"\nTop scorer    : {top['name']} ({top['score']})")
print(f"Lowest scorer : {bottom['name']} ({bottom['score']})")
