from functions import *
from operations import *

while True:
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    choice = input("Enter choice (1/2/3/4/0): ")

    if choice == '0':
        print("Exiting the calculator. Goodbye!")
        break

    num1, num2 = get_user_input()

    if num1 is None or num2 is None:
        continue

    if choice == '1':
        result = perform_addition(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = perform_subtraction(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = perform_multiplication(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = perform_division(num1, num2)
        print(result)
    else:
        print("Invalid input")