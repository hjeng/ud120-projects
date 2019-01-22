#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import operator
    
    cleaned_data = []

    ### your code goes here
    # calculate error between net worths and predictions
    # locate minimum value and index using numpy.argmin()
    # use index to delete row from ages and net_worths arrays
    # repeat for 10% of total amount of list
    error = [a-b for a,b in zip(predictions, net_worths)]
    uncleaned_data = zip(ages, net_worths, error)
    uncleaned_data.sort(key = operator .itemgetter(2))
    
    cleaned_data = uncleaned_data[:int(len(net_worths)*0.9)]
    
    return cleaned_data

