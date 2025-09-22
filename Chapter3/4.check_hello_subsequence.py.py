"""
Check if 'hello' is a Subsequence

This program:
1. Reads a string from the user.
2. Checks whether the word 'hello' can be formed as a subsequence 
   (characters appear in order, but not necessarily consecutively).
3. Prints "YES" if possible, otherwise "NO".
"""

def contains_hello(s: str) -> str:
    """Return 'YES' if 'hello' is a subsequence of s, otherwise 'NO'."""
    target = "hello"
    i = 0

    for char in s:
        if char == target[i]:
            i += 1
            if i == len(target):
                return "YES"
    return "NO"


# Read input from user
message = input("Enter a string: ")

# Check and print result
print(contains_hello(message))
