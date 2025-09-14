"""
File: next_multiple_of_ten.py
Author: Arezoo Tolou
Purpose: Calculate the next multiple of ten for a given number.
"""

# Get a number from the user
num = int(input("Enter a number: "))

# Calculate the next multiple of ten
next_multiple = ((num // 10) + 1) * 10

# Print the result
print(f"The next multiple of ten is: {next_multiple}")
