import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    function that takes as parameters a 2D array,
    prints its shape, and returns a truncated version of the array
    based on the provided start and end arguments
    '''
    try:
        valid_types = ['float64', 'float32', 'int64', 'int32']
        a = np.array(family)
        print(a.dtype)
        if a.dtype not in valid_types:
            raise AssertionError('lists must include only ints and floats')
        print("My shape is :", a.shape)
        sliced = a[start:end]
        print("My new shape is :", sliced.shape)
        return sliced.tolist()
    except Exception:
        print('Invalid Input')
        return []
