#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide a pydantic log entry."""
import logging
from uuid import uuid4
from datetime import datetime
from typing import List, Optional, Type

from pydantic import BaseModel


# pylint: disable=too-few-public-methods
class Log(BaseModel):
    """Create the database for a log statement."""
    id: str = uuid4()
    level: int = logging.INFO
    timestamp: Optional[datetime] = datetime.utcnow()
    message: str = ''
    exception: Type[BaseException] = None
    logger: str = 'main'

