
"""Example cli using click."""
import click

from pyurlcheck.find import FindUrls
from pyurlcheck.check import CheckUrl
from pyurlcheck.validate import ValidateUrl


@click.option(
    "-f",
    "--file",
    "file",
    help="File to Validate URLs.",
    type=str,
)
@click.option(
    "-d",
    "--directory",
    "directory_path",
    help="Directory, all files will be validated.",
    type=str,
)
def main(file:str, directory_path:str):
    """Entrypoint into CLI app."""
    url_list = FindUrls(file)
    print(url_list)
    for u in url_list:
        if not CheckUrl(u):
            print(ValidateUrl(u))

if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
