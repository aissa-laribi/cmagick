import sys
import subprocess


def convert(sourcefile, destinationfile):
    try:
        return subprocess.run(
            ['convert', sourcefile, destinationfile], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)


def resize(sourcefile, size, destinationfile):
    try:
        return subprocess.run(
            ['convert', sourcefile, '-resize', size, '*', destinationfile],
            stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)


def list_formats():
    try:
        return subprocess.run(
            ['convert', '-list', 'format'], stdout=subprocess.PIPE, universal_newlines=True)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)
