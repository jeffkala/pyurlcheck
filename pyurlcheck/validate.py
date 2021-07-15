"""Takes a URL and Validates a Successful HTTP Response Code."""
import requests


# suppresses invalid cert warnings, deprecated..., using verify=False
requests.packages.urllib3.disable_warnings()


class ValidateUrl:
    """Validate a URL."""

    def __init__(self, url, need_scheme=False):
        """Initialize."""
        self.url = url
        self.need_scheme = need_scheme

    def validate(self):
        """Validate a HTTP respone is not a failure."""
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        if self.need_scheme:
            resp = requests.get(f"http://{self.url}", headers=headers, verify=False)
        else:
            resp = requests.get(self.url, headers=headers, verify=False)
        if not resp.ok:
            return False
        return True
