""" PROGRAM TO PERFORM DIFFERENT
 ARITHMETIC OPERATIONS
 PROGRAM NAME: Calculator
AUTHOR: AINEEN SAYYED
DATE CREATED: 27/01/2026"""

print("SIMPLE CALCULATOR")

operand1 = int(input("enter the operand: "))
operand2 = int(input("enter the second operand: "))
operator = input("enter the operator(+,-,/,*,%,//,**): ")

if operator == "+":
    print("Your addition :",operand1 + operand2)
elif operator == "-":
    print("Your subtraction :",operand1 - operand2)
elif operator == "/":
    print("Your Division :",operand1 / operand2)
elif operator == "*":
    print("Your Multiplication :",operand1 * operand2)
elif operator == "%":
    print("Your Modulus :",operand1 % operand2)
elif operator == "**":
    print("Your Square :",operand1 ** operand2)
elif operator == "//":
    print("Your Floor Division :",operand1 // operand2)
else:
    print("Operation not supported")
