Cmagick

license|MIT build|passing python|3.8 rpm|passing dpkg|passing 

Cmagigk is a subprocess-based simple ImageMagick interaction for Python, supporting Python 3.8+, PyPy, and rpm-based Linux distributions. The functionalities of ImageMagick to convert to the following formats (bmp,eps,gif,tiff,webp,wbmp,tga,png,jpg,jpeg,hdr,exr), and resize pictures are implemented in cmagick.

## Usage

Examples:

from cmagick import cmagick

convert('website.jpg','website.webp')

from cmagick import cmagick

resize('website.jpg','100x100','website.jpg')

## Prerequisites

Python 3.8

imagemagick for apt Debian/Ubuntu
ImageMagick for yum RPM

## Installation 

You can install the package from Github by using pip:

$ pip install https://github.com/aissa-laribi/cmagick/dist/cmagick-0.0.1-py3-none-any.whl

Or check source code from the GitHub repository:

$ git clone git://github.com/aissa-laribi/cmagick.git
$ cd cmagick/
$ python3 setup.py install