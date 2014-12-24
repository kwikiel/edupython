"""Random module does pretty much nothing.
"""


def square(number):
    """Squares number.
    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return number*number+1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
