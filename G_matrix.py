import numpy as np

def G_matrix(m):
    """
    make generator matrix for hamming code
    :param m: dimension of code/number of feature stored at each node
    :return: hamming code generator matrix "G"
    """

    # Total number of vectors is 2^m - 1 (excluding the zero vector, systematic vectors not in order...)
    total_vectors = 2 ** m - 1

    matrix = np.zeros((m, total_vectors), dtype=int)

    # Fill the matrix with binary representations of numbers from 1 to total_vectors, hence bad order
    for i in range(1, total_vectors + 1):
        binary_representation = np.array(list(np.binary_repr(i, width=m)), dtype=int)
        matrix[:, i - 1] = binary_representation[::-1]  # Reverse to match column format
    # make G of the form [I|P]
    if m > 2:
        for i in range(2,m):

            temp = matrix[:,-1 + 2**i].copy() # placeholder for swapping
            matrix[:,-1 + 2**i] = matrix[:,i]
            matrix[:, i] = temp

    return matrix
def decoder(data,w):
    n,m = data.shape
    '''w is the input w 
       m is data column number 
    '''
    decode = []
    
    if np.all(w == 1):
        decode = m * [0]
        decode.append(1)
    elif np.all(w == -1):
        decode = m * [0]
        decode.append(-1)
    else:
        decode = list(w)  
        decode.append(0)
    decode_matrix = np.array([decode])

    return decode_matrix
