"""Takes a URL and Validates a Successful HTTP Response Code."""
import logging

import requests

from pyurlcheck.utils import redirect_mapper


# suppresses invalid cert warnings, deprecated..., using verify=False
requests.packages.urllib3.disable_warnings()  # pylint:disable=no-member


class ValidateUrl:
    """Validate a URL."""

    def __init__(self, url, need_scheme=False):
        """Initialize."""
        self.url = url
        self.need_scheme = need_scheme

    def validate(self):
        """Validate a HTTP respone is not a failure."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        }
        if self.need_scheme:
            logging.debug("No scheme was provided, using http. For %s", self.url)
            resp = requests.get(f"http://{self.url}", headers=headers, verify=False)  # nosec
        else:
            resp = requests.get(self.url, headers=headers, verify=False)  # nosec
        if len(resp.history) > 0:
            has_redirect = redirect_mapper(resp)
            logging.debug("Redirects: %s", has_redirect)
        else:
            has_redirect = []
        if not resp.ok:
            return False, has_redirect
        return True, has_redirect
