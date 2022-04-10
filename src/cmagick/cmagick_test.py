import subprocess
import sys


def convert(sourcefile, destinationfile):
    try:
        return subprocess.run(
            ['convert', sourcefile, destinationfile], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)


def test_convert():
    completed_process = subprocess.run(
        ['convert', 'mountain.jpg', 'blue-marble.webp'],
        stdout=subprocess.PIPE)
    assert completed_process.returncode == 0


def resize(sourcefile, size, destinationfile):
    try:
        return subprocess.run(
            ['convert', sourcefile, '-resize', size, '*', destinationfile],
            stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)


def test_resize():
    completed_process = subprocess.run(
        ['convert', 'mountain.jpg',
         '-resize', '128x128', 'mountain.jpg'],
        stdout=subprocess.PIPE)
    assert completed_process.returncode == 0
