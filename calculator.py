def calculate(num1, num2, operation):
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else "Error: Division by zero"
    }
    return operations.get(operation, "Invalid operation")


def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation: ")
            num2 = float(input("Enter second number: "))

            result = calculate(num1, num2, op)
            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Enter numbers only.")

        choice = input("Continue? (y/n): ").lower()
        if choice != "y":
            print("Calculator closed.")
            break


if __name__ == "__main__":
    calculator()
