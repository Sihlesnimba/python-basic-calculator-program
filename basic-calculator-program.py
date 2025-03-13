# My basic calculator program

num1 = float(input("Enter the first number:"))
operator = input("Enter the mathematical operator (+ - / *): ")
num2 = float(input("Enter the second number:"))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
else:
    print(f"{operator} is not a valid operator")