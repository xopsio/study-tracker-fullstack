# best practices

this document defines mandatory development practices for this repository.
it applies to human contributors and all ai agents.

---

## learning mode (must follow)

- explain the root cause in 1–3 sentences before proposing any code.
- propose a minimal fix with a small, focused diff.
- keep the existing design unless a change is explicitly requested.
- include a clear verification step for every change (how to run/check).
- if there are multiple valid solutions, list two options and recommend one with a reason.

---

## scope and safety

- do not change unrelated files.
- do not introduce new dependencies unless explicitly requested.
- avoid large refactors; prefer incremental, verifiable improvements.
- modify only the files required to resolve the issue.

---

## language and style (strict)

- source code language: english only
- comments: lowercase only
- strings: english + lowercase only
- keep messages short and neutral (e.g., "app ready", "server not responding")
- do not add finnish strings to source code

---

## javascript (frontend)

- keep modules small and focused:
  - app.js
  - ui.js
  - storage.js
  - api.js
- avoid global variables; keep state inside a single app module.
- do not hardcode ui text inside logic; use constants when needed.
- handle fetch errors explicitly:
  - check res.ok
  - handle network and parsing errors

---

## python (backend)

- framework: fastapi
- data validation: pydantic v2

- orm to schema:
  - use ConfigDict(from_attributes=True)
  - do not use orm_mode

- separate schemas:
  - request schemas (e.g., StudyCreate)
  - response schemas (e.g., Study)

- keep responsibilities separated:
  - database setup and sessions: db.py
  - data access logic: crud.py

- return consistent error payloads:
  - stable error keys
  - predictable structure

---

## tests (backend)

- pytest is required
- use fastapi TestClient
- no real network calls in tests
- prefer sqlite for tests with isolated test data
- tests must be deterministic and repeatable

---

## verification minimum (required)

after any change, run at least one relevant command:

- backend:
  - scripts/run_backend.ps1
- tests:
  - scripts/run_tests.ps1

do not consider a change complete without verification.

---

## change discipline

- keep diffs small and readable
- prefer clarity over cleverness
- learning and understanding are more important than speed

