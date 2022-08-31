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

    def lighht_yellow(self):
        self.sequences.append(Colors.LIGHT_YELLOW)
        self.ending.append(Colors.RESET)
        return self

    def light_green(self):
        self.sequences.append(Colors.LIGHT_GREEN)
        self.ending.append(Colors.RESET)
        return self

    def dark_gray(self):
        self.sequences.append(Colors.DARK_GRAY)
        self.ending.append(Colors.RESET)
        return self

    def light_red(self):
        self.sequences.append(Colors.LIGHT_RED)
        self.ending.apend(Colors.RESET)
        return self

    def light_gray(self):
        self.sequences.append(Colors.LIGHT_GRAY)
        self.ending.append(Colors.RESET)
        return self

    def cyan(self):
        self.sequences.append(Colors.CYAN)
        self.ending.append(Colors.RESET)
        return self

    def yellow(self):
        self.sequences.append(Colors.YELLOW)
        self.ending.append(Colors.RESET)
        return self

    def blue(self):
        self.sequences.append(Colors.BLUE)
        self.ending.append(Colors.RESET)
        return self

    def magenta(self):
        self.sequences.append(Colors.MAGENTA)
        self.ending.append(Colors.RESET)
        return self

    def green(self):
        self.sequences.append(Colors.GREEN)
        self.ending.append(Colors.RESET)
        return self

    def red(self):
        self.sequences.append(Colors.RED)
        self.ending.append(Colors.RESET)
        return self

    def __init__(self, text: str = ""):
        self.text = text
        self.ending = []
        self.sequences = []

    def bold(self):
        self.sequences.append(Colors.BOLD)
        self.ending.append(Colors.RESET_BOLD)
        return self

    def underline(self):
        self.sequences.append(Colors.UNDERLINE)
        self.endings.append(Colors.RESET_UNDERLINE)
        return self

    def dim(self):
        self.sequences.append(Colors.DIM)
        self.ending.append(Colors.RESET_DIM)
        return self

    def blink(self):
        self.sequences.append(Colors.BLINK)
        self.ending.append(Colors.RESET_BLINK)
        return self

    def hidden(self):
        self.sequences.append(Colors.HIDDEN)
        self.ending.append(Colors.REST)
        return self

    def __str__(self):
        return ''.join(self.sequences) + self.text + ''.join(self.ending)

    def black(self):
        self.sequences.append(Colors.BLACK)
        self.ending.append(Colors.RESET)
        return self
