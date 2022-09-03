#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import psycopg2


class PostgresMixin:

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


