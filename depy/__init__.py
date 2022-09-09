#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Allow imports from this directory."""
from typing import Iterable

PRIMITIVES = (str, bytes, bool, float, int)


def unlist(lst: Iterable):
    """Unlist an iterable."""
    for item in lst:
        if isinstance(item, Iterable) and not isinstance(item, PRIMITIVES):
            yield from unlist(item)
        else:
            yield item


def flatten(lst: Iterable) -> list:
    """Return a flat list from an Iterable."""
    return list(unlist(lst=lst))
