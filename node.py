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
        self.data = np.dot(data,G)

    def query(self, w:np.ndarray):
        # return w.T@data based on decoding protocol... idek what that is
        low_acc_w = self.decoder[w] #how this would actually work idek
        return np.dot(low_acc_w, self.data)

