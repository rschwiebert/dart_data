import os
import sys
import site
from setuptools import setup, find_packages
from pathlib import Path


FULL_PACKAGE_DIR = site.getsitepackages()[0]
RELATIVE_PACKAGE_DIR = str(Path(FULL_PACKAGE_DIR).relative_to(Path(sys.prefix)))


def get_templates():
    return [str(path) for path in Path().rglob("*.html")] + [str(path) for path in Path().rglob("*.csv")]


setup(
    name="dart_data",
    version="0.0.1",
    author="Ryan C. Schwiebert",
    description="Data files for the Database of Ring Theory",
    url="https://github.com/rschwiebert/RingApp",
    packages=find_packages(),
    data_files=[
        (
            os.path.join(RELATIVE_PACKAGE_DIR, "dart_data/templates/dart_data"),
            get_templates(),
        )
    ],
    keywords=['mathematics', 'ring theory', 'education', 'research'],
)
