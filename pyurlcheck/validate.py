"""Takes a URL and Validates a Successful HTTP Response Code."""
import requests


class ValidateUrl:
    """Validate a URL."""

    def __init__(self, url):
        """Initialize."""
        self.url = url

    def validate(self):
        """Validate a HTTP respone is not a failure."""
        resp = requests.get(self.url)
        if not resp.ok:
            return False
        return True
