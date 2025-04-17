"""
"""
import sys


def my_isalphanum(c):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return c in letters


def my_isalnum(s):
    for char in s:
        if not (my_isalphanum(char)):
            return False
    return True


def check_arg_digit(str1):
    digits = "0123456789"
    for char in str1:
        if char not in digits:
            return True
    return False


def main():

    """
        Create a program that accepts two arguments: a string(S), and an
        integer(N). The
        program should output a list of words from S that have a length
        greater than N.
            • Words are separated from each other by space characters.
            • Strings do not contain any special characters. (Punctuation or
              invisible)
            • The program must contain at least one list comprehension
                expression and one lambda.
            • If the number of argument is different from 2, or if the type
              of any argument is wrong,
        the program prints an AssertionError.
    """

    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if check_arg_digit(sys.argv[2]) is True:
            raise AssertionError("the arguments are bad")
        S = sys.argv[1]
        N = int(sys.argv[2])
        words = S.split(' ')
        print(list(filter(lambda word: my_isalnum(word)
                          and len(word) > N, words)))

    except AssertionError as ve:
        print("\033[91mAssertionError:\033[0m", ve)

    # numbers = [1, 2, 3, 4, 5, 6,"k","hhghg","112", None, "", '']
    # print("\033[91mft_filter:\033[0m")
    # filtered_numbers = ft_filter(filterstring, numbers)
    # print(list(filtered_numbers))
    # print("\033[91mfilter:\033[0m")
    # filtered_numbers = filter(filterstring, numbers)
    # print(list(filtered_numbers))


if __name__ == "__main__":
    main()
