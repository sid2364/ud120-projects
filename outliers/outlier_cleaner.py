#!/usr/bin/python
from operator import itemgetter

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []

    for i in range(len(ages)):
        cleaned_data.append((ages[i][0], net_worths[i][0], net_worths[i][0]-predictions[i][0]))
    cleaned_data.sort(key=itemgetter(2), reverse=True)

    return cleaned_data[:int(len(cleaned_data)*0.9)]

