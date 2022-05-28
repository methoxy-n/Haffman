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

    codes = nodes[0].get_dict()
    print(codes)
    print(counter)
    raw_size = len(content) * 8
    compressed_size = 0
    
    for item in counter:
        compressed_size += item[1] * len(codes[item[0]])
    print(f"raw: {raw_size} compressed: {compressed_size}")
    empty_bits = (8 - compressed_size % 8) % 8
    print(empty_bits)
    
    utils.print_hashssum(content)
    
    output = open(f"{pathlib.Path(name).stem}.hfcd", "wb")
    buffer = "0" * empty_bits
    for word in content:
        buffer += codes[chr(word)]
        
    print(buffer)
    print(len(buffer))
    output.write(int(buffer, 2).to_bytes(len(buffer) // 8, byteorder='big'))
    
    if __name__ == '__main__':
