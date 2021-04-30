#!/usr/bin/env bash
set -ex
export PYTHONPATH=.
pipenv run ./scripts/validate.sh
