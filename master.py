import numpy as np
def master(m: int, data: np.ndarray):
    """
    :param m: number of instances of class node
    :param data: assume m| num cols of data, give each to a node
    :return: transposed matrix of nodes' results
    """

    # init nodes and partition data
    nodes_array = []
    width = int(data.shape[1] / m)  # number of cols of data stored at each node

    for i in range(m):
        # Sum the two columns of data and append to nodes_array
        nodes_array.append(np.sum(data[:, width * i:width * (1 + i)], axis=1))

    # Stack nodes_array vertically to form a matrix
    result_matrix = np.vstack(nodes_array)

    # Transpose the matrix
    transposed_result_matrix = result_matrix.T

    return transposed_result_matrix



