#!/usr/bin/env python3
"""
Setup script for PySNT.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

# Read version from package
version_path = Path(__file__).parent / "src" / "pysnt" / "__init__.py"
version = "0.0.1"  # Default fallback
if version_path.exists():
    for line in version_path.read_text().splitlines():
        if line.startswith("__version__"):
            version = line.split('"')[1]
            break

setup(
    name="pysnt",
    version=version,
    author="SNT contributors",
    author_email="",
    description="Python interface for SNT, the ImageJ framework for neuroanatomy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/morphonets/pysnt",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "scyjava>=1.8.0",
        "pyimagej>=1.4.0",
        "numpy>=1.20.0",
        "install-jdk>=1.1.0",  # For automatic Java installation
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-design",
            "myst-nb",
            "sphinx-copybutton",
            "pydata-sphinx-theme",
        ],
    },
    entry_points={
        "console_scripts": [
            "pysnt=pysnt.__main__:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)