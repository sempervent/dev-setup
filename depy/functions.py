#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Predefined bash functions here."""
from depy.colors import Colors
from depy.models.bash import BashFunction, BashVariable

def export_banner(project_name: str = '$PROJECT') -> BashFunction:
    """Export a banner function."""
    project_def = "BANNER=" + Colors(project_name).green()
    banner_variable = BashVariable(project_def.split('='))
    banner_function = BashFunction(
        name="banner",
        logic=[banner_variable, 'echo -e "$BANNER"'],
        markers=True,
    )
    return banner_function


def export_die() -> str:
    """Export a die function."""
    die_function = BashFunction(
        name="die",
        logic=['echo -e "' + Colors('FAILURE:').red() + ' $1"'],
        markers=True,
    )
    return die_function


if __name__ == "__main__":
    print(export_banner())
    print(export_die())
