#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the __init__.py file of the depy package."""
import unittest

from depy import unlist


class TestInit(unittest.TestCase):
    """Test the depy init."""

    def test_unlist(self):
        """Test the unlist function."""
        test_list = [[0, 1], 2, 3, [4, 5, 6]]
        flatten_list = list(unlist(test_list))
        expected_list = [0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten_list, expected_list)


if __name__ == "__main__":
    unittest.main()
