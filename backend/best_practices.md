# best practices

## learning mode
- explain the root cause in 1-3 sentences before proposing code.
- provide a minimal fix (small diff) and keep the current design.
- include a verification step for every change (how to run/check).
- if there are multiple valid fixes, list 2 options and recommend one.

## scope and safety
- do not change unrelated files.
- do not introduce new dependencies unless explicitly requested.
- avoid large refactors; prefer incremental improvements.

## language and style
- source code language: english only
- comments: lowercase only
- strings: english + lowercase only
- keep placeholders short and neutral (e.g., "app ready", "server not responding")

## javascript (frontend)
- keep modules small: app.js, ui.js, storage.js, api.js
- avoid hardcoding ui text inside logic; use constants when needed
- avoid global variables; keep state inside a single app module
- handle fetch errors explicitly (res.ok + network errors)

## python (backend)
- fastapi + pydantic v2
- for orm -> schema use: ConfigDict(from_attributes=True)
- separate request and response schemas (e.g., StudyCreate vs Study)
- keep database code in db.py and crud in crud.py
- return consistent error payloads (use error codes/keys)

## tests
- pytest is required for backend
- use fastapi TestClient
- no real network calls in tests
- prefer sqlite test db and isolated test data
