
import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]
             ) -> list[int | float]:
    '''
    take 2 lists of integers or floats in input and returns a list
    of BMI values
    '''
    valid_types = ['float64', 'float32', 'int64', 'int32']
    try:
        if len(height) is not len(weight):
            raise AssertionError('lists must have the same length')
        a = np.array(height)
        b = np.array(weight)
        if a.dtype not in valid_types or b.dtype not in valid_types:
            raise AssertionError('lists must include only ints and floats')
        squares = np.multiply(a, a)
        bmi = np.divide(b, squares).tolist()
        return bmi
    except Exception as e:
        print(e)
        exit()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    accepts a list of integers or floats and an integer representing
    a limit as parameters.
    It returns a list of booleans (True if above the limit).
    '''
    return [x > limit for x in bmi]
