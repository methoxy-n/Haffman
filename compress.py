import utils
from utils import BinaryNode
import pathlib
import sys

def compress():
    try:
        name=sys.argv[1]
        raw=open(name,"rb")
    except IndexError:
        print("Choose file you want to compress")
        exit()
    if pathlib.Path(name).suffix == ".hfcd"
        print("File compressed")
        exit()
    content = raw.read()
