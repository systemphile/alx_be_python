#A funtion to perform arithmetic operations

#define the function and it parameters
def perform_operation(num1, num2, operation):
    result = 0 # initialize the result

    #execute the arithmetic operation based on the operation parameter
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num1 == 0 or num2 == 0: #handling division by zero
                print("Division by zero error")
            else:
                result = num1 / num2
        case _:
            print("Invalid operation")
    return result #return the result of the arithmetic operation