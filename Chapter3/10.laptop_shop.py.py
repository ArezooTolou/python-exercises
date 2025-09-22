"""
Laptop Shop Problem (Happy Irsa)

This program:
1. Reads the number of laptops.
2. For each laptop, reads its price and quality.
3. Checks if there exists a cheaper laptop with higher quality than a more expensive one.
4. Prints "happy irsa" if such a case exists, otherwise prints "poor irsa".
"""

# Read number of laptops
n = int(input("Enter number of laptops: "))

laptops = []

# Read price and quality for each laptop
for _ in range(n):
    price, quality = map(int, input("Enter price and quality separated by space: ").split())
    laptops.append([price, quality])

# Sort laptops by price
laptops.sort()

# Check if there exists a laptop with lower price but higher quality
for i in range(n - 1):
    if laptops[i][1] > laptops[i + 1][1]:
        print("happy irsa")
        exit()

print("poor irsa")
