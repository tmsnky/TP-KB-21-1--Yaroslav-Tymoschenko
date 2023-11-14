from functions import add, subtract, multiply, divide

def get_user_input():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        return None, None

def perform_addition(x, y):
    return add(x, y)

def perform_subtraction(x, y):
    return subtract(x, y)

def perform_multiplication(x, y):
    return multiply(x, y)

def perform_division(x, y):
    return divide(x, y)