import sys


def count(text: str):
    """
    args (text: str) The text to analyze,
    print th sum of:
    upper-case
    characters
    lower-case characters
    punctuation
    characters
    digits
    spaces.
    """
    punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation_number = 0
    upper = 0
    lower = 0
    spaces = 0
    digits = 0

    for s in text:
        if s.islower():
            lower += 1
        if s.isupper():
            upper += 1
        if s.isspace():
            spaces += 1
        if s.isdigit():
            digits += 1
        if s in punctuation_marks:
            punctuation_number += 1

    print(f"The text contains {text.__len__()} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} upper lower")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():

    """
        validate the input.
    """

    try:
        if sys.argv.__len__() > 2:
            raise AssertionError('too many args')
        elif sys.argv.__len__() == 1:
            x = input('What is the text to count?\n')
        else:
            x = sys.argv[1]
        count(x)
    except AssertionError as error:
        print(error)
    except EOFError:
        return
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
