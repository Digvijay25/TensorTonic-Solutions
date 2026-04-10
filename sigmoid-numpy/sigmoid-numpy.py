import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here

    arr = np.array(x, dtype='float32')

    return 1/(1 + np.exp(-arr))