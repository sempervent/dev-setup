#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide a simple class for dealing with single or multi-file uploads."""
from typing import Union
import pathlib
import magic


class Files:
    """Auto-generate a list of tupled file objects."""

    def __init__(self, file_path: Union[list, str, pathlib.Path]):
        """Initialize with a file path."""
        self.files = []
        self.paths = []
        self.encodings = []
        if isinstance(file_path, list):
            for file_path_item in file_path:
                if isinstance(file_path_item, str):
                    file_path_item = pathlib.Path(file_path_item)
                self.paths.append(file_path_item)
                self.files.append(self.prepare(file_path_item))
                self.encodings.append(self.encoding(file_path_item))
        if isinstance(file_path, str):
            file_path = pathlib.Path(file_path)
        if isinstance(file_path, pathlib.Path):
            self.paths.append(file_path)
            self.files.append(self.prepare(file_path))
            self.encodings.append(self.encoding(file_path))
        self.file_sizes = [x.stat().st_size for x in self.paths]

    @staticmethod
    def encoding(file_path: Union[str, pathlib.Path]) -> Union[str, list]:
        """Return encoding from a file_path."""
        if isinstance(file_path, str):
            file_path = pathlib.Path(file_path)
        blob = file_path.open(mode='rb').read()
        encoding = magic.Magic(mime_encoding=True).from_buffer(blob)
        return encoding

    @staticmethod
    def prepare(file_path: pathlib.Path) -> tuple:
        """Prepare the file upload object."""
        return (
            'file',
            (file_path.name,
             file_path.open('rb'),
             magic.from_file(str(file_path), mime=True)
             )
        )

    def get(self):
        """Return the self.files state."""
        if len(self.files) == 0:  # return nothing if no files
            return None
        return self.files

    def sizes(self):
        """Return the file size in bytes."""
        if len(self.file_sizes) == 0:
            return None
        if len(self.file_sizes) == 1:
            return self.file_sizes[0]
        return self.file_sizes


if __name__ == "__main__":
    a = Files(['__init__.py', 'files.py', 'README.md'])
    print(a.get())
    print(a.sizes())
    print(a.encodings)
    b = Files('files.py')
    print(b.get())
    print(b.sizes())
