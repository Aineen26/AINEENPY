"""
PROGRAM NAME: StringReversal
AUTHOR: AINEEN SAYYED
DATE CREATED: 24/01/2026
"""
# Program to reverse the string taken from user
print("Welcome to StringReversal Program of Python")

def reverse_string(string): #Here this function takes the input as string
    return string[::-1]   #returns string in the reversed form

input_string = input("Enter your string: ")
reversed_str =reverse_string(input_string)
print("Here is your reversed string:",reversed_str)