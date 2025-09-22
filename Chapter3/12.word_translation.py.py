"""
Word Translation using a Dictionary

This program:
1. Reads a number of dictionary entries.
2. Reads each entry as an English word and its translation.
3. Reads a sentence from the user.
4. Translates words that exist in the dictionary, leaving others unchanged.
5. Prints the translated sentence.
"""

from collections import OrderedDict

# Read number of dictionary entries
n = int(input("Enter number of dictionary entries: "))

# Create dictionary
translations = OrderedDict()

for _ in range(n):
    eng, trans = input("Enter English word and translation separated by space: ").split()
    translations[eng] = trans

# Read sentence to translate
sentence = input("Enter a sentence to translate: ").split()
translated_sentence = []

# Translate each word if available
for word in sentence:
    if word in translations:
        translated_sentence.append(translations[word])
    else:
        translated_sentence.append(word)

# Print the translated sentence
print(' '.join(translated_sentence))
