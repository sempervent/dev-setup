#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the colors class."""
import unittest
import inspect

from depy.colors import Colors


class TestColorOutput(unittest.TestCase):
    """Test the Colors class for methods and values."""

    def test_colors(self):
        """Test that colors are represented as strings."""
        test_strings = {
            contents[0]: contents[1] for contents in inspect.getmembers(
                Colors, lambda x: not inspect.isroutine(x))
            if not contents[0].startswith('_')
        }
        self.assertEqual(len(test_strings), 27)
        for attribute in test_strings:
            self.assertEqual(getattr(Colors, attribute),
                             test_strings[attribute])
        colors_test = Colors('test')
        test_methods = {
            contents[0]: contents[1] for contents in inspect.getmembers(
                colors_test, callable)
            if not contents[0].startswith('_') and contents[0].upper()
            and contents[0] in list(test_strings.keys())
            and contents[0] != 'reset'
        }
        for function in test_methods:
            colors_test.reset()
            self.assertEqual(
                str(test_methods[function]()).split('test', maxsplit=1)[0],
                test_strings[function.upper()]
            )


if __name__ == "__main__":
    unittest.main()
