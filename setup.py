#!/usr/bin/env python

from setuptools import setup, find_packages
import os

# read the contents of your README file
this_directory = os.path.dirname(__file__)
long_description = open(os.path.join(this_directory, "README.md"), "r").read()

install_requires = []

setup(
    name="kashida",
    version="1.0.1",  # .post1
    description="",
    author="Yanone",
    author_email="post@yanone.de",
    url="https://github.com/yanone/kashida",
    install_requires=install_requires,
    package_dir={"": "Lib"},
    packages=find_packages("Lib"),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
