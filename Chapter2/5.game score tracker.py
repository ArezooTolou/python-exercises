"""
Game Score Tracker

This program:
1. Reads 30 scores (one per round).
2. Calculates the total (final) score.
3. Counts how many times the score was exactly 3 (wins).
4. Prints the final score and number of wins.
"""

final_score = 0   # Sum of all scores
wins = 0          # Count of rounds with score == 3

# Read 30 scores
for round_number in range(1, 31):
    score = int(input(f"Enter score for round {round_number}: "))
    final_score += score

    if score == 3:
        wins += 1

print(f"Final Score: {final_score}")
print(f"Number of Wins (score == 3): {wins}")
