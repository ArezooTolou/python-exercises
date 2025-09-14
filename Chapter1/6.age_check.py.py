"""
File: age_category.py
Author: Arezoo Tolou
Purpose: Categorize a person based on their age.
"""

# Get age from the user
age = int(input("Enter your age: "))

# Determine and print the age category
if 0 < age < 6:
    print("Toddler")      # Toddler
elif 6 <= age < 10:
    print("Child")        # Child
elif 10 <= age < 14:
    print("Pre-teen / Young adolescent")       # Pre-teen / Young adolescent
elif 14 <= age < 24:
    print("Youth")         # Youth
elif 24 <= age < 40:
    print("Adult")     # Adult
elif age >= 40:
    print("Middle-aged")       # Middle-aged
else:
    print("Invalid age")
