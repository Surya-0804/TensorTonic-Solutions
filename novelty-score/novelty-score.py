import math
def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    # Write code here
    log_sum=0
    for item in item_counts:
        log_sum+=-math.log2(item/n_users)
    return log_sum/len(recommendations)
