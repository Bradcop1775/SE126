#W5D2 = Comparing Searching Methods: Sequential vs Binary

import csv

#create empty list
id_student = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open("Week5/w5_demoFile.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #remeber file is 2D

        id_student.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

#disconnected from file -- check list

print(f"{"ID#":5}\t{"Last":15}\t{"First":15}")
print("---------------------------------------------")
for i in range(0, len(id_student)):
    print(f"{id_student[i]:5}\t{lname[i]:15}\t{fname[i]:15}")
print("------------------------------------------------------------")

#searching always get the search item first
#sequential search

search_name = input("Enter the LAST NAME you are looking for: ")
found = -1
seq_count = 0

#for loop allow review of each value in list
for i in range(0, len(lname)):
    seq_count += 1
    #ask if search value matches current value in list (search)
    if search_name.lower() == lname[i].lower():
        #store the found values LOCATION [index]
        found = i

print(f"\n\tSequential Search Complete. Loop ran {seq_count} iterations.")
if found != -1:
    print(f"\n\tWe found {search_name} at index position {found}")
    print(f"\tHere is there info: ")

    print(f"{id_student[found]:5}\t{lname[found]:15}\t{fname[found]:15}")
else:
    print(f"\n\tWe could not find {search_name}")
    print("\tPleae check your spelling and try again.")

#BINARY SEARCH -- ORDERED LIST and divide into two sections (high, low) and based on a MIDDLE POINT will continually halve the search pool until  unqie value is found or isn't

min = 0
max = len(lname) - 1
mid = int((min + max) /2 )

bin_count = 0

#here is the algorithim for INCREASING (ascending) ordered list
while (min < max and search_name.lower() != lname[mid].lower()):
    #both of these must be true for search to contineL min index is still less than the max index and the query has not been found
    bin_count += 1
    if search_name.lower() < lname[mid].lower():
        #revalue the max to be in the middle 
        max = mid - 1
        

    else:
        #revalue the min the be in the middle 
        min = mid + 1

    #you must revalue the mid before the ext loop
    mid = int((min + max) /2)

print(f"\n\tBinary Search Complete. Loop ran {bin_count} iterations.")
if search_name.lower() == lname[mid].lower():
    print(f"\n\tWe found {search_name} at index position {mid}")
    print(f"\tHere is there info: ")

    print(f"{id_student[mid]:5}\t{lname[mid]:15}\t{fname[mid]:15}")
else:
    print(f"\n\tWe could not find {search_name}")
    print("\tPleae check your spelling and try again.")