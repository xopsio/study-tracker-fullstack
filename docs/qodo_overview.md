# Qodo.ai usage and documentation

Qodo.ai is used in this project as a development support tool for code review,
problem analysis, testing, and learning.

The purpose of using Qodo is to support the development process rather than
automatically generate or accept changes.

The developer remains responsible for understanding, reviewing, verifying,
and accepting the final implementation.

## Usage

Qodo may be used to:

- review code changes
- identify possible defects
- analyze technical problems
- suggest small improvements
- support testing and verification
- provide an additional review during pull requests

Suggestions from Qodo are treated as development input and are not accepted
automatically.

## Development approach

When Qodo is used, changes should follow the same development practices as
other work in the repository.

In particular:

- changes should remain small and focused
- unrelated refactoring should be avoided
- relevant functionality should be verified
- suggestions should be reviewed before they are accepted
- documentation should be updated when behavior changes

General development practices are documented in `best_practices.md`.

Guidelines for automated development tools are documented in `AGENTS.md`.

## Related documentation

Additional Qodo-specific documentation is available in the `docs/` directory.

### `docs/qodo_workflow.md`

Describes the workflow used when Qodo is involved in problem analysis,
implementation, and verification.

### `docs/qodo_prompts.md`

Contains example prompts that have been used to guide Qodo during development.

### `docs/learning-log.md`

Records selected development and learning cases where Qodo was used to help
analyze a non-trivial problem.

### `docs/commit-notes.md`

Contains notes related to earlier Qodo and documentation commits.

These files are kept as part of the project's development documentation and
history.

## Code review

Qodo may also participate in pull request reviews.

Automated review comments are evaluated in the same way as other review
feedback. A suggestion may be accepted, modified, or rejected depending on
whether it improves the project and can be verified.

The presence of an automated review does not replace developer review or
testing.

## Version control

The repository follows the branching model documented in `README.md`.

Development work is performed outside `main`. Task-specific branches may be
merged into `develop`, and reviewed changes are later merged from `develop`
into `main`.

Qodo reviews may be part of this workflow when pull requests are created.

## Principles

The use of Qodo in this project follows a few general principles:

- understand changes before accepting them
- prefer small and verifiable changes
- use automated tools as support rather than authority
- verify affected functionality
- keep the developer responsible for the final result

Qodo is one of the tools used during development. It supports the project but
does not define the project itself.
