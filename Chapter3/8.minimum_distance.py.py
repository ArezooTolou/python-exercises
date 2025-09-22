"""
Minimum Distance to Meeting Point

This program:
1. Reads three integers (locations of three friends or houses).
2. Finds the optimal meeting point (the median of the three numbers).
3. Calculates the total walking distance from all three points to the meeting point.
4. Prints the minimum total distance.
"""

def min_distance(x1: int, x2: int, x3: int) -> int:
    """Return the minimum total distance for three points to meet at a common location."""
    houses = sorted([x1, x2, x3])
    median = houses[1]
    distance = abs(x1 - median) + abs(x2 - median) + abs(x3 - median)
    return distance


# Read inputs
a1 = int(input("Enter the first location: "))
a2 = int(input("Enter the second location: "))
a3 = int(input("Enter the third location: "))

# Compute and print result
print(min_distance(a1, a2, a3))
