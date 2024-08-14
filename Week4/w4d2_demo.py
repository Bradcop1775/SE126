#W4D2 - 1D, 2D Lists, Hand-Population, Random, n Sequential Search

import random 

#create some hand-populated 1D lists
dragon_names = [
    "Drogon", 
    "Silverwing", 
    "Vermithor", 
    "Syrax", 
    "Meleys"
    ]
#below list is PARALLEL -> if you find a dragon_name at index 2, its dragon_alias is also found at index 2
dragon_alias = [
    "The Good Boi", 
    "The Silver Lady", 
    "The Bronze Fury",
    "The Goddess",
    "The Red Queen"
]

records = len(dragon_names) #records = 5 

#simply display the parllel lists with each corresponding values on its own line
print(f"{"NAMES":12}     \t{"ALIAS"}")
print("------------------------------------------------")
for i in range(0, records):
    print(f"{dragon_names[i]:12} AKA \t{dragon_alias[i]}")
print("------------------------------------------------\n")

#"formal" and long way to add value to the new list 
'''
dragon_ages[0] = random.randint(0, 500)
dragon_ages[1] = random.randint(0, 500)
dragon_ages[2] = random.randint(0, 500)
dragon_ages[3] = random.randint(0, 500)
dragon_ages[4] = random.randint(0, 500)
'''

#use a random function to populate a new list of dragon "ages"
dragon_ages = []
for i in range(0, len(dragon_names)):
    #the quick way!
    dragon_ages.append(random.randint(0, 500))


for i in range(0, len(dragon_names)):
    print(f"{dragon_names[i]:12}     \t{dragon_ages[i]:5}y.o.") 



#add all of the 1D lists to a new list, creating a 2D list!
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

print("\n\n---DRAGON INFO & 2D LISTS--------------------------------")
#processing 2D lists (processing a list that is populated with more lists)
for i in range(0, len(dragon_info)):
    print(f"\nREC# {i} LIST: {dragon_info[i]}") #this prints the full list w/ ['','']

    for x in range(0, len(dragon_info[i])):
        #for every item in the current list, display it!
        print(f"{dragon_info[i][x]:10}", end = " ") 
        #end=" " removes new line at end of print()
    
    print()#creates a new line before next list in list
print("-------------------------------------------------------------")



#SEQUENTIAL SEARCH: to search "in sequence" --> from beginning [0] to end [len(listName) - 1]; use an IF to determine IF the search query is equal to a value within the list you're searching through

#get search value (query) from user
search_dragon = input("Who are you looking for?")

#create a variable to hold the "found" data, if found
found = "n/a"

#search through the list to see if it's there
for i in range(0, len(dragon_names)):

    #SEARCH --> IF
    if search_dragon.lower() == dragon_names[i].lower():
        #store the INDEX to 'found' variable
        found = i

#check to see if value has been found
if found != "n/a":
    print(f"Your search for {search_dragon} was FOUND in record #{found}")
    #display ALL data for found dragon
    print(f"NAME:{dragon_names[found]} \t ALIAS:{dragon_alias[found]} \t AGE:{dragon_ages[found]}")
else:
    print(f"Sorry, your search for {search_dragon} was *NOT* FOUND.")


#strings are just lists!
print(f"{dragon_names[0][0]}") #displays 'D' since it is the first character in the first value within the dragon_names list


#sneak peek into Dictionaries ... 
shepherd = {
    #"key": "value" --> keys MUST be string, values can be anything!
    "name": "George",
    "age": "11",
    "color": "black & white",
    "treat": "cheese",
    "toy": "bone"
}

pithound = {
    "name": "Marlowe",
    "age": "5",
    "color": "tan & white",
    "treat": "peanut butter",
    "toy": "baby"
}

tuxedo = {
    "name": "Stevie",
    "age": "1.5",
    "color": "black & white",
    "treat": "tuna",
    "toy": "mr. fox"
}

pets = [shepherd, pithound, tuxedo]

for i in range(0, len(pets)):

    for key in pets[i]:
        print(f"{key.upper()}: {pets[i].get(key)}", end = " ")
