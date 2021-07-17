"""Find all URLs in File or all files in a directory."""
import os
import re
from pathlib import Path


def _read_in_file(file_to_read):
    """Read contents of a file."""
    return Path(file_to_read).read_text().splitlines()


def _populate_file_dict(file_list):
    """Take all files from a directory and create a dictionary."""
    result = {}
    for file in file_list:
        result.update({f"{file}": None})
    return result


def _parse_file(filepath):
    """Read in a file with enumerates to have line numbers.

    Args:
        filepath (str): path to the file

    Returns:
        dict: dictionary of filepath to urls and lines.
    """
    file_data = _read_in_file(filepath)
    url_and_lines = {}
    for line_number, line_content in enumerate(file_data):
        urls_found = re.findall(r"https?:\/{2}\S+\b", line_content)
        if len(urls_found) > 0:
            url_and_lines.update({line_number: urls_found})
    return {filepath: url_and_lines}


class FindUrls:
    """Class to take in a file or directory and return all URLs from the files."""

    def __init__(self, search):
        """Initialize Find URL class."""
        self.search = search

    def find_urls(self):
        """Find all urls from all files."""
        results = {}
        if os.path.isfile(self.search):
            results.update(_parse_file(self.search))
            return results
        if os.path.isdir(self.search):
            file_dict = _populate_file_dict(os.listdir(self.search))
            for file in file_dict:
                results.update(_parse_file(f"{self.search}{file}"))
            return results
        raise ValueError("No File or Directory Provided.")
