
print("CONVERTING TEMPERATURE FROM CELSIUS TO FAHRENHEIT ")
def temp_converter():
  
    try:
        temp_value=float(input("Enter temperature in Value: "))
        unit = input("Is this in C/F?").strip().upper()

      
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




