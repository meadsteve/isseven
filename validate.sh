#!/usr/bin/env bash
set -ex
export PYTHONPATH=.
pipenv run pytest tests --hypothesis-show-statistics
pipenv run mypy --config-file mypy.ini isseven tests
pipenv run black --check isseven tests
