#!/usr/bin/env python3
"""
Setup script for Gantt Chart Generator
"""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Professional Gantt Chart Generator"

# Read requirements
def read_requirements():
    try:
        with open("requirements.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        return ["beautifulsoup4>=4.9.0", "lxml>=4.6.0"]

setup(
    name="gantt-chart-generator",
    version="1.0.0",
    author="Gantt Chart Generator Team",
    author_email="contact@example.com",
    description="Professional Gantt chart generator with HTML output",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/gantt-chart-generator",
    packages=find_packages(),
    package_data={
        "": [
            "templates/*.html",
            "locale/*.json",
            "examples/*.json",
            "docs/*.md"
        ]
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Software Development :: Documentation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "gantt-generator=src.gantt_generator:main",
            "gantt-extractor=src.gantt_extractor:main",
        ],
    },
    keywords="gantt chart project management timeline visualization html",
    project_urls={
        "Bug Reports": "https://github.com/your-username/gantt-chart-generator/issues",
        "Source": "https://github.com/your-username/gantt-chart-generator",
        "Documentation": "https://github.com/your-username/gantt-chart-generator/wiki",
    },
)
