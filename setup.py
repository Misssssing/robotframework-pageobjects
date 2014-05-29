#!/usr/bin/env python

import os
from setuptools import setup, find_packages
import subprocess
import shlex

reqs = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                    'requirements.txt')
REQUIRES = filter(None, open(reqs).read().splitlines())


# Listing inflection module as requirements is not working in windows for some
# reason. So install it using pip install.

setup(
    name="Robot-Framework-Page-Objects",
    version="0.3.1",
    description="Lets you use the page object pattern with Robot Framework and plain python", 
    author="National Center for Biotechnology Information",
    install_requires=REQUIRES,
    packages=find_packages(exclude=("tests",)),
    zip_safe=False
)
