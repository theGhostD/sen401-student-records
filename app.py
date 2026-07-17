"""Entry point for the student records demo application.

Preventive maintenance moved all demo logic into ``main()`` behind an
``if __name__ == "__main__"`` guard so importing this module never has
side effects.
"""

from students import (
    add_student,
    format_students_table,
    score_statistics,
    students,
)
from utils.helpers import highest_score, lowest_score


def main() -> None:
    """Run the demo: list students, add one, and print statistics."""
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


if __name__ == "__main__":
    main()
