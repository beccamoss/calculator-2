"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input(">")
    tokens = user_input.split(" ")
    list_operands = []
    bad_operand = False
    
    if tokens[0] == "q" or tokens[0] == "quit":
        break
    else:
        for i in range(1, len(tokens)):
            try:
                operand = int(tokens[i])
            except:
                print "Invalid operand"
                bad_operand = True
                break
            
            list_operands.append(operand)    

        if not bad_operand:
            if tokens[0] == "+":
                print add(list_operands)
            elif tokens[0] == "-":
                print subtract(list_operands)
            elif tokens[0] == "*":
                print multiply(list_operands)
            elif tokens[0] == "/":
                print divide(list_operands)
            elif tokens[0] == "square":
                print square(list_operands)
            elif tokens[0] == "cube":
                print cube(list_operands)
            elif tokens[0] == "pow":
                print power(list_operands)
            elif tokens[0] == "mod":
                print mod(list_operands)
            else:
                print "Invalid input"


# try:
#             operand_1 = int(tokens[1])
#         except:
#             print "Operand 1 invalid"
#             break

#         if len(tokens) > 2:
#             try:
#                 operand_2 = int(tokens[2])
#             except:
#                 print "Operand 2 invalid"
#                 break
