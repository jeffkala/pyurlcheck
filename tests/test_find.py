"""Tests for Find"""

import os
import pytest
from pyurlcheck.find import _read_in_file, _new_populate_file_dict, FindUrls


def test_read_in_file():
    assert _read_in_file("./tests/examples/example3.md") == [
        "http://google.com",
        "https://youtube.com",
        "http://facebook.com https://www.ansible.com/jeff",
        "www.espn.com",
    ]


def test_populate_file_dict():
    result = _new_populate_file_dict(list(os.walk("./tests/examples/".rstrip("/"))))
    assert sorted(result.keys()) == [
        "./tests/examples/example1.md",
        "./tests/examples/example2.md",
        "./tests/examples/example3.md",
        "./tests/examples/example3.txt",
        "./tests/examples/example4.rst",
    ]
    assert len(result.keys()) == 5


def test_populate_file_dict_bad_file():
    result = _new_populate_file_dict(list(os.walk("./tests/examples/".rstrip("/"))))
    with pytest.raises(KeyError):
        result["test-file.txt"]  # pylint: disable=pointless-statement


def test_parse_single_file():
    find = FindUrls("./tests/examples/example3.md")
    result = find.find_urls()
    assert result == {
        "./tests/examples/example3.md": {
            0: ["http://google.com"],
            1: ["https://youtube.com"],
            2: ["http://facebook.com", "https://www.ansible.com/jeff"],
        }
    }


def test_parse_files_in_directory():
    find = FindUrls("./tests/examples/")
    result = find.find_urls()
    assert result == {
        "./tests/examples/example1.md": {
            2: ["https://www.google.com"],
            4: ["https://www.ansible.com"],
            6: ["https://galaxy.ansible.com"],
            8: ["https://www.ansible.com/jeff"],
            15: ["https://zigbits.tech"],
            17: ["http://resources.intenseschool.com/gns3-lab-introduction-to-dmvpn"],
        },
        "./tests/examples/example2.md": {
            2: ["https://www.readthedocs.io"],
            4: ["https://www.google.com"],
            6: ["https://www.ansible.com/jeff"],
        },
        "./tests/examples/example3.md": {
            0: ["http://google.com"],
            1: ["https://youtube.com"],
            2: ["http://facebook.com", "https://www.ansible.com/jeff"],
        },
        "./tests/examples/example3.txt": {
            1: ["http://google.com"],
            2: ["https://youtube.com"],
            3: ["http://facebook.com", "https://www.ansible.com/jeff"],
        },
        "./tests/examples/example4.rst": {21: ["http://google.com/france"], 22: ["http://google.com/japan"]},
    }


def test_no_file_directory_provided():
    with pytest.raises(ValueError, match="No File or Directory Exists with name."):
        FindUrls("t").find_urls()
