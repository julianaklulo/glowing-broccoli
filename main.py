from calculator import sum, subtract, multiply, divide, validate_float

def get_numbers_input():
    try:
        number1 = float(input("Type the first number: "))
        number2 = float(input("Type the second number: "))
        return number1, number2
    except Exception:
        print("Value is not float")

def sum_numbers():
    number1, number2 = get_numbers_input()
    print(f"Sum: {sum(number1, number2)}")

def subtract_numbers():
    number1, number2 = get_numbers_input()
    print(f"Subtraction: {subtract(number1, number2)}")

def multiply_numbers():
    number1, number2 = get_numbers_input()
    print(f"Multiplication: {multiply(number1, number2)}")

def divide_numbers():
    number1, number2 = get_numbers_input()
    print(f"Division: {divide(number1, number2)}")

def menu():
    option = -1
    while option < 0 or option > 4:
        print("\nChoose an operation:")
        print("1 - Sum")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
        print("--------------------")
        print("0 - Exit")
        option = int(input("\nOption: "))

        if option == 0:
            break
        elif option == 1:
            sum_numbers()
        elif option == 2:
            subtract_numbers()
        elif option == 3:
            multiply_numbers()
        elif option == 4:
            divide_numbers()

if __name__ == "__main__":
    menu()