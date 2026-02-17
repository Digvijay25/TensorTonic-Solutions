import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    token_dict = {i: tokens.count(i) for i in set(tokens)}

    if len(vocab) == 0: 
        return np.array([], dtype=int)
    else:
        return np.array([token_dict[i] if i in token_dict else 0 for i in vocab ])