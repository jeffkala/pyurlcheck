from pyurlcheck.validate import ValidateUrl


def test_validate_url_good_with_schema():
    validate = ValidateUrl("https://www.google.com")
    assert validate.validate() is True


def test_validate_url_good_without_schema():
    validate = ValidateUrl("www.google.com", need_scheme=True)
    assert validate.validate() is True


def test_validate_url_bad_with_schema():
    validate = ValidateUrl("https://www.google.com/fake")
    assert validate.validate() is False


def test_validate_url_bad_without_schema():
    validate = ValidateUrl("www.google.com/fake", need_scheme=True)
    assert validate.validate() is False
