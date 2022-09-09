#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the __init__.py file of the depy package."""
import unittest

from depy import unlist, flatten


class TestInit(unittest.TestCase):
    """Test the depy init."""

    def setUp(self):
        """Add test lists and expected outcome."""
        self.test_list = [[0, 1], 2, 3, [4, 5, 6]]
        self.expected_list = [0, 1, 2, 3, 4, 5, 6]

    def test_unlist(self):
        """Test the unlist function."""
        flatten_list = list(unlist(self.test_list))
        self.assertEqual(flatten_list, self.expected_list)

    def test_flatten(self):
        """Test the flatten function."""
        flatten_list = flatten(self.test_list)
        self.assertEqual(flatten_list, self.expected_list)


if __name__ == "__main__":
    unittest.main()
