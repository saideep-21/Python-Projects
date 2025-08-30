"""This is a simple calculator which can perform basic arithmetic operations (+, -, *, /)."""

print("----Simple Calculator----")

# Take inputs from the user
num_1 = float(input("Enter the 1st number: "))
num_2 = float(input("Enter the 2nd number: "))
op = input("Enter the arithmetic operator (+, -, *, /): ")

# Perform operations based on the chosen operator
if op == '+':
    result = num_1 + num_2          # Addition
elif op == '-':
    result = num_1 - num_2          # Subtraction
elif op == '*':
    result = num_1 * num_2          # Multiplication
elif op == "/":
    try:
        result = num_1 / num_2      # Division (error handled for denominator = 0)
    except ZeroDivisionError:
        result = "Denominator cannot be zero."
else:
    result = 'Invalid operator selected!'

# Print the result
print("Result:", result)
print("----Thank You----")
