#Just a reminder, the tuples are in the order of:
#HP,MAXHP,ATK,ATKBON,DEF,MP,MAXMP,MPBON,SPD

#The rework of this on a basic level
#We learned that we can set multiple variables with one def command
#So a combat command will be the main center of this
#Along with an attack command, magic command, etc.
#The main control structures we use in this utilize Correct variables
#They are used for controling which while loop we are in, and they are all just Booleans

#Imports random, which is used to generate random numbers used for combat within the game
#Imports time, which is used in a LOT of spots in the code, it's used for timings between text
#Imports sys, IDK what it does. All I know is that it's used in the q command
import random, time, sys

#COMMANDS#
#Commands used everywhere
def q(str, temporal_distance = 0.02):

    #Not sure how this works, all I know is that it does
    #Lets the text roll instead of being printed all at once
    for char in str:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(temporal_distance)
def explode():

    #Basically a self destruct button
    #Useful if something seems impossible, but could have unforseen consequences if that is bypassed
    #Have no idea how it works
    #Useful for testing
    print("Something went wrong\nrunning explode()")
    try:
        explode()
    except:
        explode()
def wait(temporal_distance = .15):

    #Literally just laziness. I don't want to write time.sleep(.15) every second when I can just write wait()
    time.sleep(temporal_distance)
def confirm(str, temporal_distance = .5):
    
    #Used to provide a visual indicator that the user needs to continue
    #All games have an arrow that tells you you need to press A to continue
    q(str)
    input(' >')
    time.sleep(temporal_distance)
def ask(question, temporal_distance = .5):

    #Asks a question an keeps asking until the user gives a numerical input
    ec = True
    while ec:
        try:
            q(question)
            option = int(input(''))
            time.sleep(temporal_distance)
            ec = False
        except ValueError:
            wait(.5)
            q("Please give a number.\n")
            ec = True
    return option

#Commands used as chunks of the game
def charSelect(player):
    
    q("1: Knight\n")
    wait()
    q("2: Peashooter\n")
    wait()
    q("3: Rouge\n")
    wait()
    q("4: Mage\n")
    wait()
    q("5: Skele\n")
    wait()
    q("6: Bard\n")
    wait()
    q("7: Barbarian\n")
    wait()
    q("8: Random")
    wait()

    #CharacterCorrect
    cc = True
    while cc:
        option = ask("Please pick a class, player " + str(player) + ": ")
        
        #RandomCorrect
        rc = True
        while rc:
            #Knight
            if option == 1:
                stats = tuple[35,35,7,5,16,5,5,2,3]
                rc = False
            
            #Peashooter
            elif option == 2:
                stats = tuple[26,26,9,4,14,7,7,3,5]
                rc = False
            
            #Rouge
            elif option == 3:
                stats = tuple[20,20,10,6,13,6,6,2,7]
                rc = False

            #Mage
            elif option == 4:
                stats = tuple[21,21,5,2,11,10,10,5,4]
                rc = False
            
            #Skele
            elif option == 5:
                stats = tuple[30,30,7,3,12,7,7,5,6]
                rc = False
            
            #Bard
            elif option == 6:
                option = ""
                stats = tuple[27,27,6,4,14,4,4,2,2]
                rc = False
            
            #Barbarian
            elif option == 7:
                option = "Barbarian"
                stats = tuple[40,40,12,2,15,2,2,1,1]
                rc = False
            
            #Random
            elif option == 8:
                option = random.randint(1,7)
            
            #-.- --- -. .- -- .. ....... -.-. --- -.. .
            elif option == 88224646790:
                option = "-.- --- -. .- -- .. ....... -.-. --- -.. ."
                stats = tuple[88224646790,88224646790,88224646790,88224646790,88224646790,88224646790,88224646790,88224646790,88224646790]
                rc = False
            
            else:
                q("Please give a valid opiton\n")
                wait(.3)
        ync = True
        while ync:
            q("1: Yes\n")
            wait()
            q("2: No\n")
            wait()
            yesorno = ask("You have chosen the " + str(option) + " class, is this correct?")
            
            #Yes
            if yesorno == 1:
                q("Player " + str(player) + " has chosen the " + str(option) + " class\n")
                wait(.5)
                ync = False
                cc = False
            
            #No
            elif yesorno == 2:
                q("Repick your character\n")
                wait(.3)
                ync = False
                cc = True
            
            #Invalid input
            else:
                q("Please give a valid option\n")
                ync = True
    return stats
def random_num(min,max,show,ad = 0):
    if ad == 1:
        num1 = random.randint(min,max)
        num2 = random.randint(min,max)
        critnum = max(num1,num2)
    elif ad == 2:
        num1 = random.randint(min,max)
        num2 = random.randint(min,max)
        critnum = min(num1,num2)
    else:
        critnum = random.randint(min,max)
    if show:
        q("You rolled a: " + str(critnum))
    return critnum
def combat():
    
    #OptionCorrect
    oc = True
    while oc:
        q("1: Attack\n")
        wait()
        q("2: Magic\n")
        wait()
        q("3: Item\n")
        wait()
        q("4: Pass\n")
        wait()
        q("5: Run\n")
        wait()
        option = ask("What would you like to do? ")
        
        #Attack
        if option == 1:
            critnumber = random_num(1,20,atk_ad,show)
            
            #You need to see what you rolled here
            if not show:
                q("You rolled a " + str(critnumber) + "!\n")
            
            #Critical hit
            if critnumber == 20:
                q("It's a critical hit!\n")
                wait(.3)
                confirm("Player " + str(atkP) + " did " + str(atkATK*2) + " damage to player " + str(defP) + ".")
                defHP = defHP - (atkATK*2)
                oc = False
            
            elif critnumber + atkATK_BON >= defDEF:
                confirm("You landed a hit, doing " + str(atkATK) + " damage to player " + str(defP) + ".")
                defHP = defHP - atkATK
                oc = False
            
            elif critnumber + atkATK_BON < defDEF:
                confirm("You missed your attack.")
                oc = False
            
            else:
                explode()




#Setting default rule values
print_random = False

#THE GAME#
q("Welcome to Dungeons and Damage\n")
wait(.5)
q("Not to be confused with Dungeons and Dragons\n")
wait(.5)
q("Although this game does feel like it.")
wait(.5)
q("\n")
wait(.3)

#The big ol' all correct
#The main loop that lets the people playing go back to the start of the game if they so wish
ac = True
while ac:
    
    #Reseting variables
    #Under the for loop to be colapsable
    for i in range(1):
        P1AD = 0
        P2AD = 0
        P1ADTR = 0
        P2ADTR = 0
        P1DMGBOOST = 0
        P2DMGBOOST = 0
        P1SPOONS = 0
        P2SPOONS = 0
        P1KNIVES = 0
        P2KNIVES = 0
        P1POTS = 0
        P2POTS = 0
        P1GLOCK = 0
        P2GLOCK = 0
        P1WINS = 0
        P2WINS = 0

    q("1: Game Start\n")
    wait()
    q("2: Guide\n")
    wait()
    q("3: Options\n")
    wait()
    q("4: Quit\n")
    wait()
    option = ask("Please select an option: ")
    
    #Guide
    if option == 2:
        q("Guide coming soon\n")
    
    #Options
    elif option == 3:
        q("Options coming soon\n")
    
    elif option == 4:
        ac = False
    
    elif option == 1:
        q("Set character classes and then let the combat commence")
    
    else:
        q("Please provide a given number")