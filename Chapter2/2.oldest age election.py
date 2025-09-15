"""
Find the oldest age from user input until -1 is entered.

This program:
1. Continuously reads ages from the user.
2. Stops when the user enters -1.
3. Keeps track of the maximum (oldest) age entered.
4. Prints the oldest age found.
"""

# Initialize the maximum age with a small default value
oldest = -1  

# Read the first input
age = int(input("Enter an age (-1 to stop): "))

# Loop until sentinel value (-1) is entered
while age != -1:
    if age > oldest:
        oldest = age
    age = int(input("Enter an age (-1 to stop): "))

print(f"The oldest age is: {oldest}")
