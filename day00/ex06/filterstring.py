from ft_filter import ft_filter
import sys


def main():
    try:
        if sys.argv.__len__() != 3:
            raise AssertionError('the arguments are bad')
        s = sys.argv[1]
        words = s.split(' ')
        n = int(sys.argv[2])
        res = ft_filter(lambda x : len(x) > n, words)
        print(res)
    except Exception as error:
        print('AssertionError: the arguments are bad')


if __name__ == "__main__":
    main()
