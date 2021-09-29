#!/bin/sh

isort --check --diff src
black --check --diff src
flake8 src
mypy src