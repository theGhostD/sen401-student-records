# Lab 2 — Software Maintenance Tasks

**Course:** SEN 401 — Software Configuration Management and Maintenance
**Student:** Ojekale David Akinola — Matric No: 2024/B/SENG/0241
**Repository:** <https://github.com/theGhostD/sen401-student-records>

## 1. Introduction

This lab applies the four IEEE software-maintenance categories — corrective,
adaptive, perfective, and preventive — to the `students.py` data module from
the Lab 1 baseline (v1.0). `students.py` is the heart of the application: it
owns the student data set and every operation that reads or mutates it, so
each maintenance category has a visible, testable effect. All work was done
on a dedicated `maintenance` branch and released as **v1.1**.

## 2. Task Breakdown

| Maintenance type | What was done | Commit |
|------------------|---------------|--------|
| Corrective | Fixed `ZeroDivisionError` on empty student list; rejected invalid names/scores in `add_student()` | `1894be1` |
| Adaptive | Upgraded to Python 3.12 (modern type hints) and added Pydantic v2 validation | `4d5bf69` |
| Perfective | Aligned console table output; added median/min/max statistics | `6954280` |
| Preventive | Refactored for modularity; docstrings throughout; removed import side effects | `89a58bd` |

## 3. Step-by-Step Actions

### 3.1 Corrective Maintenance (Bug Fix)

**Bugs identified in v1.0:**
1. `average_score([])` crashed with `ZeroDivisionError` (division by `len(data)` with no guard).
2. `add_student()` accepted any input — empty names or scores like `-5` or `"abc"` silently corrupted the data set.

**Before:**
```python
def average_score(data):
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)

def add_student(name, score):
    students.append({"name": name, "score": score})
```

**After:**
```python
def average_score(data):
    if len(data) == 0:
        return 0  # Corrective maintenance: avoid ZeroDivisionError on empty list
    ...

def add_student(name, score):
    if not name or not isinstance(name, str):
        raise ValueError("Student name must be a non-empty string")
    if not isinstance(score, (int, float)) or not 0 <= score <= 100:
        raise ValueError("Score must be a number between 0 and 100")
    students.append({"name": name, "score": score})
```

> **[SCREENSHOT 2.1]** — IDE diff view of the corrective commit (`git show 1894be1`).

### 3.2 Adaptive Maintenance (Environment Update)

- Updated the code to target **Python 3.12**: modern PEP 604/585 type hints
  (`list[dict[str, str | float]]`) that require Python 3.10+.
- Added a new feature using **Pydantic v2**: a `Student` model that validates
  every record (`name` non-empty, `score` between 0 and 100) before it enters
  the data set. `requirements.txt` now declares `pydantic>=2.0`.

```python
class Student(BaseModel):
    name: str = Field(min_length=1)
    score: float = Field(ge=0, le=100)
```

Verification on Python 3.12:
```
$ .venv/bin/python -c "from students import add_student; add_student('', 150)"
ValueError: Invalid student record: 2 validation errors for Student ...
```

> **[SCREENSHOT 2.2]** — Terminal showing Python 3.12 in use and Pydantic rejecting an invalid record.

### 3.3 Perfective Maintenance (Enhancement)

- `format_students_table()` renders students as an aligned console table
  instead of raw dictionary dumps.
- `score_statistics()` computes **average, median, minimum, and maximum**
  using the standard-library `statistics` module.
- `app.py` output was reorganized into clearly labelled sections.

```
#   Name          Score
-----------------------
1   James          45.0
2   Deborah        82.0
...

Score Statistics
-----------------------
Average :  69.50
Median  :  70.50
```

> **[SCREENSHOT 2.3]** — Terminal showing the enhanced console output.

### 3.4 Preventive Maintenance (Refactoring)

- Module, class, and function **docstrings** added throughout.
- New `StudentRecord` type alias (PEP 695 `type` statement, Python 3.12)
  shared by all modules.
- Manual loops replaced with `statistics.mean`, `max(key=...)`, `min(key=...)`.
- Demo logic in `app.py` moved into `main()` behind an
  `if __name__ == "__main__"` guard, so importing the module has no side
  effects.
- Helpers now raise a clear `ValueError` on empty input instead of an
  accidental `IndexError`.

> **[SCREENSHOT 2.4]** — IDE showing the refactored `students.py` with docstrings.

## 4. Version Control

All changes were made on a dedicated branch with one descriptive commit per
maintenance category:

```bash
git checkout -b maintenance
# ... four commits ...
git push -u origin maintenance
gh pr create --base main   # merged after review
git tag -a v1.1 && git push --tags
gh release create v1.1
```

Commit history:

```
* 89a58bd Preventive maintenance: refactor for modularity and maintainability
* 6954280 Perfective maintenance: formatted table output and extra statistics
* 4d5bf69 Adaptive maintenance: Python 3.12 compatibility and Pydantic validation
* 1894be1 Corrective maintenance: fix empty-list crash and invalid input bugs
* b50e17d (tag: v1.0) Initial commit: starter student records project (baseline v1.0)
```

> **[SCREENSHOT 2.5]** — GitHub network graph / commit list of the `maintenance` branch.
> **[SCREENSHOT 2.6]** — Merged pull request from `maintenance` into `main`.
> **[SCREENSHOT 2.7]** — Releases page showing v1.1.

## 5. Results & Observations

- All four maintenance categories were applied and verified by running the
  application after each commit — the app never regressed.
- The empty-list bug demonstrated why corrective fixes should come first:
  later statistics features reuse the same guard.
- Pydantic moved validation out of hand-written `if` checks into a declarative
  model, which is easier to extend (adaptive change enabling future features).
- **Challenge:** GitHub's Free plan does not enforce branch protection on
  private repositories; the repository was made public so the
  require-PR-review rule is active.

## 6. Conclusion

Version control made each maintenance category auditable: one branch, one
commit per category, one tagged release. The lab demonstrates that
maintenance is not just bug fixing — most of the value came from adaptive
(new validation capability) and preventive (readability, modularity) work
that reduces the cost of every future change.
