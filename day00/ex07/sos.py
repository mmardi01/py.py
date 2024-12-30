import sys


def encode(s):
    '''encode a string to Morse Code'''
    morse_code_dict = {'A': '.-', 'B': '-...',
                       'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---',
                       'K': '-.-', 'L': '.-..',
                       'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.',
                       'Q': '--.-', 'R': '.-.',
                       'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-',
                       'W': '.--', 'X': '-..-',
                       'Y': '-.--', 'Z': '--..',
                       '0': '-----', '1': '.----',
                       '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....',
                       '6': '-....', '7': '--...',
                       '8': '---..', '9': '----.',
                       ' ': "/ "}
    for c in s:
        print(morse_code_dict.get(c.capitalize()), end=" ")


def main():
    '''validate the input'''

    try:
        if sys.argv.__len__() != 2:
            raise AssertionError('the arguments are bad')
        s = sys.argv[1]
        if s.replace(" ", "").isalnum() is False:
            raise AssertionError('the arguments are bad')
        encode(s)
    except Exception as error:
        print(AssertionError.__name__, ":", error)


if __name__ == '__main__':
    main()
