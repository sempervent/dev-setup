#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide generic auth models."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from requests.auth import HTTPBasicAuth


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

    def basic_auth(self):
        """Return HTTPAuth for a request object."""
        return HTTPBasicAuth(self.username, self.password)


class TokenUser(User):
    """Auth for requests usage."""
    auth_token: str = None
    auth_token_created: Optional[datetime] = datetime.utcnow()

    def bearer(self, include_content_type: bool = False):
        """Return bearer headers."""
        bearer_header = {}
        if include_content_type is True:
            bearer_header.update({'Content-Type': 'application/json'})
        bearer_header.update({'Authorization': f'Bearer {self.auth_token}'})
        return bearer_header


if __name__ == "__main__":
    auth = User(username='testuser',
                password='testpass')
    print(auth.dict())
    print(auth.created_at())
    auth = TokenUser(username='testuser',
                     password='testpass')
    print(auth.auth())
    bearer_auth = TokenUser(username='testuser',
                            password='testpass',
                            auth_token='testtoken')
    print(bearer_auth.bearer())

