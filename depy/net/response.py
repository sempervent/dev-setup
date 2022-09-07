#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide a wrapper around requests."""
import pathlib
from datetime import datetime
from typing import Optional, Union, Any, Literal, List, Dict
from http.cookiejar import CookieJar
import requests
from requests.auth import HTTPBasicAuth
import validators
from pydantic import BaseModel, validator

from depy.models.auth import User
from depy.net.files import Files

JSON_TYPE = Union[None, int, str, bool, float, Dict[str, Any], List[Any]]
METHODS = ['GET', 'PUT', 'PATCH', 'POST', 'HEAD', 'OPTIONS', 'DELETE']
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
    json_data: Optional[JSON_TYPE] = None
    created: Optional[datetime] = datetime.utcnow()
    accessed: Optional[datetime] = None
    allow_redirects: Optional[bool] = True
    stream: Optional[bool] = False
    cert: Optional[Union[str, tuple]] = None
    cookies: Optional[Union[dict, CookieJar]] = None
    proxies: Optional[dict] = None
    return_headers: Optional[dict] = None

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **kwargs):
        """Initialize the response class."""
        super().__init__(**kwargs)
        self.user = User(username=self.username, password=self.password) \
            if self.username is not None and self.password is not None \
            else None
        self.files = Files(self.file_paths) if self.file_paths is not None \
            else None

    @validator('cookies')
    def _validate_cookies(cls, cookies):
        if isinstance(cookies, (dict, CookieJar)):
            return cookies
        return None

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
        # pylint: disable=redefined-outer-name
        while retry_counter >= self.retries:
            response = requests.request(
                method=self.method,
                url=self.url,
                params=self.params,
                data=self.data,
                json=self.json_data,
                headers=self.headers,
                cookies=self.cookies,
                files=self.files,
                auth=self.auth(),
                timeout=self.timeout,
                allow_redirects=self.allow_redirects,
                proxies=self.proxies,
                verify=self.verify,
                stream=self.stream,
                cert=self.cert,

            )
            self.accessed = datetime.utcnow()
            if response.status_code == 200:
                self.response = response
                break
            self.response = response
            retry_counter -= 1

    def error(self,
              return_type: Literal['dict', 'string'] = 'dict'
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

    def text(self) -> str:
        """Return the response as text."""
        if self.response is None:
            return None
        return self.response.text

    def as_json(self) -> dict:
        """Return the response as json."""
        if self.response is None:
            return None
        return self.response.json()

    def access_headers(self) -> dict:
        """Return the headers from the response."""
        if self.response is None:
            return None
        return self.response.headers

    def status_code(self) -> int:
        """Return the status code of the response."""
        if self.response is None:
            return None
        return self.response.status_code


if __name__ == "__main__":
    response = Response(url='https://httpbin.org/get',
                        method='get')
    response.submit()
    print(response.text())
    print(response.as_json())
    response = Response(url='https://httpbin.org/get',
                        method='post')
    response.submit()
    print(response.error())
    print(response.dict())
