#Python Multiplication Table Generator

#ask user for a number
number = int(input("Enter a number to see its multiplication table:"))

#define looping sequence
factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#find product of number and multiplication factor
for factor in factors:
    product = number * factor
    print(f"{number} * {factor} = {product}")