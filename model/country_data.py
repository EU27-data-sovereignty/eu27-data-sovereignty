#!/usr/bin/env python3
"""
Assemble what is known about one country into a plain dict (DECISIONS.md #6).

This is the input the content model (`document.py`) is built from, and it goes into the JSON
bundle unchanged. It reads nothing about any other country: no baseline, no ratios, no
"structurally different from" (#72). Capacity is not here either -- it is withdrawn until a
country can be sized from its own measured holdings (#73).

Pure function of its arguments, no file I/O (#7): the parameter row and the register view are
passed in.
"""
from __future__ import annotations


def build(c: dict, national_data: list[dict] | None = None) -> dict:
    """One country: its parameter row and its critical-holdings register view.

    `national_data` is `national_data.for_country()`: every holding class, in tier order, with
    "unrecorded" where nothing has been verified yet. None renders exactly like an unresearched
    country, which is what it is.
    """
    return {
        "iso2": c["iso2"],
        "name": c["country"],
        "params": dict(c),
        "national_data": national_data or [],
    }
