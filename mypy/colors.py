#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide a colors class for use in printing."""


class Colors:
    """Provide a Colors class for pretty printing to the console."""
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    RESET = "\033[0m"
    RESET_BOLD = "\033[21m"
    RESET_DIM = "\033[22m"
    RESET_UNDERLINE = "\033[24m"
    RESET_BLINK = "\033[25m"
    FOREGROUND = "\033[39m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    LIGHT_GRAY = "\033[37m"
    DARK_GRAY = "\033[90m"
    LIGHT_RED = "\033[91m"
    LIGHT_GREEN = "\033[92m"
    LIGHT_YELLOW = "\033[93m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_MAGENTA = "\033[95m"
    LIGHT_CYAN = "\033[96m"

    def print(message: str,
              preceeding_color: str = '',
              proceeding_color: str = '',
              ):
        """Print message to stdout."""
        print(preceeding_color + f"{message}" + proceeding_color)

