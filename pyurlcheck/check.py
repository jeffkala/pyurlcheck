"""Check Whether URL is Public or Private."""
import logging
import ipaddress
from urllib.parse import urlparse
from dns import resolver


def split_url(url):
    """Parses the URL into usable parts.

    Args:
        url (str): Exact URL found from the regex.

    Returns:
        ParseResult: Includes scheme, netloc, path, params, query, fragments.
    """
    url_split = urlparse(url)
    logging.debug("URL Split: %s", url_split)
    return url_split


def get_ip(domain):
    """Take a URL and execute a name lookup to retreive IP Address Object.

    Args:
        domain (str): URL from netloc in parse.

    Returns:
        str: IP Address
    """
    result = resolver.resolve(domain, "A")
    logging.debug("DNS Resolver: %s", result[0])
    return result[0].address


def is_private(ip_addr):
    """Take a URL manipulate it and check if it's Private RFC1918.

    Args:
        ip (str): IP address from the dns resolution.

    Returns:
        Boolean: True/False whether address is RFC1918 space.
    """
    return ipaddress.ip_address(ip_addr).is_private
