#Importing
import random

#Giving and Predefining Values
possibilities = [1,2,3,4,5,6,7,8,9,10]
cpuchoices = ["Bat","bat","Ball","ball"]
cpuwin = ""
oechoice = input("You choose odd or even ? (answer : odd/Odd/even/Even) : ")
choiceUSER = 0
choicecpu = 0
total = 0
PlayerChoice = ""

#Main Body

#If user chooses odd
if(oechoice == "odd" or oechoice == "Odd"):
    choiceUSER = int(input("Whats your choice ? :"))
    choicecpu = random.choice(possibilities)
    print("CPU chose ",choicecpu)
    total = choiceUSER + choicecpu
    if(total%2 == 0):
        print("CPU won the odd even battle , cpu will now choose between batting or balling .")
        cpuwin = random.choice(cpuchoices)
        print("CPU chose to first ",cpuwin)
        if(cpuwin == "bat" or cpuwin == "Bat"):
            PlayerChoice = "ball"
        else:
            PlayerChoice = "bat"
        print("Hence , you are gonna , ", PlayerChoice)
    elif(total%2 == 1):
        PlayerChoice = input("You won the odd even battle , what are you going to chose first between bat/ball ? : ")

#If user chooses even
elif(oechoice == "even" or oechoice == "Even"):
    choiceUSER = int(input("Whats your choice ? :"))
    choicecpu = random.choice(possibilities)
    print("CPU chose ",choicecpu)
    total = choiceUSER + choicecpu
    if(total%2 == 1):
        print("CPU won the odd even battle , cpu will now choose between batting or balling .")
        cpuwin = random.choice(cpuchoices)
        print("CPU chose to first ",cpuwin)
        if(cpuwin == "bat" or cpuwin == "Bat"):
            PlayerChoice = "ball"
        else:
            PlayerChoice = "bat"
        print("Hence , you are gonna , ", PlayerChoice)
    elif(total%2 == 0):
        PlayerChoice = input("You won the odd even battle , what are you going to chose first between bat/ball ? : ")

#If user chooses something wrong
else:
    print("!! You didnt choose a right option !!")
