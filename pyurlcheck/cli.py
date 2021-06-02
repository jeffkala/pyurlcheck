"""Example cli using click."""
import sys

import click

from pyurlcheck.check import CheckUrl
from pyurlcheck.find import FindUrls
from pyurlcheck.validate import ValidateUrl


@click.command()
@click.argument(
    "input_data",
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    required=True
    )
def main(input_data):
    """Entry point into the pyurlcheck command line tool.

    Args:
        input_data (str) - Either filename or directory to search for URLs.
    """
    results = []
    files_urls = FindUrls(input_data).find_urls()
    for file_name, url_list in files_urls.items():
        for line_num, urls in url_list.items():
            for url in urls:
                url_details = CheckUrl(url).split_url()
                if url_details.scheme == '':
                    is_valid = ValidateUrl(url, need_scheme=True).validate()
                # print(f"URL is {url}")
                # print(f"Is RFC1918: {is_private}")
                else:
                    is_valid = ValidateUrl(url).validate()
                if not is_valid:
                    results.append(f"{file_name}:{line_num + 1}\tURL Issue: {url}")
    if len(results) > 0:
        print('\n'.join(results))
        sys.exit(len(results))
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
