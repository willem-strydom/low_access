# node class
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

    def query(self, w:np.ndarray):
        # return data@w.T based on decoding protocol... idek what that is
        low_acc_w = self.decoder # python dict need imutable keys i just learned
        print(self.coded_data)
        return self.coded_data @ low_acc_w.T

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