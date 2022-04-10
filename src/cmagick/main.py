def main():
    from cmagick import convert, resize, list_formats
    sourcefile = input()
    destinationfile = input()
    size = input()
    convert = convert.convert(sourcefile, destinationfile)
    resize = resize.convert(sourcefile, size, destinationfile)
    list_formats()
