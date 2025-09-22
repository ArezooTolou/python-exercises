"""
Team Formation Counter

This program:
1. Reads the number of participants.
2. Reads each participant's skill type (0, 1, or 2).
3. Determines how many complete teams can be formed 
   (each team must have one member of each type: 0, 1, and 2).
4. Prints the maximum number of teams.
"""

def count_teams(participants: list[int]) -> int:
    """Return the maximum number of complete teams that can be formed."""
    valid_members = [x for x in participants if x in [0, 1, 2]]
    return len(valid_members) // 3


# Read input
n = int(input("Enter the number of participants: "))
participants = []

for _ in range(n):
    participants.append(int(input("Enter participant skill (0, 1, or 2): ")))

# Compute and print result
print(count_teams(participants))
