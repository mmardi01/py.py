import sys


def is_odd_or_even(number):
    try:        
        number = int(sys.argv[1])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except:
        raise AssertionError('argument is not an integer')


def main():
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 2:
        is_odd_or_even(sys.argv[1])

try:
    main()
except AssertionError as error:
    print(AssertionError.__name__,':', error)