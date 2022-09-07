#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test environment loading."""
import os
import pathlib
import unittest
from tempfile import NamedTemporaryFile

from depy.env import load_env, get_env, process_value

ENVIRONMENT = """PG_HOST=localhost
PG_ADMIN=admin
PG_USER=user
PG_PORT=5432
VERBOSE=True"""

PAIRS = {key.split('=')[0]: key.split('=')[1]
         for key in ENVIRONMENT.splitlines()}


class TestEnvLoading(unittest.TestCase):
    """Tests for loading in the environment from a file."""

    def test_environment_loaded(self):
        """Test that the variables have been loaded in the environment."""
        with NamedTemporaryFile(mode='w') as temp_file:
            pathlib.Path(temp_file.name).write_text(
                ENVIRONMENT, encoding='UTF-8')
            env = load_env(temp_file.name,
                           register=True,
                           register_system=True)
        for var in list(env.keys()):
            print(f'{var} = {env[var]}')
            self.assertEqual(env[var], process_value(PAIRS[var]))
            self.assertEqual(process_value(os.environ[var]),
                             process_value(PAIRS[var]))
            # self.assertTrue(var in globals())
            # self.assertEqual(globals()[var], PAIRS[var])
            self.assertEqual(get_env(var, env[var]), process_value(PAIRS[var]))


if __name__ == "__main__":
    unittest.main()
