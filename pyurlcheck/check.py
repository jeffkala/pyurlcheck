"""Check Whether URL is Public or Private."""
import socket
import ipaddress
from urllib.parse import urlparse


def _is_private(ipaddr):
    """Check if Private RFC1918."""
    return ipaddress.ip_address(ipaddr).is_private


def _get_ip(url):
    """Take a URL and execute a name lookup to retreive IP Address Object."""
    return socket.gethostbyname(url)


class CheckUrl:
    """Check URL class will be used for checks that need to be done on a URL."""

    def __init__(self, url):
        """Initialize URL Check."""
        self.url = url

    def split_url(self):
        """Take Full FQDN URL and split it into usable parts."""
        url_split = urlparse(self.url)
        return url_split

    def is_private(self):
        """Take a URL manipulate it and check if it's Private RFC1918."""
        split_url = self.split_url()
        ip_addr = _get_ip(split_url)
        return _is_private(ip_addr)
