def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is undefined."
    return num1 / num2

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    operations = {
        1: ("Add", "+", add),
        2: ("Subtract", "-", subtract),
        3: ("Multiply", "*", multiply),
        4: ("Divide", "/", divide)
    }

    while True:
        print("\nPlease select an operation:")
        for key, (name, _, _) in operations.items():
            print(f"{key}. {name}")

        try:
            select = int(input("Select an operation (1, 2, 3, 4): "))
            if select not in operations:
                print("Invalid selection. Please choose a valid operation.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        number_1 = get_number("Enter the first number: ")
        number_2 = get_number("Enter the second number: ")

        name, symbol, operation_func = operations[select]
        result = operation_func(number_1, number_2)
        print(f"\nResult: {number_1} {symbol} {number_2} = {result}")

        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
