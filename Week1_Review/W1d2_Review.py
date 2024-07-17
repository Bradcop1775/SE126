#W1D2 SE116 Review Demo - split into parts in Canvas

#Bradley Coppinger 
#Lab 1 / Demo 1
#7/17/24

#Program Promt: Calculator from F to C coversion that averages all temps entered

#Variable Dictory


#------Functions--------------------------------
def converter(f):

    '''This function is passed a temp F value, converts to C, and returns said value'''
    c = (f - 32) * (5/9)

    return c #literally returns to the point of function call

#------Main Code--------------------------------

#initializing known or needed values
tempCount = 0
tempSum = 0

degree = u'\N{DEGREE SIGN}'


answer = "y"

while answer == "y" or answer == "Y":

    tempF = float(input(f"\t\tEnter Tempature #{tempCount+1} in Fahrenheit: "))

    tempCount += 1 #tempCount = tempCount + 1 
    tempSum += tempF #tempSum = tempSum + tempF

    #convert F to C
    #tempC = (tempF - 32) * (5/9)

    tempC = converter(tempF)

    print(f"\tTemperature {tempF:.1f}  |  {tempC:.1f}{degree}C")



    
    #build a way out!
    answer = input("Would you like to enter another temp> [y/n]: ").lower()

    #error trap
    while answer.lower() != "y" and answer.lower() !="n" and answer.lower() != "yes" and answer.lower() !="no":
        print("\t\t***INVALID ENTRY***")
        answer = input("Would you like to enter another temp> [y/n]: ").lower()




if tempCount !=0:
    avgTemp = tempSum / tempCount
    avgC = converter(avgTemp)

    print(f"\n\n You have entered {tempCount} tempatures for an average of {avgTemp:.1f}) {degree}F    |   {avgC:.1f}{degree}C")

else:
    print("\n\n\n\tWhy would you use me?")




