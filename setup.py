# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def get_version():
    with open("geezer/version.py") as f:
        for line in f:
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Version not found.")

setup(
    name='geezer',
    version=get_version(),
    packages=find_packages(),
    description='Old-school debug logging for stylish devs',
    author='Ben McNelly',
    include_package_data=True,
    zip_safe=False,
    install_requires=["rich"],
    long_description = open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
