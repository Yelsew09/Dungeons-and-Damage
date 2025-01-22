#A big part of this game's loop control are Correct variables
#These are just variables with a binary (0 or 1) value.
#They allow the user to correct a bad input or lead them to a specific part of the program
#It's the break and continue commands with an argument you can put in

#Imports random, which is used to generate random numbers used for combat within the game
#Imports time, which is used in a LOT of spots in the code, it's used for timings between text
#Imports sys, IDK what it does. All I know is that it's used in the q command
import random, time, sys

def q(str,temporal_distance = .02):
    
    #Not entirely sure what this all does, all I know is that it rolls text instead of printing it all at once.
    for char in str:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(temporal_distance)
def explode():

    #A command used for crashing the game. Very useful if something seems impossible
    #Basically a failsafe
    #I have no clue how it works
    print("Something went wrong. exploding...")
    try:
        explode()
    except:
        explode()
def wait(temporal_distance = .15):
    
    #Literally just laziness. I don't want to type time.sleep(.15) every second
    time.sleep(temporal_distance)
def confirm(str, temporal_distance = .5):
    
    #Used as that arrow confirmation found in text bubbles in video games
    q(str)
    input(' >')
    time.sleep(temporal_distance)
def critnum(AD,num1,num2,show):
    
    #Used to generate random numbers
    #If advantage isn't being used, put 0 in for the first number
    if AD == 1:
        critnumber1 = random.randint(num1,num2)
        critnumber2 = random.randint(num1,num2)
        if critnumber1 > critnumber2:
            critnumber = critnumber1
        elif critnumber2 > critnumber1:
            critnumber = critnumber2
        else:
            critnumber = critnumber1
    elif AD == 2:
        critnumber1 = random.randint(num1,num2)
        critnumber2 = random.randint(num1,num2)
        if critnumber1 > critnumber2:
            critnumber = critnumber2
        elif critnumber2 > critnumber1:
            critnumber = critnumber1
        else:
            critnumber = critnumber2
    else:
        critnumber = random.randint(num1,num2)
    if show:
        confirm("You rolled a " + str(critnumber) + "\n")
    return critnumber
def ask(question, temporal_distance = .5):
    
    #Ask. Replaces error correct
    #Asks a question and repeats until the user gives a numerical input
    ec = 0
    while ec == 0:
        try:
            q(question)
            option = int(input(''))
            time.sleep(temporal_distance)
            ec = 1
        except ValueError:
            wait(.5)
            q("Please give a number.\n")
            ec = 0
    return option

#Do you want to see random numbers after their generated or not?
print_random = False

#THE GAME
q("Welcome to Dungeons and Damage.\n")
wait(.5)
q("Not to be confused with Dungeons and Dragons.\n")
wait(.5)
q("There are no dungeons here, but there is a lot of damage.\n")
wait(.5)
q("Informally known as HELL.\n")
wait(.5)

