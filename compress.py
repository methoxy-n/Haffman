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
    counter = {}
    for letter in content:
        if counter.get(chr(letter)) is None:
            counter[chr(letter)] = 1
        else:
            counter[chr(letter)] += 1
    counter = sorted(counter.items(),key = lambda x: x[1])

    nodes = []
    for item in counter:
        nodes.append(BinaryNode(content = item[0], prob = item[1]))

    while len(nodes) > 1:

        left = nodes[0]
        right = nodes[1]
        right.code = 0
        left.code = 1
        new_node = BinaryNode(prob = left.prob + right.prob, content = right.content + left.content, left=left, right=right)
        nodes.remove(right)
        nodes.remove(left)
        nodes.append(new_node)
        nodes = sorted(nodes, key = lambda x: x.prob)

    print(nodes[0].get_dict())
    
    utils.print_hashssum(content)
    
    if __name__ == '__main__':
