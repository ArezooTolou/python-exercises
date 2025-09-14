"""
File: double_reversed_number.py
Author: Arezoo Tolou
Purpose: Reverse a three-digit number and print double its value.
"""

# Get a three-digit number from the user
num = int(input("Enter a three-digit number: "))

# Extract hundreds, tens, and units digits
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

# Reverse the number
reversed_num = (units * 100) + (tens * 10) + hundreds

# Print double the reversed number
result = 2 * reversed_num
print(f"Double the reversed number is: {result}")
