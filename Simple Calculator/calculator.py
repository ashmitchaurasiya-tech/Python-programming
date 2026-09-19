# Simple Calculator for Beginners
# This program performs basic math operations
 
def add(a, b):
    return a + b
 
def subtract(a, b):
    return a - b
 
def multiply(a, b):
    return a * b
 
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b
 
def calculator():
    print("===========================")
    print("    Simple Calculator 🧮   ")
    print("===========================")
    print("Operations:")
    print("  1 → Addition       (+)")
    print("  2 → Subtraction    (-)")
    print("  3 → Multiplication (×)")
    print("  4 → Division       (÷)")
    print("  5 → Quit")
    print("===========================\n")
 
    while True:
        choice = input("Choose an operation (1/2/3/4/5): ")
 
        if choice == "5":
            print("Goodbye! 👋")
            break
 
        if choice not in ("1", "2", "3", "4"):
            print("❌ Invalid choice. Please enter 1, 2, 3, 4, or 5.\n")
            continue
 
        # Get numbers from the user
        try:
            num1 = float(input("Enter the first number:  "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("❌ That's not a valid number. Please try again.\n")
            continue
 
        # Perform the chosen operation
        if choice == "1":
            result = add(num1, num2)
            symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "×"
        elif choice == "4":
            result = divide(num1, num2)
            symbol = "÷"
 
        print(f"\n✅ {num1} {symbol} {num2} = {result}\n")
 
# Run the calculator
calculator()