# Contributing

## Branches

- `main` - Reserved for current release
- `develop` - Ready to release code, bases for new PRs
- `<feature>` - Individual feature branches, should be PR'd to `develop`.

## Python Versions

This leverages Python3.6 or later. All features will be tested against 3.6 - 3.9 versions of Python.

## Versioning

This project utilizes Semver versioning. As part of PRs the maintainers should leverage Poetry versioning to support the increase in version numbers. Reference [Poetry Version Docs](https://python-poetry.org/docs/cli/#version) for more information on automatically adjusting the version.  

## Installing dependencies for local development

> These steps are also required for using the examples as provided in the repository for demonstration purposes.  

This repository uses [poetry](https://python-poetry.org/) for dependency management.

Follow these steps to set up your local development environment:

```bash
# Double check your version
$ python --version
Python 3.7.7
# Activate the Poetry environment, which will auto create the virtual environment related to the project
$ poetry shell
# Install project dependencies as well as development dependencies
$ poetry install
```

## Testing

All tests should be located within the `tests\` directory with `tests\unit` for the unit tests. Integration tests should be in the `tests\integration` directory.

### Testing - Required

The following linting tasks are required:

* [Bandit](https://bandit.readthedocs.io/en/latest/)
  * Basic security tests, should be run on Python3.6 or Python3.7
* [Black code style](https://github.com/psf/black)
  * Code formatting with version 20.8b1. There are some differences in the format between versions 19 and 20.
* [Flake8](https://flake8.pycqa.org/en/latest/)
  * Black vs Flake conflicts: When conflicts arise between Black and Flake8, Black should win and Flake8 should be configured as such
* [Pydocstyle](https://github.com/PyCQA/pydocstyle/)
* [Pylint](https://www.pylint.org)
* [Yamllint](https://yamllint.readthedocs.io)
