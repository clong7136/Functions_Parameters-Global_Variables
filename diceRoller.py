import random,time
#these are dice faces
s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n" 
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def rollDice():
    print("Rolling.....")
    roll = random.randint(1,6) #makes random integer

    return roll


def diceshow(roll):
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4: 
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)
    else:
        print("Something is wrong with this code.")
        print(roll) #Small debug tool

def 2inrow():
    howManyRolls=int(input("How many times would you like to roll? > "))
    prevRoll="0"
    for x in range(howManyRolls):
        myRoll=rollDice()
        time.sleep(1)
        diceshow(myRoll)
        #print(myRoll) #debug
        if prevRoll==myRoll:
            print("You win life. Grats.")
            break
        prevRoll=myRoll

def when6():
    howManyRolls=int(input("How many times would you like to roll? > "))
    prevRoll="0"
    for x in range(howManyRolls):
        myRoll=rollDice()
        time.sleep(1)
        diceshow(myRoll)
        #print(myRoll)
        if myRoll==6:
            print("You win.")
            break

whichGame=str(input("Would you like it to stop at 2 in a row (t), \nOr when you get a six (s)? > "))
if whichGame=="t":
    2inrow() 
elif whichGame=="s":
    when6()   
