#!/usr/bin/env bash
set -ex

python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
python3 -m build
python3 -m twine upload -r pypi dist/* --verbose
