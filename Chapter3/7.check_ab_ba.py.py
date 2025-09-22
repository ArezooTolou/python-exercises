"""
Check Non-Overlapping 'AB' and 'BA' Substrings

This program:
1. Reads a string from the user.
2. Checks whether the string contains both 'AB' and 'BA' 
   as non-overlapping substrings.
3. Prints 'YES' if both exist without overlapping, otherwise 'NO'.
"""

def contains_ab_ba(word: str) -> str:
    """Return 'YES' if the string contains non-overlapping 'AB' and 'BA', else 'NO'."""
    ab = word.find("AB")
    ba = word.find("BA")

    if ab != -1:
        ba_after = word.find("BA", ab + 2)
    else:
        ba_after = -1

    if ba != -1:
        ab_after = word.find("AB", ba + 2)
    else:
        ab_after = -1

    if (ab != -1 and ba_after != -1) or (ba != -1 and ab_after != -1):
        return "YES"
    else:
        return "NO"


# Read input from user
word_input = input("Enter a string: ")

# Check and print result
print(contains_ab_ba(word_input))
