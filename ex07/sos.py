"""

"""
import sys


def ft_upper(c):
    letter_map = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
        'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
        'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
        's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
        'y': 'Y', 'z': 'Z',
        'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F',
        'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L',
        'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
        'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
        'Y': 'Y', 'Z': 'Z'
    }
    return letter_map[c]


def my_isalphanum(c):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return c in letters


def my_isalnum(s):
    for char in s:
        if my_isalphanum(char) is False:
            return False
    return True


def my_upper(s):
    lower = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in s:
        if char in lower:
            c = ft_upper(char)
            result += c
        else:
            result += char
    return result


def main():
    NESTED_MORSE = {
        'A': '.-',    'B': '-...',  'C': '-.-.',
        'D': '-..',   'E': '.',     'F': '..-.',
        'G': '--.',   'H': '....',  'I': '..',
        'J': '.---',  'K': '-.-',   'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',
        'S': '...',   'T': '-',     'U': '..-',
        'V': '...-',  'W': '.--',   'X': '-..-',
        'Y': '-.--',  'Z': '--..',  ' ': '/ ',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
    }
    result = ""

    try:
        if len(sys.argv) != 2:
            raise AssertionError("The arguments are bad")
        text = sys.argv[1]
        if my_isalnum(text) is False:
            raise AssertionError("The arguments are bad")
        text_upper = my_upper(text)
        # print(text_upper)
        i = 0
        while i < len(text_upper):
            # print(text[i])
            result += NESTED_MORSE[text_upper[i]]
            i += 1
        print(result)
    except AssertionError as ve:
        print("\033[91mAssertionError:\033[0m", ve)


if __name__ == "__main__":
    main()
