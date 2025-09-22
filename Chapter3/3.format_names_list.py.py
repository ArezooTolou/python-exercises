"""
Name Formatting Exercise

This program:
1. Reads 10 names from the user.
2. Converts each name to lowercase, then capitalizes the first letter.
3. Stores all formatted names in a list.
4. Prints the formatted names, one per line.
"""

names = []

# Read 10 names and format them
for i in range(10):
    name = input(f"Enter name {i+1}: ")
    formatted_name = name.lower().capitalize()
    names.append(formatted_name)

# Print all formatted names
print("\nFormatted names:")
for n in names:
    print(n)
