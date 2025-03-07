from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = {}
with open("graphix_ibmq/version.py") as fp:
    exec(fp.read(), version)

requirements = [requirement.strip() for requirement in open("requirements.txt").readlines()]

info = {
    "name": "graphix_ibmq",
    "version": version["__version__"],
    "packages": find_packages(),
    "author": "Daichi Sasaki, Shinichi Sunami",
    "author_email": "shinichi.sunami@gmail.com",
    "maintainer": "Daichi Sasaki, Shinichi Sunami",
    "maintainer_email": "shinichi.sunami@gmail.com",
    "license": "Apache License 2.0",
    "description": "IBMQ interface for graphix library, the MBQC compiler ",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://graphix.readthedocs.io",
    "project_urls": {"Bug Tracker": "https://github.com/TeamGraphix/graphix-ibmq/issues"},
    "classifiers": [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    "python_requires": ">=3.8,<3.12",
    "install_requires": requirements,
    "extras_require": {"test": ["graphix==0.2.8"]},
}

setup(**(info))
