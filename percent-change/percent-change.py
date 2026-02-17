def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    pct_change = []
    
    for i in range(len(series)-1):
        if series[i] == 0:
            pct_change.append(0.0)
        else: 
            pct_change.append((series[i+1] - series[i]) / series[i])
            

    return pct_change
            