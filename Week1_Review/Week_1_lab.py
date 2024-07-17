#W1D2 SE126 Lab 1

#Bradley Coppinger 
#Lab 1 
#7/17/24

#Program Promt: You will be writing one Python file for this project - it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.




#import
import time

#------Functions--------------------------------
def difference(people, max_cap):  #This will show people compared to mak cap
    diff = max_cap - people

    return diff
#test for function
#print (f"People: 30, Room Cap: 50, Diff: {difference(30, 50)}")

def decision(response): 
    while ans.lower() != "y" and ans.lower() !="n" and ans.lower() != "yes" and ans.lower() !="no":
        print("\t\t***INVALID ENTRY***")
        answer = input("Would you like to enter another temp> [y/n]: ").lower()


#Variable Dictory

    #ans = answer 
    #people = # of people
    #max_Cap = Maximum capacity of room
    #OccupencyDiff is comparision for people and room cap

#------Main Code--------------------------------
ans = "y"
max_Cap = 0
people = 0
ans2 = "y"
ans3 = "y"
print("Welcome to the Capacity Checker. Please follow the prompts below:")
#time.sleep(3)

while ans == "y":
    max_Cap = int(input(("What is the maximum number of occupency? ")))
    print(f"You enetered {max_Cap} for the maximum occupency.")

    #while ans2 == "y":
    try:
        people = int(input("Enter number of people: "))
        print(f"You entered {people} people")
        OccupencyDiff = difference(people,max_Cap)
        if OccupencyDiff <=0:
            print(f"The room meets requirments by {difference}.")
            #ans3 = input((f"{decision}"))
        else:
            print(f"WARNING: The room is over by {difference}.")
            #ans3 = input((f"{decision}"))

    except:
        print(f"The people value MUST be a number")


    ans=input("Do you want to check another room?: ")
    ans = decision(ans)


    
#initializing known or needed values