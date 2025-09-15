"""
Check if a number is prime.

This program:
1. Reads a number from the user.
2. Checks how many divisors it has (excluding itself).
3. Prints "prime" if the number has only 1 divisor (which is 1).
4. Otherwise, prints "not prime".
"""

num = int(input("Enter a number: "))
divisor_count = 0

# Count divisors excluding the number itself
for i in range(1, num):
    if num % i == 0:
        divisor_count += 1

if divisor_count == 1:
    print("prime")
else:
    print("not prime")
