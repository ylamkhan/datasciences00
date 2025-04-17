import sys


def ft_islower(c):
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    if c in lower_letters:
        return True
    return False


def ft_isupper(c):
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if c in upper_letters:
        return True
    return False


def ft_isdigit(c):
    digites = "0123456789"
    if c in digites:
        return True
    return False


def main():
    """
    This time you have to make a real autonomous program, with a main,
    which takes
    a single string argument and displays the sums of its upper-case
    characters, lower-case
    characters, punctuation characters, digits and spaces.
        • If None or nothing is provided, the user is prompted to
           provide a string.
        • If more than one argument is provided to the program,
            print an AssertionError.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("Number of arguments is incorrect.")
        elif len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.read()
        else:
            text = sys.argv[1]

        if not text:
            raise AssertionError("Please enter a non-empty string.")

        char_counts = {
            "upper letters": 0,
            "lower letters": 0,
            "punctuation marks": 0,
            "spaces": 0,
            "digits": 0
        }

        punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        for c in text:
            if ft_islower(c):
                char_counts["lower letters"] += 1
            elif ft_isupper(c):
                char_counts["upper letters"] += 1
            elif ft_isdigit(c):
                char_counts["digits"] += 1
            elif c == " ":
                char_counts["spaces"] += 1
            elif c in punctuation_chars:
                char_counts["punctuation marks"] += 1

        print(f"The text contains {len(text)} characters:")
        print(f"{char_counts['upper letters']} upper letters")
        print(f"{char_counts['lower letters']} lower letters")
        print(f"{char_counts['punctuation marks']} punctuation marks")
        print(f"{char_counts['spaces']} spaces")
        print(f"{char_counts['digits']} digits")

    except AssertionError as ve:
        print("\033[91mError:\033[0m", ve)


if __name__ == "__main__":
    main()
