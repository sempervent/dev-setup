#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the response class."""
import unittest

from depy.net.response import Response, METHODS

URL = 'https://httpbin.org/'


class TestResponse(unittest.TestCase):
    """Test the Response class."""

    def test_all_methods(self):
        """Use self.test(method) to test the methods."""
        def test_method(method: str):
            """Generic test method."""
            response = Response(url=URL + method, method=method)
            response.submit()
            self.assertTrue(response.status_code(), 200)
            print(response.response.text)
            self.assertTrue(response.as_json()['url'], URL + method)
        for method in METHODS:
            if method not in ['HEAD', 'OPTIONS', 'DELETE']:
                test_method(method.lower())


if __name__ == "__main__":
    unittest.main()
