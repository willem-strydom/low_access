import numpy as np
def query(w, nodes_array):
    """
    :param w: query on RAW data
    :param nodes_array: the storage nodes from master
    :return: np.dot(w,data) but like with low access
    """
    m = len(nodes_array)
    width = nodes_array[0].data.shape[1] #get number of cols of RAW data in a node
    # partition w and do a query
    ans_array = np.zeros(m)
    for i in range(m):
        ans_array[i] = nodes_array[i].query(w[i:i*(width+1)])
