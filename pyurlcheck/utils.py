"""Helpers for pyurlcheck."""


def redirect_mapper(url_result):
    """Take the request .history and normalize the output.

    Args:
        url_result (requests response): requests library response
    """
    return [redirect.headers["Location"] for redirect in url_result.history]
