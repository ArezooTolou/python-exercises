"""
Vote Counting with Ordered Output

This program:
1. Reads the number of votes.
2. Reads each vote (candidate's name) from the user.
3. Counts the total votes for each candidate.
4. Prints the results in alphabetical order of candidate names.
"""

from collections import OrderedDict

# Read number of votes
n = int(input("Enter the number of votes: "))

# Dictionary to store vote counts
vote_counts = OrderedDict()

# Read votes and count
for _ in range(n):
    name = input("Enter candidate name: ")
    vote_counts[name] = vote_counts.get(name, 0) + 1

# Print results sorted alphabetically
for candidate in sorted(vote_counts):
    print(f"{candidate} {vote_counts[candidate]}")
