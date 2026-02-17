def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    polynomial_feature = []
    for i in values: 
        polynomial_feature.append([i ** j for j in range(degree + 1)])

    return polynomial_feature