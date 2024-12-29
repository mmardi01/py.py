

def ft_filter(fn, iterable):
    '''ft_filter(function or None, iterable) --> filter object\

    \nReturn an iterator yielding those items\
    of iterable for which function(item)\
    \nis true. If function is None, return the items that are true.'''

    return [it for it in iterable if fn(it)]
