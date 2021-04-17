import re
from pathlib import Path

class FindUrls:

    def __init__(self, file=None):
        self.file = file

    def _read_in_file(self):
        return Path(self.file).read_text()

    def find_urls(self):
        data = self._read_in_file()
        return list(re.findall("https.*\w", data))

