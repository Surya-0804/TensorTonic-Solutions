import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    bag_of_words=np.empty(len(vocab),dtype=int)
    freq={}
    for token in tokens:
        freq.update({token:freq.get(token,0)+1})
    for i,voc in enumerate(vocab):
        bag_of_words[i]=freq.get(voc,0)
    return bag_of_words