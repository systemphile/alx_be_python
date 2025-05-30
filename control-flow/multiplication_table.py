#Python Multiplication Table Generator

#ask user for a number
number = int(input("Enter a number to see its multiplication table:"))

#find product of number and multiplication factor
for i in range(1,11):
    product = number * i
    print(f"{number} * {i} = {product}")