#W2D2 SE116 

#Bradley Coppinger 
#Lab 2b 
#7/24/24

#Program Promt: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output.  The last line should print the number of computers in the file.

#Variable Dictory
#type = rec[0], type of machine 
#brand = rec[1], brand name 
#cpu = rec [2], CPU it has 
#ram = rec [3], Ram it has 
#1st disk = rec [4], Disk installed
#No HDD - rec [5], determines if extra disk is in
#2nd disk - rec [6 or 7, based on boolian of HDD], size of 2nd disk
#os - rec [6 or 7, based on boolian of HDD], operating system
#yr - rec [7 or 8, based on boolian of HDD], operating system
#------Functions--------------------------------
#NO FUNCTIONS
#IMPORT
import csv
#------MAIN CODE--------------------------------
with open("Week2/lab2b.csv") as list:
    file = csv.reader(list)

    print(f"{'Type':10} {'Brand':10} {'CPU':10} {'RAM':10} {'1st Disk':10} {'No HDD':10} {'2nd Disk':10} {'OS':10} {'YR':10}")
    
    for rec in file:

        machine = rec[0] #CHANGE TO COMPUTER MANUFACTURER
        if rec[0] == "D":
            machine = "Desktop"
        else:
            machine = "Laptop"
        
        brand = rec[1] #CHANGE TO FULL BRAND NAME
        if rec[1] =="DL":
            brand = "Dell"
        elif rec[1] == "HP":
            brand = "HP"
        else: 
            brand = "Gateway"

        cpu = rec[2]  #DEFINE RECORD AS NAME 
        ram = rec[3]
        disk1 = rec[4]
        numdisk = int(rec[5])

        if numdisk ==1: #CHANGES RECORD NUMBER IF DISK2 IS TRUE 
            disk2 = " n/a"
            os = rec[6]
            year = rec[7]
        else: 
            disk2 = rec[6]
            os = rec[7]
            year = rec[8]
#-------------------ENDING CODE-------------------------------------
        print(f"{machine:10} {brand:10} {cpu:10} {ram:10} {disk1:10} {numdisk:3}        {disk2:10} {os:10} {year:10}")



