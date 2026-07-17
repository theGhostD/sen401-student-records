# Lab 1 — SCM Setup & Baseline Creation

**Course:** SEN 401 — Software Configuration Management and Maintenance
**Student:** `[YOUR FULL NAME]` — Matric No: `[YOUR MATRIC NUMBER]`
**Repository:** `[GITHUB REPO URL]`

## 1. Objective

Establish a fully functional Software Configuration Management (SCM)
environment: a modular Python project under Git version control, hosted on
GitHub with a branching workflow, branch protection, and a tagged v1.0
baseline release.

## 2. Project Design

The starter application is a modular Python project that manages student
records and score statistics.

| File | Description |
|------|-------------|
| `app.py` | Main script. Runs the demo: prints the student list, average score, and the highest/lowest scorers. |
| `students.py` | Data module. Holds the `students` list (records with `name` and `score`) plus `average_score()` and `add_student()`. |
| `utils/helpers.py` | Helper module. `highest_score()` and `lowest_score()` utility functions. |
| `requirements.txt` | Python dependencies (none required at v1.0 — standard library only). |
| `README.md` | Project structure, usage instructions, and branching model. |
| `.gitignore` | Excludes `__pycache__/`, virtual environments, and OS artifacts from version control. |

> **[SCREENSHOT 1.1]** — VS Code Explorer showing the project file structure.

## 3. GitHub Repository Creation

Steps taken:

1. Created the repository on GitHub (initially **Private**) using the GitHub CLI:
   ```bash
   gh repo create sen401-student-records --private --source . --push
   ```
2. Repository visibility was later switched to **Public** for submission, since
   GitHub branch protection rules require a public repository on the Free plan.

> **[SCREENSHOT 1.2]** — GitHub repository main page showing the repo name and visibility badge.

## 4. Branch & Workflow Setup

Branches created to model a real-world workflow:

| Branch | Purpose |
|--------|---------|
| `main` | Protected baseline. Changes land only through reviewed pull requests. |
| `dev` | Integration branch for ongoing development. |
| `feature/statistics` | Example feature branch (`feature/*` namespace). |
| `maint/bugfixes` | Example maintenance branch (`maint/*` namespace). |

Commands used:

```bash
git init -b main
git branch dev
git branch feature/statistics
git branch maint/bugfixes
```

Branch protection was enabled on `main` requiring at least one pull-request
review before merging.

> **[SCREENSHOT 1.3]** — GitHub branch list (Code → Branches) showing all four branches.
> **[SCREENSHOT 1.4]** — Settings → Branches showing the protection rule on `main` (require pull request reviews).

## 5. Baseline v1.0

The starter code was committed and pushed, then tagged as the first baseline:

```bash
git add -A
git commit -m "Initial commit: starter student records project (baseline v1.0)"
git tag -a v1.0 -m "Baseline v1.0: initial starter code for SEN 401 Lab 1"
git push --all && git push --tags
gh release create v1.0 --title "v1.0 — Initial Baseline" --notes-file <release notes>
```

Commit history at baseline:

```
b50e17d (tag: v1.0, main, dev, feature/statistics, maint/bugfixes)
        Initial commit: starter student records project (baseline v1.0)
```

> **[SCREENSHOT 1.5]** — GitHub commit history page.
> **[SCREENSHOT 1.6]** — GitHub Releases page showing the v1.0 release with notes.

## 6. Application Output at v1.0

```
=== Student Records Demo ===
Current Students: [{'name': 'James', 'score': 45}, {'name': 'Deborah', 'score': 82}, ...]
Average Score: 68.6
After adding Tunde: [... {'name': 'Tunde', 'score': 74}]
Highest: Chinedu with 91
Lowest: James with 45
```

> **[SCREENSHOT 1.7]** — Terminal showing `python3 app.py` output.

## 7. Summary

A complete SCM environment was established: a modular Python project under
Git, a GitHub repository with a four-tier branching model, branch protection
enforcing peer review on `main`, and a tagged, released v1.0 baseline that
all subsequent maintenance work (Lab 2) builds upon.
