# node class
#take slices instead of dot product
import numpy as np
class node:
    def __init__(self, data: np.ndarray, decoder: dict, G: np.ndarray):
        """
        :param data: data
        :param decoder: lookup table maybe?
        :param G: encoding matrix
        """
        self.G = G
        self.decoder = decoder
        self.coded_data = np.dot(data,G)
        #make parity check for use in syndrome decoding maybe
        k, n = G.shape
        P = G[:, k:n]
        self.H = np.concatenate((P.T, np.identity(n - k)), axis=1).astype(int)

    def query(self, w:np.ndarray):
        # return data@w.T based on decoding protocol...
        low_acc_w = self.decoder[tuple(w)] #python dict need immutable keys I just learned
        access = np.sum(np.where(low_acc_w!=0,1,0))
        if access > 2:
            print(w)
            print(low_acc_w)
            print(access)
        return self.coded_data @ low_acc_w.T, access
# test for making parity check matrix
"""data = np.random.rand(2,2)
decoder = {}
G = np.array([
    [1,0,1],
    [0,1,1]
])
test_node = node(data,decoder,G)
print(test_node.H)"""
# test is query is working alright
'''data = np.random.rand(2,2)
print(data)
G = np.array([[1,0,1], #parity code... satisfies the closed under compliment bit I think
              [0,1,1]
              ])
print(np.dot(data,G))
decoder = {
    (-1,-1): np.array([0,0,-1]),
    (-1,1):np.array([-1,1,0]),
    (1,-1):np.array([1,-1,0]),
    (1,1):np.array([0,0,1])
}# Best guess as to what the lookup table should look like...
node = node(data,decoder,G)
w = np.array([1,-1])
print(node.query(w))
print(data @ w.T)'''