
print("Welcome to StringReversal Program of Python")

def reverse_string(string): 
    return string[::-1]   
input_string = input("Enter your string: ")
reversed_str =reverse_string(input_string)
print("Here is your reversed string:",reversed_str)
