"""
Number Guessing Game (Computer as the Guesser)

This program:
1. The computer tries to guess a number between 1 and 99.
2. The user provides feedback after each guess:
   - 'd' → correct (done)
   - 'k' → the guess is too high
   - 'b' → the guess is too low
3. The computer keeps guessing until it finds the correct number.
"""

import random

# Initial guessing range
low = 1
high = 99

# First random guess
guess = random.randint(low, high)
print(f"My guess is: {guess}")

# User feedback: 'd' = correct, 'k' = too high, 'b' = too low
feedback = input("Enter 'd' if correct, 'k' if too high, 'b' if too low: ")

while feedback != 'd':
    if feedback == 'k':
        high = guess - 1
    elif feedback == 'b':
        low = guess + 1
    
    # Generate a new guess in the updated range
    guess = random.randint(low, high)
    print(f"My guess is: {guess}")

    feedback = input("Enter 'd' if correct, 'k' if too high, 'b' if too low: ")

print(f"Yay! The number is {guess} 🎉")
