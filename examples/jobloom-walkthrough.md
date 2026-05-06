# Jobloom Walkthrough

The fixture is intentionally compact, so the review starts with the cases that pull farthest apart.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | queue pressure | 128 | watch |
| stress | retry load | 167 | ship |
| edge | worker slack | 154 | ship |
| recovery | session drift | 180 | ship |
| stale | queue pressure | 144 | ship |

Start with `recovery` and `baseline`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

`recovery` is the optimistic case; use it to make sure the scoring path still rewards strong signal.
