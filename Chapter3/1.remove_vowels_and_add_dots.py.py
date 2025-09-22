"""
String Transformation: Remove Vowels and Add Dots

This program:
1. Reads a string from the user.
2. Converts the string to lowercase.
3. Removes all vowels (a, e, i, o, u).
4. Keeps only alphabetic characters.
5. Adds a '.' before each remaining character.
6. Prints the transformed string.
"""

# Input string
text = input("Enter a string: ")

# Convert to lowercase and remove vowels
no_vowels = text.lower().translate({ord(ch): None for ch in "aeiou"})

# Build the transformed string
result = ""
for ch in no_vowels:
    if ch.isalpha():
        result += "." + ch

print(result)
