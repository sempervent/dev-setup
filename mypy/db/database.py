#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide a generic database class."""
from abc import ABCMeta, abstractmethod


# pylint: disable=unnecessary-pass
class Database(metaclass=ABCMeta):
    """Generic database method."""

    def __init__(self, **kwargs):
        """Initialize self through kwargs."""
        self._user = kwargs.get('user') if 'user' in kwargs else None
        self._pass = kwargs.get('password') if 'password' in kwargs else None
        self.host = kwargs.get('host') if 'host' in kwargs else None
        self.port = kwargs.get('port') if 'port' in kwargs else None
        self.protocol = kwargs.get('protocol') if 'protocol' in kwargs else None
        self.connection = None

    @abstractmethod
    def connect(self, **kwargs):
        """Abstract method for connecting to database."""
        pass

    @abstractmethod
    def disconnect(self, **kwargs):
        """Abstract method for disconnecting from database."""
        pass

    def __enter__(self):
        """Use to enter context manager."""
        self.connect()
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Exit the context manager."""
        self.disconnect()
        self.connection = None

