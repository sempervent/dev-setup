#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup mypy installation."""
import os
import pathlib
from setuptools import setup

_SCRIPTS = [str(pathlib.Path('bin/') / script) for script in os.listdir('bin')]

setup(
    name="mypy",
    version="0.0.2",
    description="Common everyday tools made easier.",
    author="Joshua N. Grant",
    author_email="jngrant@live.com",
    packages=["mypy", "mypy.net", "mypy.db"],
    install_requires=(
        pathlib.Path('requirements.txt'
                     ).read_text(encoding='UTF-8').split()),
    scripts=_SCRIPTS,
)
