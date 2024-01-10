#main
import numpy as np
from master import master
from query import query
from G_matrix import G_matrix
from decoder import decoder

# use hamming code for G
# maybe write general program to make lookup table for single parity
# try over actual data
# measure access
def main():
    data = np.genfromtxt("framingham_cleaned_file.csv", dtype=float, comments='#', delimiter=",", skip_header=1)
    a = np.eye(3)
    b = np.ones((3,1))
    G = np.hstack((a,b))
    from decoder import decoder
    decoder = decoder(3)
    data = np.hstack((data,np.zeros((data.shape[0],2)))) # need m|data.shape[1] = num cols
    m = 6
    w = np.random.choice([-1, 1], data.shape[1])
    nodes_array = master(m, data, decoder, G, w)
    print(np.dot(data, w))
    return 0
main()

def hamming():
    data = np.genfromtxt("framingham_cleaned_file.csv", dtype=float, comments='#', delimiter=",", skip_header=1)
    G = G_matrix(3)
    from decoder import decoder
    decoder = {
        (1, 1, 1): np.array([0, 0, 0, 0, 0, 0, 1]),
        (1, 1, -1): np.array([0, 0, -2, 0, 0, 0, 1]),
        (1, -1, 1): np.array([0, -2, 0, 0, 0, 0, 1]),
        (-1, 1, 1): np.array([-2, 0, 0, 0, 0, 0, 1]),
        (1, -1, -1): np.array([2, 0, 0, 0, 0, 0, -1]),
        (-1, 1, -1): np.array([0, 2, 0, 0, 0, 0, -1]),
        (-1, -1, 1): np.array([0, 0, 2, 0, 0, 0, -1]),
        (-1,-1,-1):np.array([0, 0, 0, 0, 0, 0, -1])
    } # not yet automated
    data = np.hstack((data, np.zeros((data.shape[0], 2))))  # need m|data.shape[1] = num cols
    m = 6
    w = np.random.choice([-1, 1], data.shape[1])
    nodes_array = master(m, data, decoder, G, w)
    print(np.dot(data, w))

    return 0
hamming()
