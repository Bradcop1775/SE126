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

def decision(response):  #This will be response 
    while response.lower() != "y" and response.lower() !="n" and response.lower() != "yes" and response.lower() !="no":
        print("\t\t***INVALID ENTRY***")
        response = input("Do you want to check another room? Please enter 'Y' or 'N': ").lower()
    return response


#Variable Dictory

    #ans = answer 
    #people = # of people
    #max_Cap = Maximum capacity of room
    #OccupencyDiff is comparision for people and room cap
    #continueLoop - ask if you want to continue 

#------Main Code--------------------------------
#Initial Values
ans = "y"
max_Cap = 0
people = 0

#Main Code Start 
print("Welcome to the Capacity Checker. Please follow the prompts below:")
time.sleep(3)

while ans == "y" or ans == "Y":
    
    try:
        max_Cap = int(input(("What is the maximum number of occupency? ")))
        print(f"You enetered {max_Cap} for the maximum occupency.")
        people = int(input("Enter number of people: "))
        print(f"You entered {people} people")
        OccupencyDiff = difference(people,max_Cap)
        if OccupencyDiff >=0:
            print(f"The room meets requirments by {abs(OccupencyDiff)}.")

        else:
            print(f"WARNING: The room is over by {abs(OccupencyDiff)}.")
           

    except ValueError:
        print(f"The people value MUST be a number")


    continueLoop = input("Do you want to check another room? Please enter 'Y' or 'N': ")
    ans=decision(continueLoop)
    #ans = decision(ans)
    

print("Thank you for using our program!")


    
#END OF CODE