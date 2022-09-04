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


class RequestsUser(User):
    """Auth for requests usage."""
    auth_token: str = None

    def auth(self):
        """Return auth for a request object."""
        return (self.username, self.password)

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
    auth = RequestsUser(username='testuser',
                        password='testpass')
    print(auth.auth())
    bearer_auth = RequestsUser(username='testuser',
                               password='testpass',
                               auth_token='testtoken')
    print(bearer_auth.bearer())

