"""Find all URLs in File or all files in a directory."""
import enum
import os
import re
from pathlib import Path


class FindUrls:
    """Class to take in a file or directory and return all URLs from the files."""

    def __init__(self, search):
        """Initialize Find URL class."""
        self.search = search

    def _read_in_file(self, file_to_read):
        """Read contents of a file."""
        return Path(file_to_read).read_text().splitlines()

    def _populate_file_dict(self, file_list):
        """Take all files from a directory and create a dictionary."""
        result = {}
        for file in file_list:
            result.update({f"{file}": None})
        return result

    def _parse_file(self, filepath):
        file_data = self._read_in_file(filepath)
        url_and_lines = {}
        for line_number, line_content in enumerate(file_data):
            urls_found = re.findall(r"https?:\/{2}\S+\b", line_content)
            if len(urls_found) > 0:
                url_and_lines.update({line_number: urls_found})
        return {filepath: url_and_lines}

    def find_urls(self):
        """Find all urls from all files."""
        results = {}
        if os.path.isfile(self.search):
            results.update(self._parse_file(self.search))
            return results
        elif os.path.isdir(self.search):
            file_dict = self._populate_file_dict(os.listdir(self.search))
            for file in file_dict:
                results.update(self._parse_file(f"{self.search}{file}"))
            return results
        else:
            raise ValueError("No File or Directory Provided.")
