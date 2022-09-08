#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bash models for use in scripts."""
from uuid import uuid4
from typing import Union, Optional, List

from pydantic import BaseModel, Field, validator, UUID4

DOCUMENTATION_INDICATION_STR = '#/'
USAGE_STRING = '# usage'

class BashDocumentationLine(BaseModel):
    """Abstraction for documentation in bash script."""
    module_name: str
    documentation: Union[str, List[str]]
    markers: bool = True

    def __str__(self) -> str:
        """Representation of Bash Documentation."""
        contents = DOCUMENTATION_INDICATION_STR + 'Usage:\n\t./' + \
            self.module_name + ' [OPTIONS]\n'
        if isinstance(self.logic, str):
            contents += self.logic
        elif isinstance(self.logic, list):
            for item in self.logic:
                contents += item + '\n'
        markers = ''
        end_markers = ''
        if markers is True:
            markers += ' {{{1'
            end_markers += '# 1}}}'
        return USAGE_STRING + markers + '\n' + DOCUMENTATION_INDICATION_STR +\
            contents + end_markers + '\n'


# pylint: disable=too-few-public-methods
class BashVariable(BaseModel):
    """Construct a BashVariable."""
    key: str
    value: str = ""

    def __str__(self) -> str:
        """Representation of BashVariable."""
        return f'{self.key}={self.value}'


class BashFunction(BaseModel):
    """Construct a Bash function."""
    name: str
    logic: Union[list, str]
    markers: bool = False

    def __str__(self) -> str:
        """Representation of BashFunction."""
        contents = ""
        if isinstance(self.logic, str):
            contents += self.logic
        elif isinstance(self.logic, list):
            for item in self.logic:
                contents += ('\t' + item + '\n')
        markers = ""
        end_markers = ""
        if self.markers is True:
            markers += ' {{{2'
            end_markers += ' # 2}}}'
        return self.name + '() {' + markers + '\n' + contents + '}' + \
            end_markers + '\n'


class BashDocumentation(BaseModel):
    """Provide a Bash documentation script strint."""


class BashEnvironment(BaseModel):
    """Populate the BashEnvironment class."""
    environment_variables: List[BashVariable]
    bash_functions: List[BashFunction]

    class Config:
        """Options to the BaseModel config class."""
        allow_arbitrary_types = True

if __name__ == "__main__":
    print(BashVariable(key='LOGLEVEL', value='INFO'))
    print(BashFunction(name='test_function',
                       logic='ps aux\n',
                       markers=True))

