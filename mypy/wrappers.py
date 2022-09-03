#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide convenient wrappers for tasks."""
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Iterable, Optional

from tqdm import tqdm


class ParallelExecutor():
    """Provide abstract interface for parallel executions."""

    def __init__(
        self, function: Callable, iterators: Iterable,
        persist_futures: bool = False,
    ):
        """Initialize and run the execution."""
        self.persist_futures = persist_futures
        self.function = function
        self.iterators = iterators
        self.futures = []

    def execute(self):
        """Execute the function in parallel."""
        if self.persist_futures is False:
            self.futures = []
        length = len(self.iterators)
        with tqdm(total=length) as pbar:
            with ThreadPoolExecutor() as executor:
                for item in self.iterators:
                    self.futures.append(
                        executor.submit(self.function, item)
                    )
                    pbar.update(1)

    def submit(self, values: bool = False):
        """Execute function without tqdm."""
        if self.persist_futures is False:
            self.futures = []
        with ThreadPoolExecutor() as executor:
            for item in self.iterators:
                self.futures.append(
                    executor.submit(self.function, item)
                )
        if values is True:
            return self.futures

    def exceptions(self) -> list[Optional]:
        """Return all non-None exceptions."""
        exceptions = [x.exception() for x in self.futures
                      if x.exception() is not None]
        if len(exceptions) == 0:
            return None
        return exceptions

    def results(self) -> list:
        """Return the results of the execution."""
        return [x.result() for x in self.futures]

    def inputs(self) -> list:
        """Return the inputs as a list."""
        return list(self.iterators)

    def done(self) -> list:
        """Check if all futures have completed."""
        return all(x.done() for x in self.futures)

    def set_iterators(self, iterators: Iterable):
        """Set the iterators attribute."""
        self.iterators = iterators

    def set_function(self, function: Callable):
        """Set the function attribute."""
        self.function = function


if __name__ == "__main__":
    # pylint: disable=invalid-name
    from mypy.colors import Colors
    from datetime import datetime

    def count(x: int):
        """Test function."""
        return 2**x

    integers = range(10)

    pe = ParallelExecutor(count, integers)
    pe.execute()
    print(Colors('Exceptions: ').red() +
          Colors(f'{pe.exceptions()}').light_red())
    print(Colors('Results: ').green() +
          Colors(f'{pe.results()}').light_green())
    print(Colors('Inputs: ').yellow() +
          Colors(f'{pe.inputs()}').light_yellow())
    all_done = False
    integers = range(20000)
    pe = ParallelExecutor(count, integers)
    start_date = datetime.utcnow()
    pe.execute()
    while not all_done:
        end_date = datetime.utcnow()
        all_done = pe.done()
        print(Colors('Duration: ').magenta() +
              Colors(f'{end_date - start_date}').yellow())
    print(pe.results()[0:10])
