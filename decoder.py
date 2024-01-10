import numpy as np

def G_matrix(m,data):
    n,k = data.shape
    '''n is data row number
       k is data column number
       m is the nodes number
    '''
    unit_matrix = np.eye(m, m)
    ones_column = np.ones((m, 1))
    
    result_matrix = np.hstack((unit_matrix, ones_column))
    
    return result_matrix
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
