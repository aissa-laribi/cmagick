import sys
import subprocess


def convert(sourcefile, destinationfile):
    return subprocess.run(
        ['convert', sourcefile, destinationfile], stdout=subprocess.PIPE)

def resize(sourcefile, size, destinationfile):
    return subprocess.run(
        ['convert', sourcefile, '-resize', size, destinationfile], stdout=subprocess.PIPE)


def list_formats():
    return subprocess.run(
        ['convert', '-list', 'format'], stdout=subprocess.PIPE)


    
