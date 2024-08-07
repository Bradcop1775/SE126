#W2D2 SE116 

#Bradley Coppinger 
#Lab 3B 
#8/7/24

#This lab is a continuation of the Voter Registration Lab from SE116.  The original prompt is as follows: (Source: QBasic Fundamentals and Style, Quasney, Maniotes, Foremant; P. 190 #3) Construct a program that will analyze potential voters. The program should generate the following totals:
# Number of individuals not eligible to register.
# Number of individuals who are old enough to vote but have not registered.
# Number of individuals who are eligible to vote but did not vote.
# Number of individuals who did vote.
# Number of records processed.

import csv

Voter_ID = []
Age = []
Register = []
Voted = []

allowed_to_vote = 0
are_registered = 0
voted_yes = 0 
total_records = 0
notEligable = 0
notRegistered = 0
notVoted = 0

with open ("Week3/voters_202040.csv", "r") as f:
    reader = csv.reader(f)
    for record in reader:
        total_records +=1
        Voter_ID.append(record[0])
        Age.append(int(record[1]))
        Register.append(record[2])
        Voted.append(record[3])


for i in range (0,total_records):
    if (Age[i]) >= 18:
        allowed_to_vote += 1
    if (Register[i]) == "Y":
        are_registered += 1
    if (Voted[i]) == "Y":
        voted_yes += 1
        
notEligable = total_records - allowed_to_vote
notRegistered = allowed_to_vote - are_registered
notVoted = are_registered - voted_yes

print(f"Total Records: {total_records:5} Allowed to vote but not Registered: {notRegistered:5} Eligable and did not vote: {notVoted:5} Voted: {voted_yes:5} Not eligable to register: {notEligable:5}")


# Number of individuals not eligible to register.
# Number of individuals who are old enough to vote but have not registered.
# Number of individuals who are eligible to vote but did not vote.
# Number of individuals who did vote.
# Number of records processed.