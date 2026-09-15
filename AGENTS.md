# Agent guidelines

This document defines guidelines for automated development tools used in this repository.

## Scope

- keep changes small and focused
- modify only files related to the requested task
- avoid unrelated refactoring
- do not introduce unnecessary dependencies
- preserve the existing project structure unless the task requires otherwise

## Development process

Before making a change:

1. identify the problem and its likely cause
2. determine which files need to change
3. decide how the change will be verified

When implementing:

- prefer the smallest reasonable change
- keep diffs readable and focused
- follow the practices documented in `best_practices.md`
- update documentation when behavior changes

## Project technologies

The project uses:

- JavaScript for the frontend
- Python and FastAPI for the backend
- Pydantic v2 for data validation
- SQLAlchemy and SQLite for persistence
- pytest for backend testing

## Verification

Use the relevant project checks after making changes.

Available commands include:

- `scripts/run_backend.ps1`
- `scripts/run_tests.ps1`

The affected functionality should be verified before a change is considered complete.

## Version control

The branching model is documented in `README.md`.

Development work is performed outside `main`. Task-specific branches may be merged into `develop`, and reviewed changes are later merged from `develop` into `main`.

Commit messages should use a short descriptive format, for example:

`docs: update development guidelines`

## Responsibility

Automated tools may analyze code, suggest changes, and assist with reviews.

Suggestions are treated as development input rather than automatically accepted changes. The developer remains responsible for reviewing, understanding, and verifying the final implementation.


