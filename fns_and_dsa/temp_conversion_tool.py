#Python script that converts temperatures between Celsius and Fahrenheit

#define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#function that converts fahrenheit to celcius
def convert_to_celsius(fahrenheit):
    c = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return c

##function that converts celcius to fahrenheit
def convert_to_fahrenheit(celsius):
    f = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return f

#prompt user for temperature and unit
temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

#convert temperature based on input
match unit:
    case "C":
        print(f"{temperature}\N{DEGREE SIGN}{unit}  is {convert_to_fahrenheit(temperature)}\N{DEGREE SIGN}F")
    case "F":
        print(f"{temperature}\N{DEGREE SIGN}{unit} is {convert_to_celsius(temperature)}\N{DEGREE SIGN}C")
    case _:
        print("Invalid unit provided")