# ft_package

This is a simple Python package that counts occurrences of an item in a list.
Step 1: Project Structure
Create this structure:

arduino
ex09/
│
├── ft_package/
│   ├── __init__.py
│   └── count.py
│
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.cfg
├── setup.py
└── MANIFEST.in
Step 2: Code the function
ft_package/count.py

def count_in_list(lst, item):
    return lst.count(item)
ft_package/__init__.py

from .count import count_in_list
Step 3: README.md
md
# ft_package

This is a simple Python package that counts occurrences of an item in a list.
Step 4: LICENSE
Use MIT license (you can copy from: https://opensource.org/licenses/MIT)

Step 5: setup.py
from setuptools import setup

setup()
Step 6: setup.cfg
ini
[metadata]
name = ft_package
version = 0.0.1
author = eagle
author_email = eagle@42.fr
description = A sample test package
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/eagle/ft_package
license = MIT
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
packages = find:
python_requires = >=3.6
Step 7: pyproject.toml
toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
Step 8: MANIFEST.in
txt
include README.md
include LICENSE
Step 9: Build the package
From inside the ex09/ directory, run:

bash
python3 -m pip install --upgrade build
python3 -m build
This creates:

pgsql
dist/
├── ft_package-0.0.1.tar.gz
└── ft_package-0.0.1-py3-none-any.whl
Step 10: Install the package
bash
pip install ./dist/ft_package-0.0.1.tar.gz
# OR
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
Step 11: Test it
Create a test.py:

from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # ➜ 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # ➜ 0
Step 12: Verify with pip
bash
pip show -v ft_package
Should show:

makefile
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
...