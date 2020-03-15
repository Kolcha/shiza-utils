#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="shiza-utils",
    version="0.1.0",
    packages=setuptools.find_packages(),
    install_requires=['lxml', 'requests'],
    python_requires='>=3',
)
