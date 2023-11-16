from functions import add, subtract, multiply, divide
import logging

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


# Створення конфігурації для логування
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def get_user_input():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        return None, None

def perform_addition(x, y):
    result = add(x, y)
    logging.info(f"Performed addition on {x} and {y}, result: {result}")
    return result

def perform_subtraction(x, y):
    result = subtract(x, y)
    logging.info(f"Performed subtraction on {x} and {y}, result: {result}")
    return result

def perform_multiplication(x, y):
    result = multiply(x, y)
    logging.info(f"Performed multiplication on {x} and {y}, result: {result}")
    return result

def perform_division(x, y):
    result = divide(x, y)
    logging.info(f"Performed division on {x} and {y}, result: {result}")
    return result