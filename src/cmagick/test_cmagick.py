import subprocess
import sys

from .cmagick import convert, list_formats, resize

def test_convert():
    assert convert('blue-marble.jpg', 'blue-marble.webp').returncode == 0

def test_resize():
    assert resize('blue-marble.jpg','128x128', './blue-marble.jpg').returncode == 0

def test_list_formats():
    assert list_formats().returncode == 0 


