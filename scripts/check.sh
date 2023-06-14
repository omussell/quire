#!/bin/sh

black --check --diff src
ruff check src
mypy src
