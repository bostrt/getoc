#!/usr/bin/env python3
from setuptools import setup, find_packages
from getoc.version import __version__

setup(
    name="getoc",
    version=__version__,
    packages=find_packages(),
    author="bostrt",
    entry_points={
        "console_scripts": ["getoc=getoc.client:cli"]
    },
    description="Helper tool for acquiring any version OpenShift Client",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="",
    url="https://github.com/bostrt/getoc",
    install_requires=[
        "click",
        "terminaltables",
        "pick",
        "htmllistparse",
        "tqdm",
    ],
)
