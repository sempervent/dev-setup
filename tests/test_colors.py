#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the colors class."""
import unittest
import inspect

from depy.colors import Colors


class TestColorOutput(unittest.TestCase):

    def test_colors(self):
        test_strings = {
            contents[0]: contents[1] for contents in inspect.getmembers(
                Colors, lambda x: not(inspect.isroutine(x)))
            if isinstance(contents[0], str) and isinstance(contents[1], str)
            and not contents[0].startswith('_')
        }
        self.assertEqual(len(test_strings), 27)
        for attribute in test_strings:
            self.assertEqual(getattr(Colors, attribute),
                             test_strings[attribute])


if __name__ == "__main__":
    unittest.main()
