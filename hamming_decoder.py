import numpy as np
def hamming_decoder(G):
    """
    Param: G: non-systematic generator matrix of code, should be transposed though
    :return: lookup table for "hamming" code... should work for any code tho
    """
    all_combinations = np.array(np.meshgrid(*[[-1, 1]] * 7)).T.reshape(-1, 7)  # vectors in rows
    lookup_table = {}
    for v in all_combinations:
        best = 7 # maximum hamming distance between v and g
        best_code = 0
        best_ind = 0
        sign = 0
        for i,g in enumerate(G):
            dummy = np.where(v != g, 1, 0)
            dist = np.sum(dummy)

            if dist < best:
                best = dist
                best_code = g
                best_ind = i
                sign = 1
            dummy = np.where(-v != g, 1, 0)
            dist = np.sum(dummy)
            if dist < best:
                best = dist
                best_code = -g
                best_ind = i
                sign = -1

        correction = v - best_code
        code = np.zeros(8)
        code[best_ind] = sign
        lookup_table[tuple(v)] = np.hstack((correction,code))
    return lookup_table

G = np.array([
        [1,1,1,1,1,1,1],
        [-1,-1,-1,1,1,1,1],
        [-1,1,1,-1,-1,1,1],
        [1,-1,-1,-1,-1,1,1],
        [1,-1,1,-1,1,-1,1],
        [-1,1,-1,-1,1,-1,1],
        [-1,-1,1,1,-1,-1,1],
        [1,1,-1,1,-1,-1,1]
    ])
table = hamming_decoder(G)
# just realized I need to check the case where the closest vector is in the compliment
