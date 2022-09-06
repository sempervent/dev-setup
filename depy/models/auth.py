#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide generic auth models."""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


# pylint: disable=too-few-public-methods
class User(BaseModel):
    """Basic User class for authentication models."""
    username: str
    password: str
    created: Optional[datetime] = datetime.utcnow()

    def created_at(self, as_datetime=False):
        """Return the created datetime."""
        if as_datetime is True:
            return self.created
        return self.created.strftime('%Y-%m-%d %H:%M:%S')

    def auth(self):
        """Return auth for a request object."""
        return (self.username, self.password)


class RequestsUser(User):
    """Auth for requests usage."""
    auth_token: str = None

    def bearer(self):
        """Return bearer headers."""
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.auth_token}'
        }


if __name__ == "__main__":
    auth = User(username='testuser',
                password='testpass')
    print(auth.dict())
    print(auth.created_at())
    auth = RequestsUser(username='testuser',
                        password='testpass')
    print(auth.auth())
    bearer_auth = RequestsUser(username='testuser',
                               password='testpass',
                               auth_token='testtoken')
    print(bearer_auth.bearer())

