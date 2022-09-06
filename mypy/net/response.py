#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide a wrapper around requests."""
import pathlib
from typing import Optional, Union, Any, Literal
import requests
from requests.auth import HTTPBasicAuth
import validators
from pydantic import BaseModel, validator

from mypy.models.auth import User
from mypy.net.files import Files

METHODS = ['GET', 'PUT', 'PATCH', 'POST', 'HEAD']
ERROR_RETURN_TYPES = ['string', 'dict']


class Response(BaseModel):
    """Abstraction wrapper for a request response."""
    url: str
    method: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    data: Optional[dict] = None
    headers: Optional[dict] = None
    file_paths: Optional[Union[list, pathlib.Path, str]] = None
    retries: Optional[int] = 0
    timeout: Optional[int] = 30
    verify: Optional[bool] = True
    user: Optional[Any] = None
    files: Optional[Any] = None
    response: Optional[Any] = None
    params: Optional[Union[dict, list]] = None

    def __init__(self, **kwargs):
        """Initialize the response class."""
        super().__init__(**kwargs)
        self.user = User(username=self.username, password=self.password) \
            if self.username is not None and self.password is not None \
            else None
        self.files = Files(self.file_paths) if self.file_paths is not None \
            else None

    @validator('url')
    def _validate_url(cls, url):
        if not validators.url(url):
            raise ValueError(f'{url} is not a valid URL')
        return url

    @validator('method')
    def _validate_method(cls, method):
        if not method.upper() in METHODS:
            raise ValueError(f'{method} not found in {METHODS}')
        return method.upper()

    def auth(self):
        """Return an authentication tuple for use with requests."""
        if self.username is None or self.password is None:
            return None
        return HTTPBasicAuth(self.username, self.password)

    def submit(self):
        """Submit a request to the url."""
        retry_counter = self.retries
        self.response = None
        while retry_counter >= self.retries:
            response = requests.request(
                method=self.method,
                url=self.url,
                data=self.data,
                files=self.files,
                timeout=self.timeout,
                verify=self.verify,
                auth=self.auth()
            )
            if response.status_code == 200:
                self.response = response
                break
            self.response = response
            retry_counter -= 1

    def error(self,
              return_type: Literal['dict', 'string']  = 'dict'
              ) -> Union[dict, str]:
        """Return the error code and the description."""
        if self.response is None:
            return None
        if return_type == 'dict':
            return {
                'error_code': self.response.status_code,
                'error_description': self.response.reason,
            }
        if return_type == 'string':
            return f"Response failed with {self.response.status_code} " + \
                f"code and description: {self.resposne.reason}."


if __name__ == "__main__":
    response = Response(url='https://google.com',
                        method='get')
    response.submit()
    print(response.response.text)
    response = Response(url='https://google.com',
                        method='post')
    response.submit()
    print(response.error())
