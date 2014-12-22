def square(x):
    """Squares x.
    
    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x*x+1

if __name__=='__main__':
    import doctest
    doctest.testmod()
