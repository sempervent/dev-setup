#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide a PostgreSQL mixin."""
import os
from typing import Union, Any
import psycopg2


class PostgresMixin:
    """Provide PostgresMixin for use with Database class."""

    def connect(self):
        """Open a connection."""
        self.connection = psycopg2.connect(
            host=self.host if self.host is not None else os.getenv('PG_HOST'),
            port=self.port if self.port is not None else int(os.getenv('DB_PORT')),
            user=self._user if self._user is not None else os.getenv('DB_USER'),
            password=self._pass if self._pass is not None else os.getenv('DB_PASS'),
            dbname=self.db if self.db is not None else os.getenv('DB_NAME'),
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        """Disconnect from the database."""
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        self.connection = None
        self.cursor = None

    def select(self, query: str = '') -> Any[list, tuple]:
        """Send a query to the database."""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, query: str = '', parameters: Union[list, tuple] = ()):
        """Insert into the database."""
        self.cursor.execute(query, parameters)

    def commit(self):
        """Commit the changes to the databse."""
        self.connection.commit()

    def rolback(self):
        """Rollback the changes to the databse."""
        self.connection.rollback()


