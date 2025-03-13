# user input and converting to numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (-, +, /, *): ")

# Performing calculations
if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    # just preventing negative results
    if num1>num2:
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    else:
             print("Enter {num1} must be greater than {num2}")
elif operator == '/':
    if num2 != 0: 
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed.")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
else:
    print("Invalid operation! Please enter +, -, *, or /.")
