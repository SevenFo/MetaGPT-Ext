#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup file for the metagpt-provider-ark package.
"""

import os
from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="metagpt-provider-ark",
    version="0.1.0",
    description="MetaGPT Provider for Volcengine Ark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="MetaGPT Team",
    author_email="metagpt@deepwisdom.ai",
    url="https://github.com/metagpt-ext/provider/metagpt-provider-ark",
    packages=find_namespace_packages(include=["metagpt.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
)
