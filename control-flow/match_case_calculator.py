# Simple Calculator with Match Case

#ask the user for input
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

#handle attempt to divide by 0
if (num1 == 0 or num2 == 0) and operation == "/":
    print("Cannot divide by zero.")
else: #perform operation on user input
    match operation:
        case "+":
            result = num1 + num2
            print("The result is ", result)
        case "-":
            result = num1 - num2
            print("The result is ", result)
        case "*":
            result = num1 * num2
            print("The result is ", result)
        case "/":
            result = num1 / num2
            print("The result is ", result)