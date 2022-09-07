#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide a pydantic log entry."""
import os
import logging
from uuid import uuid4
from datetime import datetime
from typing import List, Optional, Type

from pydantic import BaseModel
from rich.logging import RichHandler
from rich.traceback import install

from depy.env import get_env

VALID_LOG_LEVELS = ['NOTSET', 'INFO', 'WARN', 'WARNING', 'ERROR', 'CRITICAL']


def _validate_log_level(loglevel: str):
    """Validate the log level."""
    if loglevel.upper() not in VALID_LOG_LEVELS:
        raise ValueError(f'{loglevel.upper()} is not a valid log level.')
    return True


def _get_loglevel(loglevel_var: str = 'LOGLEVEL',
                  default: Optional[str] = None) -> str:
    """Retrieve the loglevel from the os.environ."""
    if default is not None and _validate_log_level(default):
        default = default.upper()
    elif default is None:
        default = 'INFO'
    loglevel = get_env(key=loglevel_var, value=default)
    try:
        if _validate_log_level(loglevel) is True:
            return loglevel.upper()
    except ValueError as exception:
        logging.warning(f'{exception}, returning {default}')
        return default


def create_rich_logger(loglevel_var: str = 'LOGLEVEL',
                       loglevel: Optional[str] = None) -> logging.logger:
    """Create a rich logger."""
    install()
    log_level = loglevel if loglevel is not None \
        else _get_loglevel(loglevel_var=loglevel_var, default=loglevel)
    rich_handler = RichHandler(rich_tracebacks=True, markup=True)
    logging.basicConfig(level=log_level, format='%(message)s',
                        datefmt='[%Y-%m-%d %H:%M:%S]',
                        handlers=[rich_handler])
    return logging.getLogger('rich')


# pylint: disable=too-few-public-methods
class Log(BaseModel):
    """Create the database for a log statement."""
    id: str = str(uuid4())
    level: int = logging.INFO
    timestamp: Optional[datetime] = datetime.utcnow()
    message: str = ''
    exception: Type[BaseException] = None
    logger: str = 'main'

    def log(self):
        """Log a message."""
        logger = logging.getLogger(self.logger)
        if self.level == logging.DEBUG:
            logger.debug(self.message)
        elif self.level == logging.INFO:
            logger.info(self.message)
        elif self.level == logging.WARNING:
            logger.warning(self.message)
        elif self.level == logging.ERROR:
            logger.error(self.message)
        elif self.level == logging.CRITICAL:
            logger.critical(self.message)

