#main
import numpy as np
from master import master
from query import query
def main():
    data = np.random.rand(4,6)
    G = np.array([[1,0,1], #parity code... satisfies the closed under compliment bit I think
                  [0,1,1]
                  ])
    decoder = {
        (-1,-1): np.array([0,0,-1]),
        (-1,1):np.array([-1,1,0]),
        (1,-1):np.array([1,-1,0]),
        (1,1):np.array([0,0,1])
    }# Best guess as to what the lookup table should look like...
    m = 3
    print(data)
    nodes_array = master(m,data,decoder,G)
    w = np.array([1,1,-1,-1,-1,1])
    ans = query(w,nodes_array,4) # Just tell it how many examples there are
    print(ans)
    print(np.dot(data,w))
    print(data[:, 0:2])
    print(data[:, 2:4])

    return 0
main()