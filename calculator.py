def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

def calculator():
    while True:
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: ").strip())
                num2 = float(input("Enter the second number: ").strip())
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = add(num1, num2)
                print(f"The result is: {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"The result is: {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"The result is: {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result is: {result}")

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    calculator()
