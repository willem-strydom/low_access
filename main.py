#main
import numpy as np
from master import master
from query import query
# use hamming code for G
# maybe write general program to make lookup table for single parity
# try over actual data
# measure access
def main():
    data = np.random.rand(4,12)
    G = np.array([[1,0,1], #parity code... satisfies the closed under compliment bit I think
                  [0,1,1]
                  ])
    decoder = {
        (-1,-1): np.array([0,0,-1]),
        (-1,1):np.array([-1,1,0]),
        (1,-1):np.array([1,-1,0]),
        (1,1):np.array([0,0,1])
    }# Best guess as to what the lookup table should look like...
    m = 6
    print(data)
    nodes_array = master(m,data,decoder,G)
    w = np.array([1,1,-1,-1,-1,1,1,1,-1,-1,-1,1])
    ans = query(w,nodes_array,4) # Just tell it how many examples there are
    print(ans)
    print(np.dot(data,w))

    return 0
main()