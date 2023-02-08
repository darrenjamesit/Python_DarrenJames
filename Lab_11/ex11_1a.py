def average(x):
    """Function for calculating averages of numbers in a tuple.
    Parameters
    ----------
    x : tuple
    A tuple containing integers or floats.
    Returns
    ----------
    int:
    This is the average of the numbers in the tuple.
    Example usage:
    >>> average((1, 2, 3))
    2
    >>> average((2, 4, 6))
    4
    """
    if len(x) <= 0:
        print('error.')
    else:
        mean = round(sum(x)/len(x))
    return mean

tupl = (2, 4, 5, 6)

print(average(tupl))

if __name__ == '__main__':
    from doctest import testmod
    testmod()
    testmod(verbose=True)
