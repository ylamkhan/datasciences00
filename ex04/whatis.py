"""
1- sys:
    sys is a built-in module in Python that
    provides access
    to system-specific parameters and functions.


    import sys
    print(sys.argv)
    sys.exit(1)
    print(sys.path)

    sys.stdout.write("Hello\n")
    sys.stderr.write("Hello\n")
    sys.stdin.read()
    print(sys.version)

2)-try-except?
    🧠 What is try and except?
        In Python, try and except are used to handle
        exceptions (errors) that may occur during
        the execution of your code.
        This is called exception handling.

    ✅ Basic Syntax:
        try:
            # Code that might raise an exception
            # If no error occurs, this block runs completely
            risky_code()
        except SomeError:
            # Code to handle the exception (error)
            # This block only runs if there is an exception in the
            #  "try" block
            handle_error()
"""

import sys


def check(s):
    digit = "0123456789"
    for char in s:
        if char not in digit:
            return True
    return False


try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 1:
        exit(1)
    if check(sys.argv[1]) is True:
        raise AssertionError("argument is not an integer")
    number = int(sys.argv[1])
    if number % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")
except AssertionError as ve:
    print("\033[91mAssertionError:\033[0m ", ve)
