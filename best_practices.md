# Development practices

This document describes the development practices used in this repository.

## General principles

- keep changes small and focused
- avoid unrelated changes
- prefer clear and maintainable solutions
- avoid unnecessary dependencies
- verify changes before merging them
- update documentation when behavior changes

## JavaScript

Frontend code is organized into small modules:

- `app.js`
- `ui.js`
- `storage.js`
- `api.js`

Guidelines:

- avoid unnecessary global variables
- keep modules focused on a clear responsibility
- handle failed HTTP requests and network errors explicitly
- keep user interface logic separate from data access where practical

## Python

The backend uses:

- FastAPI
- Pydantic v2
- SQLAlchemy
- SQLite

Guidelines:

- use `ConfigDict(from_attributes=True)` with Pydantic v2 when converting ORM objects
- keep database setup separate from data access logic
- use separate request and response schemas when appropriate
- keep error responses consistent

## Testing

Backend tests use:

- pytest
- FastAPI TestClient

Tests should:

- be deterministic and repeatable
- avoid real network requests unless explicitly required
- use isolated test data
- verify actual application behavior rather than placeholders

## Verification

Before merging a change, run the relevant checks for the modified area.

Available project scripts include:

- `scripts/run_backend.ps1`
- `scripts/run_tests.ps1`

Not every change requires every command, but relevant functionality should be verified.

## Version control

Development follows the branching model documented in `README.md`.

Changes are developed outside `main` and merged through pull requests after review and verification.

## Development tools

Automated tools, including code-review and AI-assisted tools, may be used to support development.

Their suggestions are treated as input for review. The developer remains responsible for understanding, verifying, and accepting changes.

