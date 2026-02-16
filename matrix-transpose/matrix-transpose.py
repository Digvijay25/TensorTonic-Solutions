import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    B = np.array(A)
    C = np.zeros([B.shape[1], B.shape[0]])

    for i,j in enumerate(A):
        for k, l in enumerate(j):
            C[k,i] = l 
    
    return C
        
