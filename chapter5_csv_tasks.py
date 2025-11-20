import csv
from collections import OrderedDict
from statistics import mean
import os

# -----------------------------
# Folder and file paths
# -----------------------------
DATA_FOLDER = "data"  # folder where the CSV dataset is located
INPUT_FILE = os.path.join(DATA_FOLDER, "grades.csv")

# Output files for each task
OUTPUT_TASK1 = "task1_output.csv"
OUTPUT_TASK2 = "task2_output.csv"
OUTPUT_TASK3 = "task3_output.csv"
OUTPUT_TASK4 = "task4_output.csv"
OUTPUT_TASK5 = "task5_output.csv"

# -----------------------------
# Task 1: Calculate average score per student
# -----------------------------
def calculate_averages(input_file_name, output_file_name):
    """
    Read input CSV, calculate the average of each student's scores,
    and save results to output CSV in the same order.
    """
    results = OrderedDict()
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]                  # student name
            scores = list(map(float, row[1:]))  # convert scores to float
            avg = mean(scores)             # calculate average
            results[name] = avg
    # Write results to output CSV
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, avg in results.items():
            writer.writerow([name, avg])


# -----------------------------
# Task 2: Sort students by average score (ascending)
# -----------------------------
def calculate_sorted_averages(input_file_name, output_file_name):
    """
    Sort students by average score (ascending), then by name,
    and write the results to output CSV.
    """
    results = []
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            scores = list(map(float, row[1:]))
            avg = mean(scores)
            results.append((name, avg))
    results.sort(key=lambda x: (x[1], x[0]))  # sort by average, then name
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, avg in results:
            writer.writerow([name, avg])


# -----------------------------
# Task 3: Top 3 students
# -----------------------------
def calculate_three_best(input_file_name, output_file_name):
    """
    Find the top 3 students with the highest averages,
    sorted by average descending and then name.
    """
    results = []
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            scores = list(map(float, row[1:]))
            avg = mean(scores)
            results.append((name, avg))
    results.sort(key=lambda x: (-x[1], x[0]))  # descending order
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, avg in results[:3]:
            writer.writerow([name, avg])


# -----------------------------
# Task 4: Bottom 3 averages
# -----------------------------
def calculate_three_worst(input_file_name, output_file_name):
    """
    Find the 3 lowest averages (ignoring names)
    and write them to output CSV.
    """
    results = []
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            scores = list(map(float, row[1:]))
            avg = mean(scores)
            results.append(avg)
    results.sort()  # ascending order
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for avg in results[:3]:
            writer.writerow([avg])


# -----------------------------
# Task 5: Overall average of averages
# -----------------------------
def calculate_average_of_averages(input_file_name, output_file_name):
    """
    Calculate the mean of all students' averages
    and save the result to output CSV.
    """
    all_averages = []
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            scores = list(map(float, row[1:]))
            avg = mean(scores)
            all_averages.append(avg)
    overall_average = mean(all_averages)
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([overall_average])


# -----------------------------
# Run all tasks
# -----------------------------
if __name__ == "__main__":
    calculate_averages(INPUT_FILE, OUTPUT_TASK1)
    calculate_sorted_averages(INPUT_FILE, OUTPUT_TASK2)
    calculate_three_best(INPUT_FILE, OUTPUT_TASK3)
    calculate_three_worst(INPUT_FILE, OUTPUT_TASK4)
    calculate_average_of_averages(INPUT_FILE, OUTPUT_TASK5)

    print("All tasks completed. Output files are created in the current folder.")
