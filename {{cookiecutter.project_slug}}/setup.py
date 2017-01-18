# -*- coding: utf-8 -*-
"""setuptools control."""

import re

from setuptools import setup


def get_version():
    """Return __version__ value from main source file."""
    with open("{{cookiecutter.project_slug}}/__init__.py") as source:
        version = re.search(r"^__version__\s*=\s*'(.*)'",
                            source.read(),
                            re.M).group(1)
    return version


def get_description():
    """Return long description from README."""
    with open("README.rst", "rb") as readme:
        long_description = readme.read().decode("utf-8")
    return long_description


setup(
    name="{{cookiecutter.project_slug}}",
    packages=["{{cookiecutter.project_slug}}"],
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}.__main__:main"
        ]
    },
    version=get_version(),
    description="{{cookiecutter.project_short_description}}",
    long_description=get_description(),
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    url="https://gitlab.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}",
    install_requires=["future"],
    setup_requires=[]
)
