#main
import numpy as np
from master import master
from query import query
from decoder import decoder, G_matrix
from node import node
# use hamming code for G
# maybe write general program to make lookup table for single parity
# try over actual data
# measure access
def main():
    data = np.random.rand(4,12)
    m = 6
    w = np.random.choice([1, -1], size=int(m))
    G = G_matrix(m,data)
    print(G)
    decode = decoder(data,w)
    # Best guess as to what the lookup table should look like...
    print(decode)
    nodes_array = master(m,data)
    print(nodes_array)
    node_result = node(nodes_array, decode, G)
    print(print(node_result.query(w)))

    return 0
main()