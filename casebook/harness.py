"""Executable checks for the jobloom casebook."""

from __future__ import annotations

from collections import Counter

from . import jobloom_segment_00
from . import jobloom_segment_01
from . import jobloom_segment_02
from . import jobloom_segment_03
from . import jobloom_segment_04
from . import jobloom_segment_05
from . import jobloom_segment_06
from . import jobloom_segment_07
from . import jobloom_segment_08
from . import jobloom_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from jobloom_segment_00.iter_jobloom_00()
    yield from jobloom_segment_01.iter_jobloom_01()
    yield from jobloom_segment_02.iter_jobloom_02()
    yield from jobloom_segment_03.iter_jobloom_03()
    yield from jobloom_segment_04.iter_jobloom_04()
    yield from jobloom_segment_05.iter_jobloom_05()
    yield from jobloom_segment_06.iter_jobloom_06()
    yield from jobloom_segment_07.iter_jobloom_07()
    yield from jobloom_segment_08.iter_jobloom_08()
    yield from jobloom_segment_09.iter_jobloom_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def jobloom_summary() -> dict:
    return assert_expected()
