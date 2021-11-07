"""Find all URLs in File or all files in a directory."""
import logging
import os
import re
from pathlib import Path
from pyurlcheck.constants import IGNORE_DIRS


def _read_in_file(file_to_read):
    """Read contents of a file."""
    return Path(file_to_read).read_text().splitlines()


def _check_if_ignored(directory):
    """Quick check to see if the directory should be ignored."""
    for ignore in IGNORE_DIRS:
        if ignore in directory:
            return True
    return False


def _new_populate_file_dict(file_walk):
    """Take all files from a directory and create a dictionary."""
    result = {}
    for pwd, _, filename_list in file_walk:
        if not _check_if_ignored(pwd):
            for file in filename_list:
                result.update({f"{pwd}/{file}": None})
    logging.debug("Populate File Dict: %s", result)
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
    logging.debug("URL and Lines: %s", url_and_lines)
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
            file_dict = _new_populate_file_dict(list(os.walk(self.search.rstrip("/"))))
            for file in file_dict:
                results.update(_parse_file(f"{file}"))
            logging.debug("Find URLs: %s", results)
            return results
        raise ValueError("No File or Directory Exists with name.")
