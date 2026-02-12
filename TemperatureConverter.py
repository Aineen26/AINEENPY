"""PROGRAM TO CONVERT TEMPERATURE
BETWEEN CELSIUS TO FAHRENHEIT
PROGRAM NAME: Temperature Converter
AUTHOR: AINEEN SAYYED
DATE CREATED: 31/01/2026"""
print("CONVERTING TEMPERATURE FROM CELSIUS TO FAHRENHEIT ")
def temp_converter():
    #Get the user input for value and unit
    try:
        temp_value=float(input("Enter temperature in Value: "))
        unit = input("Is this in C/F?").strip().upper()

        #Logic & formula
        #Celsius to Fahrenheit
        if unit == "C":
            converted=(temp_value*9/5)+32
            print(f"{temp_value}C will be {converted:.2f}F")
        #Fahrenheit to Celsius
        elif unit == "F":
            converted=(temp_value-32)*5/9
            print(f"{temp_value}F will be {converted:.2f}C")
        else :
            print("Error:Please enter 'C' for celsius or 'F' for fahrenheit")

    except ValueError:
        print("Error:Please enter a valid temperature value")
if __name__ == "__main__":
    temp_converter()

""" If we use Modern line code"""
# temp,unit=float(input("temperature Value:")),input("Unit(C/F):").upper()
#
# if unit == 'C':
#     print(f"Converted value:{temp * 9 / 5 + 32}")
# else:
#     print(f"({(temp -32)*5/9:.2f}{'F' if unit == 'C' else 'C'}")


