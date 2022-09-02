#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide convenient wrappers for tasks."""
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Iterable

from tqdm import tqdm


class ParallelExecutor():
    """Provide abstract interface for parallel executions."""

    def __init__(
        self, function: Callable, iterators: Iterable
    ):
        """Initialize and run the execution."""
        self.function = function
        self.iterators = iterators
        self.futures = []

    def execute(self):
        """Execute the function in parallel."""
        self.futures = []
        length = len(self.iterators)
        with tqdm(total=length) as pbar:
            with ThreadPoolExecutor() as executor:
                for item in self.iterators:
                    self.futures.append(
                        executor.submit(self.function, item)
                    )
                    pbar.update(1)

    def submit(self):
        """Execute function without tqdm."""
        self.futures = []
        with ThreadPoolExecutor() as executor:
            for item in self.iterators:
                self.futures.append(
                    executor.submit(self.function, item)
                )
        return self.futures

    def exceptions(self) -> list:
        """Return all non-None exceptions."""
        return [x.exception() for x in self.futures
                if x.exception() is not None]

    def results(self) -> list:
        """Return the results of the execution."""
        return [x.result() for x in self.futures]

    def inputs(self) -> list:
        """Return the inputs as a list."""
        return [x for x in self.iterators]


if __name__ == "__main__":
    def count(x: int):
        """Dummy example function."""
        return 2**x

    integers = range(10)

    pe = ParallelExecutor(count, integers)
    pe.execute()
    print(pe.exceptions())
    print(pe.results())
    print(pe.inputs())
    print(pe.submit())
