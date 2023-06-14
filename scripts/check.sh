#!/bin/sh

black --check --diff quire.py
ruff check quire.py
mypy quire.py
