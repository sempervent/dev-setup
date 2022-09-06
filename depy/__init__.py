#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Allow imports from this directory."""
import itertools
from collections.abc import Iterable
from typing import Iterable as IterableType


def unlist(lst: IterableType):
    """Unlist an iterable."""
    if isinstance(lst, Iterable):
        return list(itertools.chain.from_iterable(lst))
    return lst


if __name__ == "__main__":
    test_list = [[1, 2], [3, 4, 5], [6, 7], [8, [9]]]
    print(unlist(test_list))

