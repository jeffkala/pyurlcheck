"""Testing for pyurlcheck."""
import os

import toml
from pyurlcheck import __version__


def test_version():
    """Simple version test."""
    parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    print(parent_path)
    poetry_version = toml.load(f".{parent_path}pyproject.toml")["tool"]["poetry"]["version"]
    assert __version__ == poetry_version
