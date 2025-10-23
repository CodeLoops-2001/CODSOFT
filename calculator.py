# Simple Calculator

def calculator():
    print("---- SIMPLE CALCULATOR ----")
    
    # Get user input for numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return
    
    # Show operation options
    print("\nSelect an operation:")
    print("1 - Addition (+)")
    print("2 - Subtraction (-)")
    print("3 - Multiplication (*)")
    print("4 - Division (/)")
    
    operation = input("Enter the operation (1/2/3/4): ").strip()
    
    # Perform calculation
    if operation == "1":
        result = num1 + num2
        op_symbol = "+"
    elif operation == "2":
        result = num1 - num2
        op_symbol = "-"
    elif operation == "3":
        result = num1 * num2
        op_symbol = "*"
    elif operation == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        op_symbol = "/"
    else:
        print("Invalid operation choice.")
        return
    
    # Display result
    print(f"\nResult: {num1} {op_symbol} {num2} = {result}")

# Run the calculator
calculator()
