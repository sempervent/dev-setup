#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Make docker functions easy."""
import os
import shlex
import pathlib
import subprocess
from typing import Optional, Union

from depy import flatten


class Compose:
    """Abstraction layer to call docker-compose commands from the shell."""

    VALID_COMMANDS = ["build", "config", "create", "down", "events", "exec",
                      "help", "images", "kill", "logs", "pause", "port", "ps",
                      "pull", "push", "restart", "rm", "run", "scale", "start",
                      "stop", "top", "unpause", "up", "version"]

    def __init__(self, command: str,
                 options: Optional[Union[str, list]] = None,
                 directory: Optional[Union[str, pathlib.Path]] = os.getcwd(),
                 container: Optional[str] = None):
        """Initialize a compose command."""
        if command not in self.VALID_COMMANDS:
            raise ValueError(
                f'{command} not an available docker-compose option.')
        self.command = command
        if options is None:
            self.options = options
        elif isinstance(options, str):
            self.options = shlex.split(options)
        elif isinstance(options, list):
            self.options = options
        else:
            raise TypeError(f'{options} is not a str or list')
        if isinstance(directory, str):
            directory = pathlib.Path(directory)
        self.directory = directory
        if isinstance(container, str):
            self.container = container
        elif container is None:
            self.container = container
        else:
            raise TypeError(f'{container} is not a str or None')
        self.output = None
        self.error = None

    def submit(self):
        """Submit the Compose class to subprocess."""
        command = ['docker-compose', self.command]
        if self.options is not None:
            command.extend(self.options)
        if self.container is not None:
            command.extend(self.container)
        command = flatten(command)
        with subprocess.Popen(args=command,
                             cwd=str(self.directory),
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE) as proc:
            self._process(proc.communicate())

    def _process(self, proc: tuple):
        """Process the results of a communicate into self."""
        self.output = proc[0].decode('utf-8')
        self.error = proc[1].decode('utf-8')

    def show_output(self):
        """Show the output of the command."""
        print(self.output)

    def show_error(self):
        """Show the errors of the command."""
        print(self.error)
