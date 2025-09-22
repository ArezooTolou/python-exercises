"""
Convert Word to Uppercase or Lowercase

This program:
1. Reads a word from the user.
2. Counts the number of uppercase and lowercase letters.
3. If uppercase letters are more, it converts the whole word to UPPERCASE.
   Otherwise, it converts the whole word to lowercase.
4. Prints the converted word.
"""

def convert_case(word: str) -> str:
    """Convert a word to uppercase if it has more uppercase letters, 
    otherwise to lowercase."""
    upper_count = 0
    lower_count = 0

    for char in word:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    if upper_count > lower_count:
        return word.upper()
    else:
        return word.lower()


# Read input from user
word_input = input("Enter a word: ")

# Process and print result
print(convert_case(word_input))
