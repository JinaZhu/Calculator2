"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator_with_3(symbol, num1, num2):
    # add, sub, div, pow, mod
    if symbol == "+":
        return add(num1, num2)
    elif symbol == "-":
        return subtract(num1, num2)
    elif symbol == "/":
        return divide(num1, num2)
    elif symbol == "pow":
        return power(num1, num2)
    elif symbol == "mod":
        return mod(num1, num2)
    else:
        print("Invalid entry! Try again.")
    # if/elif/else add....etc print the function in arithmetric


def calculator_with_2(symbol, num1):
    if symbol == "square":
        return square(num1)
    elif symbol == "cube":
        return cube(num1)
    else:
        print("Invalid entry! Try again.")


def tokenize():
    print("What do you want to calculate?")
    print("Give us an input.")
    print("""
        Keys
        +: add
        -: subtract
        /: divide
        mod: remainder
        pow: power
        square: square
        cube: cube
        """)
    print("example: [key first number second number], [+ 2 4] **exclude brackets")
    nums = input("> ")
    split = nums.split(" ")
    #print(split)

    if len(split) == 3:
        return calculator_with_3(split[0], float(split[1]), float(split[2]))
    elif len(split) == 2:
        return calculator_with_2(split[0], float(split[1]))
    else:
        print("Invalid, try again!")

def repeat():
    cont = input("Will you like to keep going? yes or q to quit. ")

    while True:
        if cont == "q":
            return tokenize()
        elif cont == "yes":
            print(tokenize())
            repeat()
        else:
            return "invalid entry"


    



print(tokenize())
print(repeat())



    # # No setup
    # repeat forever:
    #     read input
    #     tokenize input
    #     if the first token is "q":
    #         quit
    #     else:
    #         decide which math function to call based on first token