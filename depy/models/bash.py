#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bash models for use in scripts."""
from uuid import uuid4
from typing import Union, Optional, List

from pydantic import BaseModel, Field, validator, UUID4


# pylint: disable=too-few-public-methods
class BashVariable(BaseModel):
    """Construct a BashVariable."""
    key: str
    value: str = ""

    def __repr__(self) -> str:
        """Representation of BashVariable."""
        return f'{self.key}={self.value}'


class BashFunction(BaseModel):
    """Construct a Bash function."""
    name: str
    logic: Union[list, str]
    markers: bool = False

    def __repr__(self) -> str:
        """Representation of BashFunction."""
        contents = ""
        if isinstance(self.logic, str):
            contents += self.logic
        elif isinstance(self.logic, list):
            for item in self.logic:
                contents += ('\t' + item + '\n')
        markers = ""
        end_markers = ""
        if markers is True:
            markers += ' {{{2'
            end_markers += ' # 2}}}'
        return self.name + '() {' + markers + contents + '}' + end_markers + \
            '\n'


class BashEnvironment(BaseModel):
    """Populate the BashEnvironment class."""
    environment_variables: List[BashVariable]
    bash_functions: List[BashFunction]

    class Config:
        """Options to the BaseModel config class."""
        allow_arbitrary_types = True
