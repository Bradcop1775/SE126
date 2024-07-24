#W1D2 SE116 Review Demo - split into parts in Canvas

#Bradley Coppinger 
#Lab 2a 
#7/24/24

#Program Promt: he csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event. Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit

#Variable Dictory
#total_records = total number of rooms processed
#over_cap = determine if room is over capacity 
#room_limit = limit of room 

#------Functions--------------------------------

import csv

total_records = 0
over_cap = 0
room_limit = 0

print("Welcome to the over checker!")
print("---------------------------")
print(f"{'Room':20}{'Max':5}{'Min':5}")
print("---------------------------")
with open("Week2\lab2a.csv") as list:

    file = csv.reader(list)

    for record in file:
        total_records += 1

    #print(f"{record[0]:20}, {record[1]:10}, {record[2]:4}")
        if record[2] > record [1]:
            room_limit += 1 
            print(f"\n{record[0]:20}{record[1]:5}{record[2]:5}")
            over_cap = int(record[1]) - int(record[2])
            print(f"\nYour room is over by: {abs(over_cap)} people\n------------------------------------")
            

print(f"\nYou have processed {total_records} rooms. \n\n\nWARNING: \n*********** You have {room_limit} rooms over limit ************")

print("\n\nFile processing complete.")

#avg_age = sum_age / total_records
