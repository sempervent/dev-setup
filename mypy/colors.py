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

    def __init__(self, text: str = ""):
        self.text = text
        self.ending = []
        self.sequences = []

    def light_cyan(self):
        """Color with LIGHT_CYAN."""
        self.sequences.append(Colors.LIGHT_CYAN)
        self.ending.append(Colors.RESET)
        return self

    def light_magenta(self):
        """Color with LIGHT_MAGENTA."""
        self.sequences.append(Colors.LIGHT_BLUE)
        self.ending.append(Colors.RESET)
        return self

    def light_blue(self):
        """Color with LIGHT_BLUE."""
        self.sequences.append(Colors.LIGHT_BLUE)
        self.ending.append(Colors.RESET)
        return self

    def light_yellow(self):
        """Color with LIGHT_YELLOW."""
        self.sequences.append(Colors.LIGHT_YELLOW)
        self.ending.append(Colors.RESET)
        return self

    def light_green(self):
        """Color with LIGHT_GREEN."""
        self.sequences.append(Colors.LIGHT_GREEN)
        self.ending.append(Colors.RESET)
        return self

    def dark_gray(self):
        """Color with DARK_GRAY."""
        self.sequences.append(Colors.DARK_GRAY)
        self.ending.append(Colors.RESET)
        return self

    def light_red(self):
        """Color with LIGHT_RED."""
        self.sequences.append(Colors.LIGHT_RED)
        self.ending.append(Colors.RESET)
        return self

    def light_gray(self):
        """Color with LIGHT_GRAY."""
        self.sequences.append(Colors.LIGHT_GRAY)
        self.ending.append(Colors.RESET)
        return self

    def cyan(self):
        """Color with CYAN."""
        self.sequences.append(Colors.CYAN)
        self.ending.append(Colors.RESET)
        return self

    def yellow(self):
        """Color with YELLOW."""
        self.sequences.append(Colors.YELLOW)
        self.ending.append(Colors.RESET)
        return self

    def blue(self):
        """Color with BLUE."""
        self.sequences.append(Colors.BLUE)
        self.ending.append(Colors.RESET)
        return self

    def magenta(self):
        """Color with MAGENTA."""
        self.sequences.append(Colors.MAGENTA)
        self.ending.append(Colors.RESET)
        return self

    def green(self):
        """Color with GREEN."""
        self.sequences.append(Colors.GREEN)
        self.ending.append(Colors.RESET)
        return self

    def red(self):
        """Color with RED."""
        self.sequences.append(Colors.RED)
        self.ending.append(Colors.RESET)
        return self

    def bold(self):
        """Color with BOLD."""
        self.sequences.append(Colors.BOLD)
        self.ending.append(Colors.RESET_BOLD)
        return self

    def underline(self):
        """Color with UNDERLINE."""
        self.sequences.append(Colors.UNDERLINE)
        self.ending.append(Colors.RESET_UNDERLINE)
        return self

    def dim(self):
        """Perform operation DIM."""
        self.sequences.append(Colors.DIM)
        self.ending.append(Colors.RESET_DIM)
        return self

    def blink(self):
        """Perform operation BLINK."""
        self.sequences.append(Colors.BLINK)
        self.ending.append(Colors.RESET_BLINK)
        return self

    def hidden(self):
        """Perform operation HIDDEN."""
        self.sequences.append(Colors.HIDDEN)
        self.ending.append(Colors.RESET)
        return self

    def __str__(self):
        """Return a string implementation."""
        return ''.join(self.sequences) + self.text + ''.join(self.ending)

    def black(self):
        """Color with BLACK."""
        self.sequences.append(Colors.BLACK)
        self.ending.append(Colors.RESET)
        return self