#AllCorrect. The main while loop that loops the ENTIRE PROGRAM
ac = 0
while ac == 0:
    
    #Reseting everything
    for i in range (1):
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
    
    q("1: Play the game\n")
    wait()
    q("2: Guide\n")
    wait()
    q("3: Options\n")
    wait()
    q("4: Quit\n")
    wait()
    option = ask("What would you like to do? ")

    #Guide
    if option == 2:
        confirm("Guide coming soon")

    #Options
    elif option == 3:
        q("0: Cancel\n")
        wait()
        q("1: Print randomly generated numbers. Currently set to - " + str(print_random) + "\n")
        wait()
        
        #MenuCorrect
        #I know it's MagicCorrect later, but we'll ignore that
        mc = 0
        while mc == 0:
            option = ask("What would you like to change? ")
            
            #Cancel
            if option == 0:
                mc = 1
            
            #Print random numbers
            elif option == 1:
                
                #Set to false
                if print_random:
                    q("print_random has been set to False\n")
                    print_random = False
                    mc = 1
                
                #Set to True
                elif not print_random:
                    q("print_random has been set to True\n")
                    print_random = True
                    mc = 1
                
                else:
                    explode()
            
            #Text speed
            elif option == "Yes":
                
                #OptionCorrect. Used for when the user could give a bad input
                oc = 0
                while oc == 0:
                    q("text_speed is currently set to " + str(text_speed) + "\n")
                    option = ask("How fast would you like to scroll the text? ")
                    
                    #Too slow
                    if option >= 1:
                        confirm("That's too slow. Please give a number lower than that.")
                    
                    #0 or below
                    elif option <= 0:
                        text_speed = .02
                    
                    else:
                        q("1: Yes\n")
                        wait()
                        q("2: No\n")
                        wait()
                        text_speed = option

                        #YesNoCorrect
                        ync = 0
                        while ync == 0:
                            yesorno = ask("Is this a good speed? ")
                            
                            #Yes
                            if yesorno == 1:
                                q("This is now the new text speed\n")
                                ync = 1
                                oc = 1
                            
                            #No
                            elif yesorno == 2:
                                text_speed = .02
                                q("Please choose a new text speed\n")
                                ync = 1
                            
                            else:
                                q("Please give a valid option\n")
            
            else:
                q("Please give an option we can use.")
                wait(.5)
            

    #Ends program
    elif option == 4:
        #Ends program
        ac = 1


    elif option == 1:

        #Starts the game part of the program
        #GameCorrect. Allows for someone to go back and play the game again if they want to. 
        gc = 0
        while gc == 0:
            q("1: Knight\n")
            wait()
            q("2: Peashooter\n")
            wait()
            q("3: Mage\n")
            wait()
            q("4: Rouge\n")
            wait()
            q("5: Skele\n")
            wait()
            q("6: Bard\n")
            wait()
            q("7: Barbarian\n")
            wait()
            q("8: Random\n")

            #OptionCorrect
            #Character select for player 1
            oc = 0
            while oc == 0:

                option = ask("Please select a class, player 1. ")
                
                #RandomCorrect. Used specifically here and used for determining a random character
                rc = 0
                while rc == 0:
                    
                    if option == 1:
                        option = "Knight"
                        P1HP = 42
                        P1MAXHP = P1HP
                        P1ATK = 12
                        P1ATKBON = 2
                        P1DEF = 14
                        P1MP = 4
                        P1MPBON = 1
                        P1MAXMP = P1MP
                        P1SPD = 3
                        rc = 1
                    
                    elif option == 2:
                        option = "Peashooter"
                        P1HP = 35
                        P1MAXHP = P1HP
                        P1ATK = 10
                        P1ATKBON = 1
                        P1DEF = 14
                        P1MP = 5
                        P1MPBON = 1
                        P1MAXMP = P1MP
                        P1SPD = 6
                        rc = 1
                    
                    elif option == 3:
                        option = "Mage"
                        P1HP = 29
                        P1MAXHP = P1HP
                        P1ATK = 7
                        P1ATKBON = 2
                        P1DEF = 10
                        P1MP = 20
                        P1MPBON = 5
                        P1MAXMP = P1MP
                        P1SPD = 2
                        rc = 1
                    
                    elif option == 4:
                        option = "Rouge"
                        P1HP = 31
                        P1MAXHP = P1HP
                        P1ATK = 13
                        P1ATKBON = 4
                        P1DEF = 14
                        P1MP = 6
                        P1MPBON = 1
                        P1MAXMP = P1MP
                        P1SPD = 7
                        rc = 1
                    
                    elif option == 5:
                        option = "Skele"
                        P1HP = 33
                        P1MAXHP = P1HP
                        P1ATK = 20
                        P1ATKBON = 6
                        P1DEF = 20
                        P1MP = 15
                        P1MPBON = 3
                        P1MAXMP = P1MP
                        P1SPD = 4
                        rc = 1
                    
                    elif option == 6:
                        option = "Bard"
                        P1HP = 37
                        P1MAXHP = P1HP
                        P1ATK = 7
                        P1ATKBON = 1
                        P1DEF = 13
                        P1MP = 14
                        P1MPBON = 4
                        P1MAXMP = P1MP
                        P1SPD = 5
                        rc = 1
                    
                    elif option == 7:
                        option = "Barbarian"
                        P1HP = 52
                        P1MAXHP = P1HP
                        P1ATK = 14
                        P1ATKBON = 2
                        P1DEF = 11
                        P1MP = 2
                        P1MPBON = .25
                        P1MAXMP = P1MP
                        P1SPD = 4
                        rc = 1
                    
                    elif option == 88224646790:
                        option = "-.- --- -. .- -- .. ....... -.-. --- -.. ."
                        P1HP = 88224646790
                        P1MAXHP = P1HP
                        P1ATK = 88224646790
                        P1ATKBON = 88224646790
                        P1DEF = 88224646790
                        P1MP = 88224646790
                        P1MPBON = 88224646790
                        P1MAXMP = P1MP
                        P1SPD = 88224646790
                        rc = 1
                    
                    elif option == 8:
                        option = random.randint(1,7)
                    
                    else:
                        confirm("Please choose a valid option")
                        rc = 1
                
                #YesNoCorrect. Used for a yes/no situation
                ync = 0
                while ync == 0:
                    q("1: Yes\n")
                    wait()
                    q("2: No\n")
                    wait()
                    yesorno = ask("Player 1 has choesn the " + str(option) + " class. Is this correct? ")
                    
                    if yesorno == 1:
                        confirm("Player 1 has chosen the " + str(option) + " class.")
                        ync = 1
                        oc = 1
                    
                    elif yesorno == 2:
                        confirm("Repick your character.")
                        oc = 0
                        ync = 1
                    
                    else:
                        q("Pleae give a valid number.\n")
                        wait(.5)

            #OptionCorrect
            #Character select for player 2
            oc = 0
            while oc == 0:
                q("1: Knight\n")
                wait()
                q("2: Peashooter\n")
                wait()
                q("3: Mage\n")
                wait()
                q("4: Rouge\n")
                wait()
                q("5: Skele\n")
                wait()
                q("6: Bard\n")
                wait()
                q("7: Barbarian\n")
                wait()
                q("8: Random\n")
                wait()
                
                option = ask("Please select a class, player 2. ")
                
                #RandomCorrect
                rc = 0
                while rc == 0:
                    
                    if option == 1:
                        option = "Knight"
                        P2HP = 42
                        P2MAXHP = P2HP
                        P2ATK = 12
                        P2ATKBON = 2
                        P2DEF = 14
                        P2MP = 4
                        P2MPBON = 1
                        P2MAXMP = P2MP
                        P2SPD = 3
                        rc = 1
                    
                    elif option == 2:
                        option = "Peashooter"
                        P2HP = 35
                        P2MAXHP = P2HP
                        P2ATK = 10
                        P2ATKBON = 1
                        P2DEF = 14
                        P2MP = 5
                        P2MPBON = 1
                        P2MAXMP = P2MP
                        P2SPD = 6
                        rc = 1
                    
                    elif option == 3:
                        option = "Mage"
                        P2HP = 29
                        P2MAXHP = P2HP
                        P2ATK = 7
                        P2ATKBON = 2
                        P2DEF = 10
                        P2MP = 20
                        P2MPBON = 5
                        P2MAXMP = P2MP
                        P2SPD = 2
                        rc = 1
                    
                    elif option == 4:
                        option = "Rouge"
                        P2HP = 31
                        P2MAXHP = P2HP
                        P2ATK = 13
                        P2ATKBON = 4
                        P2DEF = 14
                        P2MP = 6
                        P2MPBON = 1
                        P2MAXMP = P2MP
                        P2SPD = 7
                        rc = 1
                    
                    elif option == 5:
                        option = "Skele"
                        P2HP = 33
                        P2MAXHP = P2HP
                        P2ATK = 20
                        P2ATKBON = 6
                        P2DEF = 20
                        P2MP = 15
                        P2MPBON = 3
                        P2MAXMP = P2MP
                        P2SPD = 4
                        rc = 1
                    
                    elif option == 6:
                        option = "Bard"
                        P2HP = 37
                        P2MAXHP = P2HP
                        P2ATK = 7
                        P2ATKBON = 1
                        P2DEF = 13
                        P2MP = 14
                        P2MPBON = 4
                        P2MAXMP = P2MP
                        P2SPD = 5
                        rc = 1
                    
                    elif option == 7:
                        option = "Barbarian"
                        P2HP = 52
                        P2MAXHP = P2HP
                        P2ATK = 14
                        P2ATKBON = 2
                        P2DEF = 11
                        P2MP = 2
                        P2MPBON = .25
                        P2MAXMP = P2MP
                        P2SPD = 4
                        rc = 1
                    
                    elif option == 88224646790:
                        option = "-.- --- -. .- -- .. ....... -.-. --- -.. ."
                        P2HP = 88224646790
                        P2MAXHP = P2HP
                        P2ATK = 88224646790
                        P2ATKBON = 88224646790
                        P2DEF = 88224646790
                        P2MP = 88224646790
                        P2MPBON = 88224646790
                        P2MAXMP = P1MP
                        P2SPD = 88224646790
                        rc = 1
                    
                    elif option == 8:
                        option = random.randint(1,7)
                    
                    else:
                        q("Please choose a valid option.\n")
                        rc = 1
                        wait(.5)
                
                #YesNoCorrect
                ync = 0
                while ync == 0:
                    q("1: Yes\n")
                    wait()
                    q("2: No\n")
                    wait()
                    yesorno = ask("Player 2 has chosen the " + str(option) + " class, is this correct? ")
                    
                    if yesorno == 1:
                        confirm("Player 2 has chosen the " + str(option) + " class.")
                        oc = 1
                        ync = 1
                    
                    elif yesorno == 2:
                        confirm("Repick your character.")
                        ync = 1

                    else:
                        q("Please give an option we can use.\n")
                        wait(.5)


            #CombatCorrect. Used for combat
            #Will stop when either or both characters reach 0 HP
            cc = 0
            while cc == 0:
                turn = 0
                if P1SPD > P2SPD:

                    #Player 1's turn when they go first
                    #Otherwise just setting up variables for the turn
                    items_left = 3
                    turn = turn + 1
                    q("This is turn " + str(turn) + "\n")
                    wait(.3)
                    q("Player 1 has + " + str(P1HP) + "/" + str(P1MAXHP) + "HP left, and " + str(P1MP) + "/" + str(P1MAXMP) + "MP left")
                    confirm("Player 2 has + " + str(P2HP) + "/" + str(P2MAXHP) + "HP left, and " + str(P2MP) + "/" + str(P2MAXMP) + "MP left", .3)

                    #OptionCorrect to mark the start of the turn
                    oc = 0
                    while oc == 0:
                        q("This is Player 1's turn\n")
                        wait()
                        q("1: Attack\n")
                        wait()
                        q("2: Magic\n")
                        wait()
                        q("3: Use an item\n")
                        wait()
                        q("4: Pass turn\n")
                        wait()
                        option = ask("What would you like to do? ")

                        #Attack
                        if option == 1:

                            critnumber = critnum(P1AD,1,20,print_random)
                            
                            #Even if you don't want to see a random number printed, you need to see this one
                            if not print_random:
                                confirm("You rolled a " + str(critnumber))

                            #Critical hit
                            if critnumber == 20:
                                confirm("IT'S A CRITICAL HIT!!!", .15)
                                confirm("Player 1 did " + str(P1ATK*2) + " damage to player 2")
                                P2HP = P2HP - (P1ATK*2)
                                oc = 1
                                
                            #Hit
                            elif critnumber + P1ATKBON > P2DEF:
                                confirm("Player 1 landed a hit, doing " + str(P1ATK) + " damage to Player 2.")
                                P2HP = P2HP - P1ATK
                                oc = 1
                                
                            #Miss
                            elif critnumber + P1ATKBON < P2DEF:
                                confirm("Player 1 missed their attack.")
                                oc = 1
                                
                            #If all else fails...
                            else:
                                explode()
                            P1ATKBON = 0
                            
                        #Magic
                        elif option == 2:
                            q("1: Fireball - 5MP\n")
                            wait()
                            q("2: Summon a random item - 2MP\n")
                            wait()
                            q("3: Gain advantage on your next turn - 5MP\n")
                            wait()
                            q("4: Impose disadvantage on your opponent's next turn - 5MP\n")
                            wait()
                            q("5: Heal 20 percent of your max health - 5MP\n")
                            wait()
                            q("6: Gain a damage boost on your next attack - Varies\n")
                            wait()
                            q("Currently 7: Spell descriptions\n")
                            wait()
                            q("0: Cancel\n")
                            wait()
                                
                            #MagicCorrect. We can't use OptionCorrect, so we have to use a more specific variable
                            #On a basic level, its purpose is the same as OptionCorrect
                            mc = 0
                            while mc == 0:   
                                option = ask("What would you like to do? ")
    
                                #Fireball - 5MP
                                if option == 1:
                                        
                                    #Not enough MP
                                    if P1MP < 5:
                                        confirm("You don't have enough MP for that.")
                                    
                                    else:
                                        critnumber = critnum(0,round(P1MAXMP/2),P1MAXMP,print_random)

                                        #If the magic is so bad, it will get blocked
                                        if round(P2DEF/4) >= critnumber:
                                            confirm("Your opponent's defence blocked the " + str(critnumber) + " damage you tried to do.")
                                        
                                        #If you are competent enough to make an effective fireball
                                        else:
                                            confirm("Player 1 did " + str(critnumber) + " damage to player 2.")
                                            P2HP = P2HP - critnumber
                                            P1MP = P1MP - 5
                                            oc = 1
                                            mc = 0

                                #Make a random item - 2MP
                                elif option == 2:

                                    #Not enough MP
                                    if P1MP < 2:
                                        confirm("You don't have enough MP for that.")
                                        
                                    else:
                                        critnumber = critnum(0,1,100,print_random)
                                        q("You conjured up ")
                                            
                                        #If critnumber is between 1 and 10:
                                        #Rusty Spoon
                                        if critnumber >= 1 and critnumber <= 10:
                                            q("a... ")
                                            wait(.5)
                                            q("Rusty...", .5)
                                            wait(.6)
                                            confirm("Spoon?")
                                            P1SPOONS = P1SPOONS + 1
                                            
                                        #If critnumber is between 11 and 55:
                                        #Throwing knives
                                        elif critnumber >= 11 and critnumber <= 55:
                                            confirm("a few throwing knives")
                                            P1KNIVES = P1KNIVES + 3
                                            
                                        #If critnumber is between 56 and 99:
                                        #Healing potion
                                        elif critnumber >= 56 and critnumber <= 99:
                                            confirm("a healing potion!")
                                            P1POTS = P1POTS + 1
                                            
                                        #HE HAS A GUN
                                        elif critnumber == 100:

                                            #If P2 has a gun, now they both do
                                            if P1GLOCK == 0 and P2GLOCK == 1:
                                                q("Ok, great. Now the OTHER guy has a gun.\n", .2)
                                                wait(.5)
                                                confirm("I'm leaving.", .2)
                                                P1GLOCK = P1GLOCK + 1
                                                
                                            #If P1 already had a gun
                                            elif P1GLOCK > 0:
                                                q("You did it again.\n", .4)
                                                wait(1)
                                                q("Landed a 1 in 100 chance to get a literal GUN.\n", .3)
                                                wait(.5)
                                                q("That thing could've won you the game intstanly.\n", .1)
                                                wait(.3)
                                                wait()
                                                q("And you kept going.\n", .1)
                                                wait(2)
                                                q("\n")
                                                print("WHY?!?!?")
                                                wait(.5)
                                                q("Alright, I'm ending this here and now.\n")
                                                wait(.8)
                                                confirm("God landed a destructive hit, doing " + str(999+P2HP) + " damage to player 2.", 1)
                                                P2HP = P2HP - P2HP
                                                for i in range (5):
                                                    print("Calculating, please wait.")
                                                    wait(.5)
                                                    print("Calculating failed.")
                                                    wait(.3)
                                                    if i > 5:
                                                        print("Retrying...")
                                                        wait(.2)
                                                confirm("Player 2 has ValueError HP left.")
                                                
                                            #The first gun in the game
                                            elif P1GLOCK == 0 and not P2GLOCK == 1:
                                                wait(.3)
                                                print("GUN?!?!?!?")
                                                wait(.3)
                                                q("Like, not even an old gun, like a musket.\n")
                                                wait(.3)
                                                q("It's just a Glock-19\n")
                                                wait(.3)
                                                confirm("I quit")
                                                P1GLOCK = P1GLOCK + 1
                                                
                                            #If all else fails...
                                            else:
                                                explode()
                                        
                                        #If all else fails...
                                        else:
                                            explode()
                                        oc = 1
                                        P1MP = P1MP - 2
                                        mc = 1

                                #Gain advantage - 5MP
                                elif option == 3:
                                    
                                    #Not enough MP
                                    if P1MP < 5:
                                        confirm("You don't have enough MP for that")
                                        
                                    else:
                                        confirm("You gained advantage on your next turn.")
                                        P1AD = 1
                                        P1ADTR = 2
                                        oc = 1
                                        P1MP = P1MP - 5
                                        mc = 1
                                    
                                #Impose disadvantage - 5MP
                                elif option == 4:

                                    #Not enough MP
                                    if P1MP < 5:
                                        confirm("You don't have enough MP for that.")

                                    else:

                                        #If Player 2 already had advantage
                                        if P2AD == 1:
                                            confirm("You got rid of Player 2's advantage.")
                                            P2AD = 0
                                            P2ADTR = 0

                                        #If Player 2 had no advantage
                                        elif P2AD == 0:
                                            confirm("You gave Player 2 disadvantage on their next turn.")
                                            P2AD = 2
                                            P2ADTR = 1

                                        #If Player 2 already had disadvantage
                                        elif P2AD == 2:
                                            confirm("You continued Player 2's disadvantage into their next turn.")
                                            P2AD = 2
                                            P2ADTR = 1
                                        oc = 0
                                        P1MP = P1MP - 5
                                    mc = 1

                                #Heal 20% of max HP - 5MP
                                elif option == 5:

                                    #Not enough MP
                                    if P1MP < 5:
                                        confirm("You don't have enough MP for that.")
                                    
                                    #Already at max health
                                    elif P1HP >= P1MAXHP:
                                        confirm("You are already at maximum HP.")
                                        P1HP = P1MAXHP
                                    
                                    else:
                                        HEAL = round(P1MAXHP/5)
                                        confirm("You healed " + str(HEAL) + " damage.", .2)
                                        P1HP = P1HP + HEAL

                                        #If healing would put you over your MAXHP
                                        if P1HP > P1MAXHP:
                                            confirm("But, that would've brought you over your maximum health.", .2)
                                            P1HP = P1MAXHP
                                        wait(.3)
                                        P1MP = P1MP - 5
                                        oc = 1
                                    mc = 1

                                #Damage boost - Varies
                                elif option == 6:

                                    #If P1 has NO MP
                                    if P1MP < 1:
                                        confirm("You have no MP, so therefor you cannot use this spell.")

                                    else:
                                        q("For every 4 MP you put into this spell, you will get a +1.25 damage boost to your next attack.\n")
                                        wait()
                                        P1DMGBOOST = ask("How much MP would you like to put into this spell (0 to cancel)? ")

                                        #Cancel
                                        if P1DMGBOOST == 0:
                                            q("You canceled your damage boost.\n")

                                        else:

                                            #If P1 tries to spend more MP than they have
                                            if P1MP < P1DMGBOOST:
                                                confirm("You don't have enough MP for that amount of damage boost.")
                                            
                                            #Sucess!
                                            else:
                                                P1MP = P1MP - P1DMGBOOST
                                                P1DMGBOOST = round(P1DMGBOOST * 1.25)
                                                confirm("You gained a buff of +" + str(P1DMGBOOST) + " damage on your next attack.")
                                                mc = 1
                                                oc = 1
                                                
                                #Spell descriptions
                                elif option == 7:
                                    q("Spell descriptions: \n")
                                    wait()
                                    q("Fireball - 5MP. Create a ball of fire that crashes down on the target. This will do anywhere from half of your MAXMP to your MAXMP of almost unblockable damage. If you are to create a fireball that does so little damage, it will get blocked\n")
                                    wait()
                                    q("Conjure a random item - 2 MP. Conjure a random item that can be used on your next turn.\n")
                                    wait()
                                    q("Gain advantage - 5MP. Gain advantage until the end of your next turn. For more information on advantage, visit the guide in the Main Menu.\n")
                                    wait()
                                    q("Impose disavantage - 5MP. Give your opponent disavnatage on their next turn, or get rid of thier advantage. For more information on advnatages, visit the guide in the Main Menu.\n")
                                    wait()
                                    q("Heal 20 percent of MAXHP - 5MP. Heal 20 percent of your max HP. This cannot take you above your maximum, though.\n")
                                    wait()
                                    confirm("Damage boost - Varies. Put as much MP as you want (and can) into this move, and have that amount multiplied by 1.25 and added to your next attack.")
                                
                                #Cancel
                                elif option == 0:
                                    q("You cenceled your magic\n")
                                    wait()
                                    mc = 1
                                
                                else:
                                    q("Please give an option we can use.\n")
                                    wait(.5)

                        #Item
                        elif option == 3:

                            #If there are no item uses left and you just selected it from the menu
                            if items_left == 0:
                                confirm("You've used all your items this turn.")
                                ic = 0
                            
                            #If you have items left to use
                            else:
                                if not items_left == 3:
                                    confirm("You can use " + str(items_left) + " more items on this turn", .3)
                                q("1: Spoons - " + str(P1SPOONS) + "\n")
                                wait()
                                q("2: Knives - " + str(P1KNIVES) + "\n")
                                wait()
                                q("3: Healing Potions - " + str(P1POTS) + "\n")
                                wait()
                                
                                #Print properly if the gun is in play
                                if P1GLOCK >= 1:
                                    q("4: Glock 19\n")
                                    wait()
                                    q("5: Cancel\n")
                                
                                #Print properly if the gun is not in play
                                else:
                                    q("4: Cancel\n")
                                wait()
                                
                                #ItemCorrect
                                #The specific correct for item usage
                                ic = 0
                                while ic == 0:
                                    
                                    #If you just used an item and that was your last one
                                    if items_left == 0:
                                        ic = 1
                                        option = 0
                                    
                                    #If you have items left
                                    else:
                                        option = ask("What would you like to use? ")
                                        
                                        #Spoon
                                        if option == 1:
                                            
                                            #No spoons
                                            if P1SPOONS < 1:
                                                confirm("You don't have any spoons. No soup for you.")
                                            
                                            else:
                                                critnumber = critnum(0,1,1000,print_random)
                                                
                                                #The 1 in 1000 chance to kill player 2 with tetanus
                                                if critnumber == 1000:
                                                    confirm("Player 2 got tetanus from being hit with the spoon, dying on the spot.")
                                                    ic = 1
                                                    oc = 1
                                                    P2HP = P2HP - P2HP
                                                
                                                #The 1 in 1000 chance to die from tetanus due to holding the spoon
                                                elif critnumber == 1:
                                                    confirm("Player 1 got tetanus from holding the spoon, dying on the spot.")
                                                    ic = 1
                                                    oc = 1
                                                    P1HP = P1HP - P1HP
                                                
                                                #If it all goes normally
                                                else:
                                                    confirm("You threw a spoon, doing 1 point of damage to Player 2")
                                                    P2HP = P2HP - 1
                                                items_left = items_left - 1
                                                P1SPOON = P1SPOON - 1
                                        
                                        #Knife
                                        elif option == 2:
                                            
                                            #No knives
                                            if P1KNIVES < 1:
                                                input("You don't have any knives. Want a pencil instead? ")
                                                wait(.3)
                                                q("Well I don't have any.\n")
                                                wait(.5)
                                            
                                            else:
                                                critnumber = critnum(0,1,50,print_random)
                                                
                                                #Miss
                                                if critnumber == 50:
                                                    confirm("You threw a knive, completely missing your opponent.", .3)
                                                    items_left = items_left - 1
                                                
                                                #Hit
                                                else:
                                                    critnumber = critnum(0,1,5,print_random)
                                                    confirm("Player 1 threw a knife, doing " + str(critnumber) + " damage to player 2")
                                                    P2HP = P2HP - critnumber
                                                    P1KNIVES = P1KNIVES - 1
                                                    items_left = items_left - 1
                                        
                                        #Healing Potion
                                        elif option == 3:
                                            
                                            #No healing potions
                                            if P1POTS < 1:
                                                confirm("You don't have any healing potions.")
                                            
                                            #Already at max health
                                            elif P1HP >= P1MAXHP:
                                                confirm("You are already at maximum health.")
                                                P1HP = P1MAXHP
                                            
                                            else:
                                                HEAL = critnum(0,2,5,print_random)
                                                confirm("Player 1 healed " + str(HEAL) + " damage",2)
                                                
                                                #If healing would've brought you over maximum HP
                                                if P1HP > P1MAXHP:
                                                    confirm("But that would've taken you over your maximum HP.", .2)
                                                    P1HP = P1MAXHP
                                                wait(.3)
                                                P1POTS = P1POTS - 1
                                                items_left = items_left - 1
                                        
                                        #Shoot the gun (if you have it)
                                        elif option == 4 and P1GLOCK > 0:
                                            critnumber = critnum(0,1,1000)
                                            
                                            #You landed the 1 in 1000 chance to MISS
                                            if critnumber == 1:
                                                confirm("You missed.", .2)
                                                q("And that's the last shot in the clip.")
                                                wait(.5)
                                                confirm("My man really conjured up a one shot weapon with one shot")
                                                P1GLOCK = P1GLOCK - 1
                                            
                                            #So anyway, I started blasting
                                            else:
                                                confirm("Player 1 shot their gun, hitting player 2 and doing " + str(P2HP) + " damage to player 2")
                                                P1GLOCK = P1GLOCK - 1
                                                items_left = 0
                                        
                                        #Cancels item usage (if you have the gun)
                                        elif option == 5 and P1GLOCK > 0:
                                            q("You canceled your item usage\n")
                                            ic = 1
                                        
                                        #Cancels item usage (if you don't have the gun)
                                        elif option == 4 and not P1GLOCK > 0:
                                            q("You canceled your item usage\n")
                                            ic = 1
                                        
                                        else:
                                            q("Please give an option we can use.\n")

                        #Pass turn
                        elif option == 4:
                            q("You passed your turn.\n")
                            P1MP = P1MP + 1
                            if P1MP >= P1MAXMP:
                                P1MP = P1MAXMP
                            oc = 1
                            
                        #Not a valid input
                        else:
                            q("Please give an option we can use.\n")
                            ec = 0
                            oc = 0
                            wait(.5)
                    
                    #If player 1 is out of health
                    if P1HP <= 0:
                        confirm("Player 1 is out of health. They have lost the game.")
                        cc = 1
                        P2WINS = P2WINS + 1
                    
                    #If player 2 is out of health
                    elif P2HP <= 0:
                        confirm("Player 2 is out of health. They have lost the game.")
                        cc = 1
                        P1WINS = P1WINS + 1
                    
                    #Everyone's healthy
                    else:
                        q("Player 1 has + " + str(P1HP) + "/" + str(P1MAXHP) + "HP left, and " + str(P1MP) + "/" + str(P1MAXMP) + "MP left")
                        confirm("Player 2 has + " + str(P2HP) + "/" + str(P2MAXHP) + "HP left, and " + str(P2MP) + "/" + str(P2MAXMP) + "MP left", .3)

                        #OptionCorrect to mark the start of the turn
                        oc = 0
                        items_left = 3
                        while oc == 0:
                            q("Player 2's turn\n")
                            wait()
                            q("1: Attack\n")
                            wait()
                            q("2: Magic\n")
                            wait()
                            q("3: Use an item\n")
                            wait()
                            q("4: Pass turn\n")
                            wait()
                            option = ask("What would you like to do? ")
                            
                            #Attack
                            if option == 1:
                                critnumber = critnum(P2AD,1,20)
                                
                                #This is a neccisary print
                                if not print_random:
                                    q("You rolled a " + str(critnumber) + "\n")
                                
                                #CRITICAL HIT
                                if critnumber == 20:
                                    q("IT'S A CRITICAL HIT!!!!")
                                    wait(.3)
                                    confirm("Player 2 did " + str(P2ATK*2) + " damage to player 2.\n")
                                    P1HP = P1HP - P2ATK*2
                                    oc = 1
                                
                                #Hit
                                elif critnumber + P2ATKBON >= P1DEF:
                                    confirm("Player 2 landed a hit, doing " + str(P2ATK) + " damage to player 1.\n")
                                    P1HP = P1HP - P2ATK
                                    oc = 1
                                
                                #Miss
                                elif critnumber + P2ATKBON < P1DEF:
                                    q("Player 2 missed their attack.\n")
                                    oc = 1

                                #If all else fails...
                                else:
                                    explode()
                                P2DMGBOOST = 0
                            
                            #Magic
                            elif option == 2:
                                q("1: Fireball - 5MP\n")
                                wait()
                                q("2: Summon a random item - 2MP\n")
                                wait()
                                q("3: Gain advantage on your next turn - 5MP\n")
                                wait()
                                q("4: Impose disadvantage on your opponent's next turn\n")
                                wait()
                                q("5: Heal 20 percent of your max health - 5MP\n")
                                wait()
                                q("6: Gain a damage boost on your next - Varies\n")
                                wait()
                                q("Currently 7: Spell descriptions\n")
                                wait()
                                q("0: Cancel\n")
                                wait()
                                
                                #MagicCorrect
                                mc = 0
                                while mc == 0:
                                    option = ask("What would you like to do")
                                    
                                    #Fireball - 5MP
                                    if option == 1:
                                        
                                        #Not enough MP
                                        if P1MP > 5:
                                            q("You don't have enough MP for that.\n")
                                        
                                        else:
                                            critnumber = critnum(0,round(P2MAXMP/2),P2MAXMP,print_random)
                                            
                                            #If the magic was SO bad
                                            if critnumber <= P1DEF/4:
                                                q("That was pathetic. It didn't do anything.\n")
                                            
                                            else:
                                                q("Player 2 did " + str(critnumber) + " damage to player 1\n")
                                                P1HP = P1HP - critnumber
                                                P2MP = P2MP - 5
                                    
                                    #Random item
                                    elif option == 2:
                                        
                                        #Not enough MP
                                        if P2MP < 2:
                                            confirm("You don't have enough MP for that")
                                        
                                        else:
                                            critnumber = critnum(0,1,100,print_random)
                                            q("You conjured up ")
                                            
                                            #If critnumber is between 1 and 10:
                                            #Rusty Spoon
                                            if critnumber >= 1 and critnumber <= 10:
                                                q("a... ")
                                                wait(.5)
                                                q("Rusty...", .5)
                                                wait(.6)
                                                confirm("Spoon?")
                                                P2SPOONS + P2SPOONS + 1
                                            
                                            #If critnumber is between 11 and 55:
                                            #Throwing knives
                                            elif critnumber >= 11 and critnumber <= 55:
                                                confirm("a few throwing knives!")
                                                P2KNIVES = P2KNIVES + 3
                                            
                                            #If critnumber is between 56 and 99:
                                            #Healing potion
                                            elif critnumber <-56 and critnumber <= 99:
                                                confirm("a healing potion!")
                                                P2POTS = P2POTS + 1
                                            
                                            #HE HAS A GUN
                                            elif critnumber == 100:

                                                #If P1 has a gun, now they both do
                                                if P2GLOCK == 0 and P1GLOCK == 1:
                                                    q("Ok, great. Now the OTHER guy has a gun\n", .2)
                                                    wait(.5)
                                                    q("I'm leaving.", .2)
                                                
                                                #If P2 already had a gun
                                                elif P2GLOCK > 0:
                                                    q("You did it again.\n", .4)
                                                    wait(1)
                                                    q("Landed a 1 in 100 chance to get a literal GUN.\n", .3)
                                                    wait(.5)
                                                    q("That thing could've won you the game intstanly.\n", .1)
                                                    wait(.3)
                                                    wait()
                                                    q("And you kept going.\n", .1)
                                                    wait(2)
                                                    q("\n")
                                                    print("WHY?!?!?")
                                                    wait(.5)
                                                    q("Alright, I'm ending this here and now.\n")
                                                    wait(.8)
                                                    confirm("God landed a destructive hit, doing " + str(999+P1HP) + " damage to player 1.", 1)
                                                    P1HP = P1HP - P1HP
                                                    for i in range (5):
                                                        print("Calculating, please wait.")
                                                        wait(.5)
                                                        print("Calculating failed.")
                                                        wait(.3)
                                                        if i > 5:
                                                            print("Retrying...")
                                                        confirm("Player 1 has ValueError HP left.")
                                                
                                                #The first gun in the game
                                                elif P2GLOCK == 0 and not P1GLOCK == 1:
                                                    wait(.3)
                                                    print("GUN?!?!?!?")
                                                    wait(.3)
                                                    q("Like, not even an old gun, like a musket\n")
                                                    wait(.3)
                                                    q("It's just a Glock-19\n")
                                                    wait(.3)
                                                    confirm("I quit")
                                                    P2GLOCK = P2GLOCK + 1
                                                
                                                #If all else fails...
                                                else:
                                                    explode()
                                                oc = 1
                                                P2MP = P2MP - 2
                                                mc = 1
                                        
                                    #Gain advantage - 5MP
                                    elif option == 3:
                                        
                                        #Not enough MP
                                        if P2MP < 5:
                                            confirm("You don't have enough MP for that.")
                                        
                                        else:
                                            confirm("You gained advantage on your next turn.")
                                            P2AD = 1
                                            P2ADTR = 2
                                            oc = 1
                                            P2MP = P2MP - 5
                                            mc = 1
                                    
                                    #Impose disadvantage - 5MP
                                    elif option == 4:

                                        #Not enough MP
                                        if P2MP < 5:
                                            confirm("You don't have enough MP for that.")

                                        else:

                                            #If Player 1 already had advantage
                                            if P1AD == 1:
                                                confirm("You got rid of player 1's advantage.")
                                                P1AD = 0
                                                P1ADTR = 0
                                            
                                            #If Player 1 had no advantage
                                            elif P1AD == 0:
                                                confirm("You gave Player 1 disadvantage on their next turn.")
                                                P1AD = 2
                                                P1ADTR = 1
                                            
                                            #If Player 1 already had disadvantage
                                                confirm("You continued Player 1's disadvantage through their next turn.")
                                                P1AD = 2
                                                P1ADTR = 1
                                            oc = 0
                                            P1MP = P1MP - 5
                                        mc = 1

                                    #Heal 20% of max HP - 5MP
                                    elif option == 5:

                                        #Not enough MP
                                        if P2MP < 5:
                                            confirm("You don't have enough MP for that.")
                                        
                                        #Already at max health
                                        elif P2HP >= P2MAXHP:
                                            confirm("You are already at maximum HP.")
                                            P2HP = P2MAXHP
                                        
                                        else:
                                            HEAL = round(P2MAXHP/5)
                                            confirm("You healed " + str(HEAL) + " damage.", .2)
                                            P2HP = P2HP + HEAL

                                            #If healing would put you over your MAXHP
                                            if P2HP > P2MAXHP:
                                                confirm("But, that would've brought you over your maximum health.", .2)
                                                P2HP = P2MAXHP
                                            wait(.3)
                                            P2MP = P2MP - 5
                                            oc = 1
                                        mc = 1
                                    
                                    #Damage boost - Varies
                                    elif option == 6:

                                        #If P2 has NO MP
                                        if P1MP < 1:
                                            confirm("You have no MP, so therefor you cannot use this spell.")
                                        
                                        else:
                                            q("For every MP you put into this spell, you will get a +1.25 damage boost to your next attack.\n")
                                            wait()
                                            P2DMGBOOST = ask("How much MP would you like to put into the spell (0 to cancel)? ")
                                        
                                        #Cancel
                                        if P2DMGBOOST == 0:
                                            q("You canceled your damage boost.\n")
                                        
                                        else:

                                            #If P2 tries to spend more MP than they have
                                            if P2MP < P2DMGBOOST:
                                                confirm("You don't have enough MP for that amount of a damage boost.")
                                            
                                            #Sucess!
                                            else:
                                                P2MP = P2MP - P2DMGBOOST
                                                P2DMGBOOST = round(P2DMGBOOST * 1.25)
                                                confirm("You gained a buff of +" + str(P2DMGBOOST) + " damage on your next attack.")
                                                mc = 1
                                                oc = 1
                                    
                                    #Spell descriptions
                                    elif option == 7:
                                        q("Spell descriptions: \n")
                                        wait()
                                        q("Fireball - 5MP. Create a ball of fire that crashes down on the target. This will do anywhere from half of your MAXMP to your MAXMP of almost unblockable damage. If you are to create a fireball that does so little damage, it will get blocked\n")
                                        wait()
                                        q("Conjure a random item - 2 MP. Conjure a random item that can be used on your next turn.\n")
                                        wait()
                                        q("Gain advantage - 5MP. Gain advantage until the end of your next turn. For more information on advantage, visit the guide in the Main Menu.\n")
                                        wait()
                                        q("Impose disavantage - 5MP. Give your opponent disavnatage on their next turn, or get rid of thier advantage. For more information on advnatages, visit the guide in the Main Menu.\n")
                                        wait()
                                        q("Heal 20 percent of MAXHP - 5MP. Heal 20 percent of your max HP. This cannot take you above your maximum, though.\n")
                                        wait()
                                        confirm("Damage boost - Varies. Put as much MP as you want (and can) into this move, and have that amount multiplied by 1.25 and added to your next attack.")
                                    
                                    #Cancel
                                    elif option == 0:
                                        q("You cenceled your magic\n")
                                        wait()
                                        mc = 1
                                    
                                    else:
                                        q("Please give an option we can use.\n")
                                        wait(.5)
                                    
                            #Item
                            elif option == 3:

                                #If you've already used all your items this turn
                                if items_left == 0:
                                    confirm("You've used all your items this turn.")
                                    ic = 0

                                #If you can use more items
                                else:
                                    if not items_left == 3:
                                        confirm("You can use " + str(items_left) + " more items on this turn", .3)
                                    q("1: Spoons - " + str(P2SPOONS) + "\n")
                                    wait()
                                    q("2: Knives - " + str(P2KNIVES) + "\n")
                                    wait()
                                    q("3: Healing Potions - " + str(P2POTS) + "\n")
                                    wait()
                                    
                                    #Print properly whether the gun is in play or not
                                    if P2GLOCK >= 1:
                                        q("4: Glock - 19\n")
                                        wait()
                                        q("5: Cancel\n")
                                    else:
                                        q("4: Cancel\n")
                                    wait()
                                    
                                    #ItemCorrect
                                    ic = 0
                                    while ic == 0:

                                        #If there are no more items to be used
                                        if items_left == 0:
                                            ic = 1
                                            option = 0
                                        else:
                                            option = ask("What would you like to use?")

                                            #Spoons
                                            if option == 1:
                                                
                                                #If there are no spoons to use
                                                if P2SPOONS < 1:
                                                    confirm("You have no spoons. No soup for you.")
                                                
                                                #Spoons are at the ready
                                                else:
                                                    critnumber = critnum(0,1,1000,print_random)

                                                    #The 1 in 1000 chance to have P1 die from tetanus
                                                    if critnumber == 1000:
                                                        confirm("Player 1 got tetanus from being hit with the spoon, dying on the spot.")
                                                        ic = 1
                                                        oc = 1
                                                        P1HP = P1HP - P1HP
                                                    
                                                    #The 1 in 1000 chance to die from tetanus due to holding the spoon
                                                    elif critnumber == 1:
                                                        confirm("Player 2 got tetanus from holding the spoon, dying on the spot.")
                                                        ic = 1
                                                        oc = 1
                                                        P2HP = P2HP - P2HP
                                                    
                                                    #If it all goes normally
                                                    else:
                                                        confirm("You threw a spoon, doing 1 point of damage to Player 1")
                                                        P1HP = P1HP - 1
                                                    items_left = items_left - 1
                                                    P2SPOON = P2SPOON - 1
                                            
                                            #Knives
                                            if option == 2:

                                                #If there are no knives
                                                if P2KNIVES < 1:
                                                    confirm("You have no knives.")
                                                
                                                #Knives at the ready
                                                else:
                                                    critnumber = critnum(0, 1, 5, print_random)

                elif P2SPD > P1SPD:
                    q("Player 2 first, then player 1\n")
                
                else:
                    q("Since you have the same speed, we are randomly going to pick a character to go first.\n")
                    option = random.randint(1,2)
                    if option == 1:
                        P1SPD = P1SPD + 1
                    
                    elif option == 2:
                        P2SPD = P2SPD + 1
                    
                    else:
                        explode()
            
    
    else:
        q("Please give an option we can use.\n")
        wait(.5)
q("End of program\n")