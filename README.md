# Action Test

[![GitHub Super-Linter](https://github.com/costaTest/actions-test/actions/workflows/actions-test.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Flake-8](https://github.com/costaTest/actions-test/actions/workflows/flake8-lint.yml/badge.svg)](https://github.com/marketplace/actions/flake8-action)
[![Pytest](https://github.com/costaTest/actions-test/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/marketplace/actions/run-pytest)
[![codecov](https://codecov.io/github/costaTest/actions-test/branch/main/graph/badge.svg?token=A26SGXCUX0)](https://codecov.io/github/costaTest/actions-test)

Testing GitHub Actions

## Super Linter

[Run Super-Linter Locally](https://github.com/github/super-linter/blob/main/docs/run-linter-locally.md)

```bash
docker pull github/super-linter:latest
docker run -e RUN_LOCAL=true -v $PWD:/tmp/lint github/super-linter
```

## Flake8 Linter

To run locally, install flake8.

```bash
python3 -m flake8
```

## PyTest

To run locally, install pytest and run pytest.

```bash
python3 -m pytest
```

## PyTest Code Coverage

To run locally:
```bash
python -m pytest
coverage run -m pytest
coverage report
```
