import math

def truncated_sqrt(number: float, decimals: int = 4) -> float:
    """
    Returns the square root of a number truncated to a specific number of decimals.
    
    Parameters:
        number (float): The input number.
        decimals (int): Number of decimal digits to keep (default: 4).
    
    Returns:
        float: Truncated square root.
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    
    factor = 10 ** decimals
    truncated = int(math.sqrt(number) * factor) / factor
    return truncated


if __name__ == "__main__":
    n = int(input("Enter the number of values: "))
    numbers = [float(input()) for _ in range(n)]
    
    print("\nResults:")
    for num in numbers:
        print(f"{truncated_sqrt(num):.4f}")
