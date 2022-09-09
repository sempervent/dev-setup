#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup depy installation."""
import os
import pathlib
from setuptools import setup

_SCRIPTS = [str(pathlib.Path('bin/') / script) for script in os.listdir('bin')]
_VERSION = pathlib.Path('VERSION').read_text(encoding='UTF-8').splitlines()[0]

setup(
    name="depy",
    version=_VERSION,
    description="Common everyday tools made easier.",
    author="Joshua N. Grant",
    author_email="jngrant@live.com",
    packages=["depy", "depy.net", "depy.db", "depy.models"],
    install_requires=(
        pathlib.Path('requirements.txt'
                     ).read_text(encoding='UTF-8').split()),
    scripts=_SCRIPTS,
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov',
        ],
        'postgres': [
            'psycopg2-binary',
        ],
    }
)
