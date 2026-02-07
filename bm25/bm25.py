import numpy as np
from collections import Counter, defaultdict
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    if not docs:
        return np.array([],dtype=float)
    
    N = len(docs)

    doc_lens = np.array([len(doc) for doc in docs],dtype=float)
    avg_dl=doc_lens.mean() if N else 0

    tf_docs = [Counter(doc) for doc in docs]

    df = defaultdict(int)
    for doc in docs:
        for t in set(doc):
            df[t]+=1

    query_terms = list(dict.fromkeys(query_tokens))

    idf={}
    for t in query_terms:
        if t not in df:
            idf[t]=0.0
        else:
            idf[t]=math.log((N-df[t]+0.5)/(df[t]+0.5) +1)
    
    scores = np.zeros(N, dtype=float)

    for i,tf in enumerate(tf_docs):
        dl =  doc_lens[i]
        norm = k1*(1-b +b*dl/avg_dl)

        for t in query_terms:
            tf_td = tf.get(t,0)

            if tf_td == 0:
                continue
            
            numerator = tf_td *(k1+1)
            denom = tf_td + norm
            scores[i]+=idf[t]*numerator/denom

    return scores
