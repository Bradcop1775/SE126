#Week 3 Day 2 -- Practicing with LISTS

import csv

#count the number of records in the file
records = 0

#prep some *empty* lists
name = []
age = []
animal = []
color = []
number = [] 

with open("Week3\classList_202140.txt") as csvfile: 

    file = csv.reader(csvfile)

    for rec in file:
        #everything in this file happens to EACH record in the file
        records += 1 

        #store data into the lists 
        name.append(rec[0])
        age.append(int(rec[1]))
        animal.append(rec[2])
        color.append(rec[3])
        #number.append(rec[4])


#disconnected from the file

#list processing -- FOR LOOP!
for i in range(0, records):

    print("INDEX: {0}\t{1}\t{2}\t{3:8}\t{4}\t{5}".format(i, name[i], age[i], animal[i], color[i], number[i]))


#i = 0 

#while i < records:

    #print("INDEX: {0}\t{1}\t{2}\t{3:8}\t{4}\t{5}".format(i, name[i], age[i], animal[i], color[i], number[i]))

    #i += 1 



#process the age list to determine the average age in the class 

total_age = 0

for i in range(0, records):

    print("INDEX: {0} TOTAL_AGE: {1} PERSON: {2} AGE:{3}".format(i, total_age, name[i], age[i]))

    #add each person's age to the total_age
    total_age += age[i]

#after the for loop, i retains the value of the last index within the lists
print("VALUE OF i AFTER FOR LOOP EXIT: ", i)

average_age = total_age / records 
print("\tTOTAL RECORDS: {0}".format(records))
print("\tAVERAGE AGE: {0:.2f}".format(average_age))

#count how many of each favorite animal type there are
#initializing counters for each potential animal type
dog = 0 
cat = 0
tiger = 0
elephant = 0
bird = 0
chicken = 0
bunny = 0
horse = 0
bat = 0

#process the animal list to determine how many people prefer each animal
for i in range(0, records):

    if animal[i] == "Dog":

        dog+= 1
    
    if animal[i] == "Cat":

        cat += 1

    if animal[i] == "Tiger":

        tiger += 1

    if animal[i] == "Elephant":

        elephant += 1

    if animal[i] == "Bird":

        bird += 1

    if animal[i] == "Chicken":

        chicken += 1

    if animal[i] == "Bunny":

        bunny += 1

    if animal[i] == "Horse":

        horse += 1

    if animal[i] == "Bat":

        bat += 1

print("\nBUNNY: ", bunny)
print("DOG: ", dog)
print("CAT: ", cat)
print("HORSE: ", horse)
print("BIRD: ", bird)
print("TIGER: ", tiger)
print("ELEPHANT: ", elephant)
print("CHICKEN: ", chicken)




#process the favorite number list to find the average favorite number, rounded to the nearest whole number

total_num = 0

for i in range(0, records):

    total_num += int(number[i])

avg_num = total_num / records 

print("AVG FAVE NUMBER: {0:.2f}".format(avg_num))

#length function -- find the number of items in an element 
total_records = len(name)

print("TOTAL RECORDS: {0} == RECORDS {1}".format(total_records, records))