#W2D1 mini demo - intro to text file handling

import csv

total_records = 0
sum_age = 0

with open("Week2/week2_practice.csv") as poop:

    file = csv.reader(poop)

    for record in file:

        print(f"{record[0]:10}, {record[2]:4}")
        sum_age += int(record[2])
        total_records += 1

print("\n\nFile processing complete.")

avg_age = sum_age / total_records
print(f"\n\nAverage Age in file: {avg_age:.2f}")