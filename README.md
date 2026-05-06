# jobloom

`jobloom` is a compact Elixir repository for backend services, centered on this goal: Schedule actor-style jobs with retry policy and queue inspection.

## Project Rationale

The point is to make a small domain rule concrete enough that a reader can change it and immediately see what broke.

## Jobloom Review Notes

The first comparison I would make is `session drift` against `queue pressure` because it shows where the rule is most opinionated.

## Feature Set

- `fixtures/domain_review.csv` adds cases for queue pressure and retry load.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/jobloom-walkthrough.md` walks through the case spread.
- The Elixir code includes a review path for `session drift` and `queue pressure`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Architecture

The repository has two validation layers: the original compact policy fixture and the domain review fixture. They are separate so one can change without hiding failures in the other.

The Elixir addition stays small enough to inspect in one sitting.

## Usage

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Test Command

The same command runs the local verification path. The highest-scoring domain case is `recovery` at 180, which lands in `ship`. The most cautious case is `baseline` at 128, which lands in `watch`.

## Next Improvements

This remains a local project with deterministic fixtures. It does not depend on credentials, hosted services, or live data. Future work should add richer malformed inputs before widening the public API.
