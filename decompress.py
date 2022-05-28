import utils
import pathlib
import sys

def decompress():
    try:
        name = sys.argv[1]
        raw = open(name, "rb")
    except IndexError:
        print("Choose file you want to decompress")
        exit()
    if pathlib.Path(name).suffix != ".hfcd":
        print("File is not compressed yet")
        exit()
    content = raw.read()
    utils.print_hashsum(content)

    if __name__ == '__main__':
    decompress()
