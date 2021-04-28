#!/usr/bin/env bash
set -ex
export PYTHONPATH=.
pytest tests --hypothesis-show-statistics
mypy --config-file mypy.ini isseven tests
black --check isseven tests
