from ft_filter import ft_filter
import sys


def main():
    '''take 2 args (string, n).\
    \ncheck types.\
    \nprint list of words with length greater than n.
    '''
    try:
        if sys.argv.__len__() != 3:
            raise AssertionError('the arguments are bad')
        s = sys.argv[1]
        words = s.split(' ')
        n = int(sys.argv[2])
        res = ft_filter(lambda x: len(x) > n, words)
        print(res)
    except Exception as error:
        error
        print('AssertionError: the arguments are bad')


if __name__ == "__main__":
    main()
