"""
Palindrome Checker

This program:
1. Reads a word from the user.
2. Reverses the word.
3. Checks whether the word is a palindrome (same forward and backward).
4. Prints 'palindrome' if true, otherwise 'not palindrome'.
"""

def reverse_word(word: str) -> str:
    """Return the reversed version of the given word."""
    reversed_word = ""
    for i in range(len(word)):
        reversed_word += word[-(i + 1)]
    return reversed_word


# Read input from user
word_input = input("Enter a word: ")

# Check palindrome (ignoring case)
if word_input.lower() == reverse_word(word_input.lower()):
    print("palindrome")
else:
    print("not palindrome")
