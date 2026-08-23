
import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]
             ) -> list[int | float]:
    '''
    take 2 lists of integers or floats in input and returns a list
    of BMI values
    '''
    try:
        if len(height) != len(weight):
            raise AssertionError('lists must have the same length')
        a = np.array(height)
        b = np.array(weight)
        valid_types = ['float64', 'float32', 'int64', 'int32']
        if a.dtype not in valid_types or b.dtype not in valid_types:
            raise AssertionError('lists must include only ints and floats')
        squares = np.multiply(a, a)
        bmi = np.divide(b, squares).tolist()
        return bmi
    except Exception as e:
        print("An error occurred:", e)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    accepts a list of integers or floats and an integer representing
    a limit as parameters.
    It returns a list of booleans (True if above the limit).
    '''
    if (len(bmi) == 0):
        return []
    return [x > limit for x in bmi]
