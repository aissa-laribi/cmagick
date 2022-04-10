# cmagick

![GitHub](https://img.shields.io/github/license/aissa-laribi/cmagick)
[![cmagick CI](https://github.com/aissa-laribi/cmagick/actions/workflows/python-app.yml/badge.svg)](https://github.com/aissa-laribi/cmagick/actions/workflows/python-app.yml)
![PyPI](https://img.shields.io/pypi/v/cmagick?color=blue)

Cmagigk is a <a href="https://docs.python.org/3.8/library/subprocess.html">subprocess-based</a> simple <a href ="https://www.imagemagick.org/">ImageMagick</a> interaction for Python, supporting Python 3.8+ and Linux distributions. The functionalities of ImageMagick to convert to the following formats (bmp,eps,gif,tiff,webp,wbmp,tga,png,jpg,jpeg,hdr,exr), and resize pictures are implemented in cmagick.

## Usage

Examples:
```
from cmagick import cmagick

convert('website.jpg','website.webp')
```
```
from cmagick import cmagick

resize('website.jpg','100x100','website.jpg')
```
## Prerequisites

Python 3.8

imagemagick for apt Debian/Ubuntu
ImageMagick for yum RPM

## Installation 

You can install the package from PyPI:
```
pip install cmagick
```
You can install the package the GitHub repository:
```
$ git clone git://github.com/aissa-laribi/cmagick.git
$ cd cmagick/
$ python3 setup.py install --user
```
## To Uninstall
```
$ pip uninstall cmagick
```
