"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input(">")
    tokens = user_input.split(" ")

    if tokens[0] == "q" or tokens[0] == "quit":
        break
    else:
        try:
            operand_1 = int(tokens[1])
        except:
            print "Operand 1 invalid"
            break

        if len(tokens) > 2:
            try:
                operand_2 = int(tokens[2])
            except:
                print "Operand 2 invalid"
                break

        if tokens[0] == "+":
            print add(operand_1, operand_2)
        elif tokens[0] == "-":
            print subtract(operand_1, operand_2)
        elif tokens[0] == "*":
            print multiply(operand_1, operand_2)
        elif tokens[0] == "/":
            print divide(operand_1, operand_2)
        elif tokens[0] == "square":
            print square(operand_1)
        elif tokens[0] == "cube":
            print cube(operand_1)
        elif tokens[0] == "pow":
            print power(operand_1, operand_2)
        elif tokens[0] == "mod":
            print mod(operand_1, operand_2)
        else:
            print "Invalid input"
