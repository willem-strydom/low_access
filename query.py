import numpy as np
def query(w, nodes_array,n):
    """
    :param w: query on RAW data
    :param nodes_array: the storage nodes from master
    :return: np.dot(w,data) but like with low access
    """
    m = len(nodes_array)
    width = nodes_array[0].G.shape[0] # size of raw data at each node is needed to partition w. assume systematic G
    # partition w and do a query
    ans_array = np.zeros((n,m))
    for i in range(m):
        ans_array[:,i] = nodes_array[i].query(w[i:width+i])
    return np.sum(ans_array, axis = 1) # add the responses together, i think sum them as columns is axis = 1 ...
