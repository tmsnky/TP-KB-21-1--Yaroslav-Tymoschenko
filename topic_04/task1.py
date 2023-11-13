def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is undefined.")
        return None
    else:
        return result

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

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        continue

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        if result is not None:
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input")