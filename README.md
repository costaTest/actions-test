# actions-test

[![GitHub Super-Linter](https://github.com/costaTest/actions-test/actions/workflows/actions-test.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)

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
