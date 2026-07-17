# Student Records Demo (SEN 401)

A small, modular Python project used for the SEN 401 Software Configuration
Management and Maintenance lab assessment. The application stores a list of
students, computes score statistics, and demonstrates a clean module layout
under version control.

## Project Structure

```
student-records/
├── app.py              # Main script — runs the demo application
├── students.py         # Data module — student records + score functions
├── utils/
│   ├── __init__.py
│   └── helpers.py      # Utility functions (highest/lowest score)
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── docs/               # Lab reports
```

## Modules

| File | Purpose |
|------|---------|
| `app.py` | Entry point. Prints the student list, average score, and highest/lowest scorers. |
| `students.py` | Holds the `students` list (each record has a `name` and `score`) plus `average_score()` and `add_student()`. |
| `utils/helpers.py` | `highest_score()` and `lowest_score()` helpers that scan the student list. |

## Usage

```bash
python3 app.py
```

No external dependencies are required for v1.0.

## Branching Model

- `main` — protected baseline; changes land via reviewed pull requests
- `dev` — integration branch
- `feature/*` — new feature work (e.g. `feature/statistics`)
- `maint/*` — maintenance work (e.g. `maint/bugfixes`)

## Releases

- **v1.0** — initial baseline (starter code)
