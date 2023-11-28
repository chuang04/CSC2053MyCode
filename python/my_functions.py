# Calum Huang
# Citations: Rephactor

import random

def randomValue(list):
    
    list2 = [] #Making a second list

    for i in range(len(list)):                      # Making a loop to mix up the list inputted
        rand = random.randrange(0,len(list))        # Randomizing indexes
        list2.append(list[rand])                    # Adding Randomized Input
        list.pop(rand)                              # Removing Used Item
    
    #print (list2)                                  # Checking if the list is randomized


    return list2[random.randrange(0,len(list2))]    # Return a random num from the randomized list

print (randomValue([1,3,5,6,78,23]))                # Prints the randomized num from randomized list
print (randomValue([1,5,24,23,7,2]))
print (randomValue([11,33,54,66,90,234]))

def rollDaDice (numRolls, totWanted, sides):        # Rolling a Dice to and trying to get close to the number you want
    total = 0                                       # Tracking Total

    for i in range(numRolls):                       # Rolling number of times you want
        total += random.randrange(1,sides)          # Randomizing each roll
    
    return "The average value was " + str(abs(total/numRolls)) + ". \nYou were " + str(abs(totWanted - total)) +" off from the number you wanted."
# Returning the result

print (rollDaDice (3, 15, 6))                       # Printing the result   
print (rollDaDice (4, 12, 6))
print (rollDaDice (40, 240, 12))                                      