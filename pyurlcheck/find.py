"""Find all URLs in File or all files in a directory."""
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
        return Path(file_to_read).read_text()

    def _populate_file_dict(self, file_list):
        """Take all files from a directory and create a dictionary."""
        result = {}
        for file in file_list:
            result.update({f"{file}": None})
        return result

    def find_urls(self):
        """Find all urls from all files."""
        if os.path.isfile(self.search):
            file_data = self._read_in_file(self.search)
            return {self.search: list(re.findall(r"https.*\w", file_data))}
        elif os.path.isdir(self.search):
            file_dict = self._populate_file_dict(os.listdir(self.search))
            for file in file_dict:
                data = self._read_in_file(f"{self.search}{file}")
                file_dict[file] = list(re.findall(r"https.*\w", data))
            return file_dict
        else:
            raise ValueError("No File or Directory Provided.")
