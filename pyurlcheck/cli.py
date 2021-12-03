"""Example cli using click."""
import logging
import sys

import click

from pyurlcheck.check import split_url, get_ip, is_private
from pyurlcheck.find import FindUrls
from pyurlcheck.validate import ValidateUrl


LOGGER = logging.getLogger(__name__)


@click.command()
@click.argument("input_data", type=click.Path(exists=True, file_okay=True, dir_okay=True), required=True)
@click.option("--log_level", type=click.Choice(["INFO", "DEBUG"], case_sensitive=False), default="INFO")
def main(input_data, log_level):
    """Entry point into the pyurlcheck command line tool.

    Args:
        input_data (str): Either filename or directory to search for URLs.
        log_level (str): Logging level to execute with. Choices ['INFO', 'DEBUG']. Default is INFO.
    """
    logging.basicConfig(format="%(asctime)s %(message)s", stream=sys.stdout, level=getattr(logging, log_level))
    results = []
    files_urls = FindUrls(input_data).find_urls()
    for file_name, url_list in files_urls.items():
        for line_num, urls in url_list.items():
            for url in urls:
                url_details = split_url(url)
                # RFC 1918 Check, if True don't validate.
                if not is_private(get_ip(url_details.netloc)):
                    if url_details.scheme == "":
                        is_valid, has_redirects = ValidateUrl(url, need_scheme=True).validate()
                    else:
                        is_valid, has_redirects = ValidateUrl(url).validate()
                    if not is_valid:
                        results.append(f"{file_name}:{line_num + 1}\tURL Issue: {url}")
                    if has_redirects:
                        LOGGER.info(
                            "Redirect_Warning: %s had redirects while executing. Redirects are ' => '.join(%s)!",
                            url,
                            has_redirects,
                        )
    if len(results) > 0:
        LOGGER.info("\n".join(results))
        sys.exit(len(results))
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
