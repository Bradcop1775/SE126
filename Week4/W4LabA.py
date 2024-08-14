#W4D1 Class Lab

#Bradley Coppinger 
#Lab 4A
#8/14/24

#Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.

#Variable list
#firstNames = first name on list
#lastNames = last names on list
#test1 = test1 score
#test2 = test2 score
#test3 = test3 score
#numAvg = Average of test scores 
#avg = grade avg

import csv 

#create empty lists - one for EACH potential field
firstNames = []
lastNames = []
test1 = []
test2 = []
test3 = []

#we will also create data and append to these belows
numAvg = []
letAvg = []

#connected to file----------------------------------
with open("Week4\listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: 
        #'file' is an example of a 2D list XD
        firstNames.append(rec[0])
        lastNames.append(rec[1])
        #will be mathematically processing test data -- > cast int()
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#DISconnected to file----------------------------------

print(f"{"FIRST":10}\t{"LAST":10}\t{"T#1":3}\t{"T#2":3}\t{"T#3":3}")
print("-----------------------------------------------------------")
#process list --> FOR LOOP!
for i in range(0, len(firstNames)):
    print(f"{firstNames[i]:10}\t{lastNames[i]:10}\t{test1[i]:3}\t{test2[i]:3}\t{test3[i]:3}")
print("-----------------------------------------------------------")

#process lists to find numeric and letter grade equivalent for each student 
for i in range(0, len(firstNames)):

    avg = (test1[i] + test2[i] + test3[i]) / 3

    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    #finish the grade equivalents for HW :]
    else:
        letter = "F"

    #adding num and let avg to respective lists; these remain PARALLEL with starting data
    numAvg.append(avg)
    letAvg.append(letter)   

#reprocess to print & display new data
print(f"{"FIRST":10}\t{"LAST":10}\t{"T#1":3}\t{"T#2":3}\t{"T#3":3}\t{"AVG.":5}\t{"LETTER":3}")
print("-------------------------------------------------------------------------------")
#process list --> FOR LOOP!
for i in range(0, len(firstNames)):
    print(f"{firstNames[i]:10}\t{lastNames[i]:10}\t{test1[i]:3}\t{test2[i]:3}\t{test3[i]:3}\t{numAvg[i]:5.1f}\t{letAvg[i]:3}")
print("-------------------------------------------------------------------------------")
#process lists to find class average; display data at end
gradeTotal = 0

for i in range(0, len(numAvg)):
    #add each student's numAvg to the gradeTotal variable
    gradeTotal += numAvg[i]

classAvg = gradeTotal / len(numAvg)

print(f"\n\tThere are {len(numAvg)} students in the class\n\tThe Class Average is: {classAvg:.1f}\n\n")