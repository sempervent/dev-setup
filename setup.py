#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup mypy installation."""
from setuptools import setup

setup(
    name="mypy",
    version="0.0.1",
    description="Common everyday tools made easier.",
    author="Joshua N. Grant",
    author_email="jngrant@live.com",
    packages=["mypy", "mypy.net"],
    install_requires=open('requirements.txt').read().splitlines(),
)
