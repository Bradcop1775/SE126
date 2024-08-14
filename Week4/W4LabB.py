#W4D1 Class Lab

#Bradley Coppinger 
#Lab 4B
#8/14/24

#In Python, process the text file “lab4A_GOT_NEW.txt” to store each field into its own corresponding list

#Variable list
#firstNames = first name
#lastNames = last name
#Age = age 
#Nickname = nickname
#House = house person is in
#stark = house Stark
#watch = Night's Watch house
#tully = House Tully
#lanister = House Lanister
#targaryen = House Targaryen
#baratheon = House Baratheon
#motto = House Motto
#total_number_of_people = person count 
#avg_Age = average age 

#-----------------------------------------------------------------

import random 
import csv 

#create empty lists - one for EACH potential field
firstNames = []
lastNames = []
Age = []
Nickname = []
House = []
stark = 0
watch = 0
tully = 0
lanister = 0
targaryen = 0
baratheon = 0
motto = []
total_number_of_people = 0
avg_Age = 0



#connected to file----------------------------------
with open("Week4\lab4A_GOT_NEW.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: 
        #'file' is an example of a 2D list XD
        firstNames.append(rec[0])
        lastNames.append(rec[1])
        Age.append(int(rec[2]))
        Nickname.append(rec[3])
        House.append(rec[4])
#DISconnected to file----------------------------------

print(f"{"FIRST":10}\t{"LAST":10}\t{"Age":3}\t{"Nickname":3}\t\t{"House":3}")
print("-------------------------------------------------------------------------------")

#process list --> FOR LOOP!
for i in range(0, len(firstNames)):
    print(f"{firstNames[i]:10}\t{lastNames[i]:10}\t{Age[i]:3}\t{Nickname[i]:20}\t{House[i]:25}")
print("-------------------------------------------------------------------------------")
print("\n\n*******************************************************************************")

#process lists to find numeric and letter grade equivalent for each student 

#RE-PROCCESS LIST 
for i in range(0, len(firstNames)):
    if House[i] == "House Stark":
        houseMotto = "Winter is Coming"
        stark += 1
    elif House[i] == "Night's Watch":
        houseMotto = "And now my watch begins"
        watch += 1
    elif House[i] == "House Tully":
        houseMotto = "Family. Duty. Honor"
        tully += 1
    elif House[i] == "House Lannister":
        houseMotto = "Hear me roar!"
        lanister += 1
    elif House[i] == "House Targaryen":
        houseMotto = "Fire & Blood"
        targaryen += 1
    elif House[i] == "House Baratheon":
        houseMotto = "Ours is the fury"
        baratheon += 1
    motto.append(houseMotto)
        
print(f"\n{"FIRST":10}\t{"LAST":10}\t{"Age":3}\t{"Nickname":3}\t\t{"House":3}\t\t\t{"Moto":25}")
print("--------------------------------------------------------------------------------------------------------------------")

for i in range(0, len(firstNames)):
    print(f"{firstNames[i]:10}\t{lastNames[i]:10}\t{Age[i]:3}\t{Nickname[i]:20}\t{House[i]:25}{motto[i]}")
print("--------------------------------------------------------------------------------------------------------------------")
print("\n\n********************************************************************************************************************")

#Reprocess list 

total_number_of_people = len(firstNames)
print(f"There are {total_number_of_people} total number of people.")

avg_Age = int(sum(Age)) / len(Age)
print(f"The average age is: {avg_Age:.0f}.")
 
print(f"The number of allegances are: \nHouse Stark: {stark}\nNight's Watch: {watch}\nHouse Tully: {tully}\nHouse Lannister: {lanister}\nHouse Targaryen: {targaryen}\nHouse Baratheon: {baratheon}")