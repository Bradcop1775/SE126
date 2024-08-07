#W4D2 - 1D, 2D Lists, Hand-Populated, Random and Sequential Search 

import random

#create some hand populated 1D Lists
dragon_names = [
    "Drogon", 
    "SilverWing", 
    "Vermithor", 
    "Syrax", 
    "Meleys"
    ]
#Below list is parallell - match to list
dragon_alias = [
    "The Good Boi",
    "The Silver Lady",
    "The Bronze Fury",
    "The Goddess",
    "The Red Queen"
]

records = len(dragon_names) #record = 5

#display parllel list with corresponding values
print(f"{"Names":12} \t\t{"ALIAS"}")
print("--------------------------------------------")
for i in range(0, records):
    print(f"{dragon_names[i]:12} AKA \t{dragon_alias[i]}")
print("--------------------------------------------")

#use a random function to populate a new list of dragon "ages"
dragon_ages = []
for i in range(0, len(dragon_names)):
    #the quick way!
    dragon_ages.append(random.randint(0, 500))


for i in range(0, len(dragon_names)):
    print(f"{dragon_names[i]:12}     \t{dragon_ages[i]:5} y.o.")

#add all of the 1D list to  new list to create a 2D list!

'''
dragon_info = [
    dragon_names,
    dragon_alias,
    dragon_ages
]
'''
dragon_info = []
for i in range(0, len(dragon_names)):
    #print(f"{dragon_info[i]}")
    dragon_info.append([dragon_names[i], dragon_alias[i], dragon_ages[i]])



#2d list
print("---------- 2D DRAGON LIT-----------")
for i in range(0, len(dragon_info)):
    print(f"REC # {i} LIST: {dragon_info[i]}") #prints list with full "".""

    for x in range(0, len(dragon_info[i])):
        #for every item in the current list, display it!
        print(f"{dragon_info[i][x]:10}", end = ' ') #end='' removes new line 

    print() #new line
print("---------- END 2D DRAGON LIT-----------")

#sequential search (beginning to end)

#get search value
search_dragon = input("Who are you looking for?: ")

#create variable to hold found data
found = "n/a"


#search through list
for i in range(0, len(dragon_names)):
    #search -------> if
    if search_dragon.lower() == dragon_names[i].lower():
        #store IDEX to dound
        found = i
        break #if multiples do not use

#check to see if value has been found 
if found != "n/a":
    print(f"Your search for {search_dragon} was FOUND in record #{found}")
    #display ALL data
    print(f"Name: {dragon_names[found]} \t Alias: {dragon_alias[found]} \t Age: {dragon_ages[found]}")
else:
    print(f"Sorry your search for {search_dragon} was *NOT* FOUND.")
