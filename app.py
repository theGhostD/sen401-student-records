# app.py - main script that runs the student records demo application

from students import students, average_score, add_student
from utils.helpers import highest_score, lowest_score

print("=== Student Records Demo ===")
print("Current Students:", students)
print("Average Score:", average_score(students))

add_student("Tunde", 74)
print("After adding Tunde:", students)

top = highest_score(students)
bottom = lowest_score(students)
print("Highest:", top["name"], "with", top["score"])
print("Lowest:", bottom["name"], "with", bottom["score"])
