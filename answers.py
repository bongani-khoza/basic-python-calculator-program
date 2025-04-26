# Basic Calculator Program

def calculator():
    # Ask for two numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Ask for operation from the user
    operations = {
        '+': 'addition',
        '-': 'subtraction',
        '*': 'multiplication',
        '/': 'division'
    }
    
    print("\nChoose an operation:")
    print("+ (addition)")
    print("- (subtraction)")
    print("* (multiplication)")
    print("/ (division)")

    op = input("Enter your choice (+, -, *, /): ")

    # Perform the operation based on user's input
    if op in operations:
        try:
            if op == '+':
                result = num1 + num2
                operation_name = operations[op]
                print(f"{num1} {operation_name} {num2} = {result}")
            elif op == '-':
                result = num1 - num2
                operation_name = operations[op]
                print(f"{num1} {operation_name} {num2} = {result}")
            elif op == '*':
                result = num1 * num2
                operation_name = operations[op]
                print(f"{num1} {operation_name} {num2} = {result}")
            elif op == '/':
                if num2 != 0:
                    result = num1 / num2
                    operation_name = operations[op]
                    print(f"{num1} {operation_name} {num2} = {result}")
                else:
                    print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
    else:
        print("Error: Invalid operation. Please choose from the options.")

# Run the calculator function
calculator()
