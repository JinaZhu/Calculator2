"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator_with_3(symbol, num1, num2):
    # add, sub, div, pow, mod
    if symbol == "+":
        print(add(num1, num2))
    elif symbol == "-":
        print(subtract(num1, num2))
    elif symbol == "/":
        print(divide(num1, num2))
    elif symbol == "pow":
        print(power(num1, num2))
    elif symbol == "mod":
        print(mod(num1, num2))
    else:
        print("Invalid entry! Try again.")
    # if/elif/else add....etc print the function in arithmetric


def calculator_with_2(symbol, num1):
    if symbol == "square":
        print(square(num1))
    elif symbol == "cube":
        print(cube(num1))
    else:
        print("Invalid entry! Try again.")


def tokenize():
    print("What do you want to calculate?")
    print("Give us an input.")
    print("example: +, 3, 4 will calculate 3 + 4")
    nums = input("> ")
    split = nums.split(",")
    if len(split) == 3:
        calculator_with_3(split[0], float(split[1]), float(split[2]))
    elif len(split) == 2:
        calculator_with_2(split[0], float(split[1]))
    else:
        print("Invalid, try again!")


test = tokenize()
print(test)

    # # No setup
    # repeat forever:
    #     read input
    #     tokenize input
    #     if the first token is "q":
    #         quit
    #     else:
    #         decide which math function to call based on first token