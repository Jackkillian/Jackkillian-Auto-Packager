"""Created with Jackkillian Auto Packager. To install: pip install JackkillianAutoPackager"""
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JackkillianAutoPackager",
    version="1.0.0",
    author="jackkillian",
    description="Upload projects to pip with ease!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="github.com/Jackkillian/Jackkillian-Auto-Packager",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3", "Development Status :: 5 - Production/Stable ", "License :: OSI Approved :: MIT License ", "Operating System :: OS Independent"])
