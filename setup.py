#!/usr/bin/env python

# BS'D
# created by aareman
# 2019

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gif-me-loader",
    version="0.0.1",
    author="aareman",
    author_email="aareman000@citymail.cuny.edu",
    description="A simple package for adding loading bars to GIFS",
    url="https://github.com/aareman/gif-me-loader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
        'setuptools',
        'sys',
        'argparse',
        'Pillow'
    ],
    scripts=['bin/gif-me-loader'],
)
