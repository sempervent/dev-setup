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


if __name__ == "__main__":
    test_list = [[1, 2], [3, 4, 5], [6, 7], [8, [9]], 10]
    print(list(unlist(test_list)))

