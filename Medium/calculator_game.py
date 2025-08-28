def calculator(num_1, num_2, op):
    """
    Simple calculator that performs basic arithmetic operations (+, -, *, /).
    Features:
    - Uses functions
    - Supports loops (game continues until 'q' is entered)
    - Error handling (invalid input & zero division)
    - Conditional statements
    """
    if op == '+':
        result = f"Sum is: {num_1 + num_2}"          # Addition
    elif op == '-':
        result = f"Difference is: {num_1 - num_2}"   # Subtraction
    elif op == '*':
        result = f"Product is: {num_1 * num_2}"      # Multiplication
    elif op == "/":
        try:
            result = f"Quotient is: {num_1 / num_2}" # Division with error handling
        except ZeroDivisionError:
            result = "Denominator cannot be zero."
    else:
        result = 'Invalid operator entered!'
    return result


print("---- Simple Calculator Game ----")
print("---- Enter 'q' anytime to quit ----")

while True:
    num_1 = input("Enter the 1st number: ")
    if num_1 == 'q':
        break

    num_2 = input("Enter the 2nd number: ")
    if num_2 == 'q':
        break

    op = input("Enter the arithmetic operator (+, -, *, /): ")
    if op == 'q':
        break

    try:
        num_1, num_2 = float(num_1), float(num_2)    # Convert inputs to float
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")
    else:
        print(calculator(num_1, num_2, op))          # Call function & display result

print("--- Thank You ---")
