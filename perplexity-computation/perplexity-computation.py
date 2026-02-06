import math

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    prob_sum = 0
    N=len(actual_tokens)

    for distribution,token in zip(prob_distributions,actual_tokens):
        prob_sum+=-math.log(distribution[token])

    entropy=prob_sum/N
    return math.exp(entropy)