"""
File: calculate_rectangle_area.py
Author: Arezoo Tolou
Purpose: Calculate the area of a rectangle given length and width.
"""

# Get user input for length and width
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Calculate the area and print the absolute value
area = abs(length * width)
print(f"The area of the rectangle is: {area}")
