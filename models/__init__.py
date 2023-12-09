#!/usr/bin/python3
"""
This module is first called whenever this package is used.
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
