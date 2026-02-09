def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    ref_total = sum(reference_counts)
    prod_total = sum(production_counts)

    normalized_ref=[ref/ref_total for ref in reference_counts]
    normalized_prod=[prod/prod_total for prod in production_counts]
    
    tvd = 0.5 * sum(abs(p-q) for p,q in zip(normalized_ref,normalized_prod))

    drift_detected=tvd/2>threshold
    
    return {"score":tvd ,"drift_detected":drift_detected}
