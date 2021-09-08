#Predefinig Values
import random
possibilities = [1,2,3,4,5,6,7,8,9,10]
choice1 = 0
runsP = 0
runsC = 0
choice2 = 0
wicket = 0
cpuchoices = ["Bat","bat","Ball","ball"]
cpuwin = ""
choiceUSER = 0
choicecpu = 0
total = 0
PlayerChoice = ""

#Intro
print("Welcome to ODD-EVE")

#Odd-Even battle
oechoice = input("You choose odd or even ? (answer : odd/Odd/even/Even) : ")

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

#Seperations
print()
print("___________________________________________________________________________________________________________________________________")
print()


##User Batting First
#Batting
if(PlayerChoice == "bat" or PlayerChoice == "Bat"):
    print("You are batting ! ")
    wicket=0
    while(wicket < 1):
        choice2 = int(input("Whats your choice : "))
        choice1 = random.choice(possibilities)
        if(choice2 == choice1):
            wicket = wicket + 1
            print("Your Choice : ", choice2)
            print("Ballers Choice : ", choice1)
            print("Ohh ! The cpu struck you out at ",runsP," runs !")
            print()
            print("___________________________________________________________________________________________________________________________________")
            print()
            print("You are balling now")
            break
        else:
            wicket = 0
            runsP = runsP + choice2
            print("Your Choice : ", choice2)
            print("Ballers Choice : ", choice1)
            print("You're Safe , current runs : ", runsP)

#Balling
    wicket = 0        
    print("Now its youre turn for balling !")
    while(wicket < 1):
        choice1 = random.choice(possibilities)
        choice2 = int(input("Whats your choice : "))
        if(choice1 == choice2):
            wicket = 1
            print("Your Choice : ", choice2)
            print("Batters Choice : ", choice1)
            print()
            print("___________________________________________________________________________________________________________________________________")
            print()            
            print("Amazing ! You struck the cpu out at ",runsC," runs !")
            break
        else:
            wicket = 0
            runsC = runsC + choice1
            print("Your Choice : ", choice2)
            print("Batters Choice : ", choice1)            
            print("You havent struck the batter out yet , batters current runs : ", runsC)

##Player Balling First 
#Balling       
elif(PlayerChoice == "ball" or PlayerChoice == "Ball"):       
    print("You are Balling!")
    wicket = 0
    while(wicket < 1):
        choice1 = random.choice(possibilities)
        choice2 = int(input("Whats your choice : "))
        if(choice1 == choice2):
            wicket = 1
            print("Your Choice : ", choice2)
            print("Batters Choice : ", choice1)
            print("Amazing ! You struck the cpu out at ",runsC," runs !")
            print()
            print("___________________________________________________________________________________________________________________________________")
            print()            
            print("You are batting now !")
            break
        else:
            wicket = 0
            runsC = runsC + choice1
            print("Your Choice : ", choice2)
            print("Batters Choice : ", choice1)            
            print("You havent struck the batter out yet , batters current runs : ", runsC)

#Batting
    print("Now its your turn for batting!")
    wicket=0
    while(wicket < 1):
        choice2 = int(input("Whats your choice : "))
        choice1 = random.choice(possibilities)
        if(choice2 == choice1):
            wicket = wicket + 1
            print("Your Choice : ", choice2)
            print("Ballers Choice : ", choice1)
            print()
            print("___________________________________________________________________________________________________________________________________")
            print()
            print("Ohh ! The cpu struck you out at ",runsP," runs !")
            break
        else:
            wicket = 0
            runsP = runsP + choice2
            print("Your Choice : ", choice2)
            print("Ballers Choice : ", choice1)
            print("You're Safe , current runs : ", runsP)


#Invalid choice
else:
    print("Please Make a Valid Choice , or check if there are any spelling mistakes, terminating the program .!")

#Outro
print("The round is over !")
print("Your runs , " , runsP)
print("CPU's runs , " , runsC)

if(runsP > runsC):
    print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗")
    print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║")
    print(" ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║")
    print("  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║")
    print("   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║")
    print("   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝")

elif(runsP < runsC) :
    print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗")
    print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝")
    print(" ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║   ")
    print("  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║   ")
    print("   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║   ")
    print("   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ")

else:
    print("The game was interrupted !")