#W1D2 SE116 Review Demo - split into parts in Canvas

#Bradley Coppinger 
#Lab 2a 
#7/17/24

#Program Promt: Calculator from F to C coversion that averages all temps entered

#Variable Dictory


#------Functions--------------------------------

import csv

total_records = 0
room_over = 0
sum_age = 0

with open("Week2\lab2a.csv") as list:

    file = csv.reader(list)

    for record in file:

        print(f"{record[0]:20}, {record[1]:10}, {record[2]:4}")
        sum_age += int(record[2])
        total_records += 1

print("\n\nFile processing complete.")

avg_age = sum_age / total_records
print(f"\n\nAverage Age in file: {avg_age:.2f}")