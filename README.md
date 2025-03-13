# Basic Calculator Program

A simple Python program that lets you input two numbers and a mathematical operator (`+`, `-`, `/`, `*`). It calculates the result and displays it in an easy-to-read format.

## How to Use
1. Download or clone this repository to your computer.
2. Open a terminal or command prompt and navigate to the folder where the program is saved.
3. Run the program by typing:
   ```bash
   python calculator.py
   ```
4. Follow the prompts:
   - Enter the first number.
   - Enter the operator (`+`, `-`, `/`, `*`).
   - Enter the second number.
5. The program will show the result (e.g., `10 + 5 = 15`).

## What the Code Does
- The program asks for two numbers and an operator.
- It checks the operator and performs the correct calculation.
- If the operator is invalid, it tells you.

Here’s the code:
```python
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
```

## Requirements
- Python installed on your computer. Download it from [python.org](https://www.python.org/).
