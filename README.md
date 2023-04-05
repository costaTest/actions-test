# actions-test

[![GitHub Super-Linter](https://github.com/costaTest/actions-test/actions/workflows/actions-test.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)

Testing GitHub Actions

[Run Super-Linter Locally](https://github.com/github/super-linter/blob/main/docs/run-linter-locally.md)

```bash
docker pull github/super-linter:latest
docker run -e RUN_LOCAL=true -v $PWD:/tmp/lint github/super-linter
```
