# Daniel Sterling
# October 14, 2024
# Week 2 Assignment 2: Programming Assignment

# Input section
v1 = float(input("Enter the first value:\n"))
v2 = float(input("Enter the second value:\n"))
v3 = float(input("Enter the third value:\n"))
v4 = float(input("Enter the fourth value:\n"))

# Arithmetic section
# Addition
add_result = v1 + v2
# Subtraction
subtract_result = v3 - v4
# Multiplication
multiply_result = v1 * v3
# Division
if v4 != 0:
    divide_result = v2 / v4
else:
    divide_result = "Error: Division by zero"

# Display Results
print(f"Addition of {v1} and {v2} is {add_result}")
print(f"Subtraction of {v3} and {v4} is {subtract_result}")
print(f"Multiplication of {v1} and {v3} is {multiply_result}")
print(f"Division of {v2} and {v4} is {divide_result}")