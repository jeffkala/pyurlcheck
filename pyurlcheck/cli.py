"""Example cli using click."""
import click

from pyurlcheck.find import FindUrls
from pyurlcheck.check import CheckUrl
from pyurlcheck.validate import ValidateUrl


@click.command()
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
def main(file: str, directory_path: str):
    """Entrypoint into CLI app."""
    url_list = FindUrls(file)
    print(f"For {file} found the following urls:\n{url_list.find_urls()}")
    for url in url_list.find_urls():
        is_private = CheckUrl(url).is_private()
        print(f"URL is {url}")
        print(f"Is RFC1918: {is_private}")
        is_valid = ValidateUrl(url).validate()
        print(f"Is Valid: {is_valid}")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
