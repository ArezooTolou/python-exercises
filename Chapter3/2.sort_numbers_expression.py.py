"""
Sort Numbers in a String Expression

This program:
1. Reads a string of numbers separated by '+' (e.g., "3+2+1").
2. Splits the string into individual numbers.
3. Sorts the numbers in ascending order.
4. Joins them back with '+'.
5. Prints the sorted expression.
"""

# Read input string
expression = input("Enter numbers separated by '+': ")

# Split by '+' and sort as strings
numbers = expression.split("+")
numbers.sort()

# Join them back with '+'
sorted_expression = "+".join(numbers)

print(sorted_expression)
