"""
Find the number with the most divisors among 20 inputs.

This program:
1. Reads 20 numbers from the user.
2. Calculates the number of divisors for each number.
3. Determines which number has the highest count of divisors.
   - If there is a tie, it picks the larger number.
4. Prints the result as: number divisor_count
"""

def divisor_count(x: int) -> int:
    """Return the number of divisors of x."""
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count


final_num = 0        # Number with the most divisors
final_count = 0      # Highest divisor count found so far

# Read 20 numbers from user input
for _ in range(20):
    num = int(input("Enter a number: "))
    current_count = divisor_count(num)

    # Update if we find a number with more divisors
    if current_count > final_count:
        final_num = num
        final_count = current_count
    # If same divisor count, keep the larger number
    elif current_count == final_count and num > final_num:
        final_num = num
        final_count = current_count

print(f"{final_num} {final_count}")
