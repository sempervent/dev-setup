#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the wrapper methods."""
import unittest

from depy.wrappers import ParallelExecutor

NUMS = range(1000)


def fxn(num: int) -> int:
    """Generic function for use with the test."""
    return 2**num


NUMS_RESULTS = [fxn(num) for num in NUMS]


class TestParallelExecutor(unittest.TestCase):
    """Test the ParallelExecutor."""

    # pylint: disable=invalid-name
    def test_parallel_execution(self):
        """Test methods for parallel execution."""
        pe = ParallelExecutor(function=fxn, iterators=NUMS)
        pe.execute()
        self.assertEqual(pe.results(), NUMS_RESULTS)
        self.assertEqual(pe.exceptions(), None)
        futures = pe.submit(values=True)
        self.assertGreater(len(futures), 0)


if __name__ == "__main__":
    unittest.main()
