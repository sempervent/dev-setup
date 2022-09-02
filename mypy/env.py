#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Use this file to read values in from an env file."""
import os
import pathlib
from typing import Union


def process_value(value: str) -> Union[int, str, bool]:
    """Convert value to proper type."""
    if value.lower() in ['true', 't']:
        return True
    if value.lower() in ['false', 'f']:
        return False
    try:
        return int(value)
    except ValueError:
        pass
    return value


def load_env(file_path: Union[str, pathlib.Path],
             register: bool = True) -> dict:
    """Load an environment file into a dict."""
    if isinstance(file_path, str):
        file_path = pathlib.Path(file_path)
    env_dict = {}
    if file_path.exists() is False:
        raise FileNotFoundError
    env_lines = file_path.read_text().splitlines()
    env_pairs = [x.split('=') for x in env_lines]
    for pair in env_pairs:
        key, value = pair[0], process_value(pair[1])
        env_dict[key] = value
        if register is True:
            globals()[key] = value
    return env_dict


def get_env(
    key: str,
    value: Union[int, str, bool] = None
) -> Union[int, str, bool]:
    """Retrieve a key with default value from os.environ."""
    if key in os.environ:
        return process_value(os.environ[key])
    if key in globals():
        return globals()[key]
    else:
        return value

