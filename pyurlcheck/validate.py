"""Takes a URL and Validates a Successful HTTP Response Code."""
import requests


class ValidateUrl:
    """Validate a URL."""

    def __init__(self, url, need_scheme=False):
        """Initialize."""
        self.url = url
        self.need_scheme = need_scheme

    def validate(self):
        """Validate a HTTP respone is not a failure."""
        if self.need_scheme:
            resp = requests.get(f"http://{self.url}")
        else:
            resp = requests.get(self.url)
        if not resp.ok:
            return False
        return True
