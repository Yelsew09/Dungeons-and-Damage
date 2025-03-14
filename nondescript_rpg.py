"""
atkP
atkHP
atkMAX_HP
atkMP
atkMAX_MP
atkATK
atkATK_BON
atkDMG_BON
atkAD
atkADTR
atkSPOON
atkKNIFE
atkPOTS
atkFENCE
atkFENCE_SET
atkGLOCK

defP
defHP
defDEF
defAD
defADTR
defFENCE_SET
defGLOCK
print_random
"""

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
def q(str, t = 0.02):

    #Not sure how this works, all I know is that it does
    #Lets the text roll instead of being printed all at once
    for char in str:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(t)
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
def wait(t = .15):

    #Literally just laziness. I don't want to write time.sleep(.15) every second when I can just write wait()
    time.sleep(t)
def confirm(str, t = .5):
    
    #Used to provide a visual indicator that the user needs to continue
    #All games have an arrow that tells you you need to press A to continue
    q(str)
    input(' >')
    time.sleep(t)
def ask(question, t = .5):

    #Asks a question an keeps asking until the user gives a numerical input
    ec = True
    while ec:
        try:
            q(question)
            option = int(input(''))
            time.sleep(t)
            ec = False
        except ValueError:
            wait(.5)
            q("Please give a number.\n")
            ec = True
    return option
def random_num(minimum,maximum,show,ad = 0):
    
    #Generates a random number with advantage in mind
    if ad == 1:
        num1 = random.randint(minimum,maximum)
        num2 = random.randint(minimum,maximum)
        critnum = max(num1,num2)
    elif ad == 2:
        num1 = random.randint(minimum,maximum)
        num2 = random.randint(minimum,maximum)
        critnum = min(num1,num2)
    else:
        critnum = random.randint(minimum,maximum)
    if show:
        q("You rolled a: " + str(critnum))
    return critnum


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
    q("8: Random\n")
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
                option = "Knight"
                hp = 35
                maxHP = hp
                atk = 7
                atkBON = 5
                de = 16
                mp = 5
                maxMP = mp
                mpBON = 2
                spd = 3
                rc = False
            
            #Peashooter
            elif option == 2:
                option = "Peashooter"
                hp = 26
                maxHP = hp
                atk = 9
                atkBON = 4
                de = 14
                mp = 7
                maxMP = mp
                mpBON = 3
                spd = 5
                rc = False
            
            #Rouge
            elif option == 3:
                option = "Rouge"
                hp = 20
                maxHP = hp
                atk = 10
                atkBON = 6
                de = 13
                mp = 6
                maxMP = mp
                mpBON = 2
                spd = 7
                rc = False

            #Mage
            elif option == 4:
                option = "Mage"
                hp = 21
                maxHP = hp
                atk = 5
                atkBON = 2
                de = 11
                mp = 10
                maxMP = mp
                mpBON = 5
                spd = 4
                rc = False
            
            #Skele
            elif option == 5:
                option = "Skele"
                hp = 30
                maxHP = hp
                atk = 7
                atkBON = 3
                de = 12
                mp = 7
                maxMP = mp
                mpBON = 5
                spd = 6
                rc = False
            
            #Bard
            elif option == 6:
                option = "Bard"
                hp = 27
                maxHP = hp
                atk = 6
                atkBON = 4
                de = 14
                mp = 4
                maxMP = mp
                mpBON = 2
                spd = 2
                rc = False
            
            #Barbarian
            elif option == 7:
                option = "Barbarian"
                hp = 40
                maxHP = hp
                atk = 12
                atkBON = 2
                de = 15
                mp = 2
                maxMP = mp
                mpBON = 1
                spd = 1
                rc = False
            
            #Random
            elif option == 8:
                option = random.randint(1,7)
            
            #-.- --- -. .- -- .. ....... -.-. --- -.. .
            elif option == 88224646790:
                option = "-.- --- -. .- -- .. ....... -.-. --- -.. ."
                hp = 88224646790
                maxHP = hp
                atk = 88224646790
                atkBON = 88224646790
                de = 88224646790
                mp = 88224646790
                maxMP = mp
                mpBON = 88224646790
                spd = 88224646790
                rc = False
            
            else:
                q("Please give a valid opiton")
                wait(.3)
                q("\n")
        ync = True
        while ync:
            q("1: Yes\n")
            wait()
            q("2: No\n")
            wait()
            yesorno = ask("You have chosen the " + str(option) + " class, is this correct? ")
            
            #Yes
            if yesorno == 1:
                q("Player " + str(player) + " has chosen the " + str(option) + " class")
                wait(.5)
                q("\n")
                ync = False
                cc = False
            
            #No
            elif yesorno == 2:
                q("Repick your character")
                wait(.3)
                q("\n")
                ync = False
                cc = True
            
            #Invalid input
            else:
                q("Please give a provided number.")
                wait(.3)
                q("\n")
                ync = True
    return hp, maxHP, atk, atkBON, de, mp, maxMP, mpBON, spd
def combat(atkP, atkHP, atkMAX_HP, atkMP, atkMAX_MP, atkATK, atkATK_BON, atkDMG_BON, atkAD, atkADTR, atkSPOON, atkKNIFE, atkPOTS, atkFENCE, atkFENCE_SET, atkGLOCK,  defP, defHP, defDEF, defAD, defADTR, defFENCE_SET, defGLOCK, show):
    
    #OptionCorrect
    oc = True
    items_left = 3
    confirm("This is the start of player " + str(atkP) + "'s turn.",.3)
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

            #Fence
            if defFENCE_SET:
                confirm("You struck player " + str(defP) + "'s fence they set up.")
                defFENCE_SET = False

            else:
                critnumber = random_num(1,20,atkAD,show)
                
                #You need to see what you rolled here
                if not show:
                    q("You rolled a " + str(critnumber) + "!")
                    wait(.5)
                    q("\n")
                
                #Critical hit
                if critnumber == 20:
                    q("It's a critical hit!")
                    wait(.3)
                    confirm("\nPlayer " + str(atkP) + " did " + str(atkATK*2 + atkDMG_BON) + " damage to player " + str(defP) + ".")
                    defHP -= atkATK*2 + atkDMG_BON
                
                elif critnumber + atkATK_BON >= defDEF:
                    confirm("You landed a hit, doing " + str(atkATK + atkDMG_BON) + " damage to player " + str(defP) + ".")
                    defHP -= atkATK + atkDMG_BON
                
                elif critnumber + atkATK_BON < defDEF:
                    confirm("You missed your attack.")
                
                else:
                    explode()
            atkDMG_BON = 0
            oc = False
        
        #Magic
        elif option == 2:
            
            #MagicCorrect
            mc = True
            while mc:
                q("1: Fireball - 5MP\n")
                wait()
                q("2: Summon item - 2MP\n")
                wait()
                q("3: Gain advantage - 3MP\n")
                wait()
                q("4: Impose disadvantage - 4MP\n")
                wait()
                q("5: Heal 20% - 4MP\n")
                wait()
                q("6: Damage boost\n")
                wait()
                q("7: Spell descriptions\n")
                wait()
                q("0: Cancel\n")
                wait()
                option = ask("What would you like to do? ")

                #Fireball - 5MP
                if option == 1:
                    
                    #Not enough MP
                    if atkMP < 5:
                        confirm("You don't have enough MP for that.")
                    
                    else:
                        critnumber = random_num(atkMAX_MP,round(atkMAX_MP*1.5),show)
                        atkMP -= 5
                        oc = False
                        mc = False
                        
                        #If the magic is weak enough, it will get blocked
                        if round(defDEF/4) >= critnumber:
                            confirm("Your opponent's defence blocked the " + str(critnumber) + " damage you tried to do.")

                        #Fence
                        elif defFENCE_SET == 1:
                            confirm("You struck player " + str(defP) + "'s fence.")

                        else:
                            confirm("Player " + str(atkP) + " did " + str(critnumber) + " damage to player " + str(defP) + ".")
                            defHP = defHP - critnumber
                
                #Summon random item - 2MP
                elif option == 2:
                    
                    #Not enough MP
                    if atkMP < 2:
                        confirm("You don't have enough MP for that.")
                    
                    else:
                        critnumber = random_num(1,100,show)
                        atkMP -= 2
                        q("You conjured up ")

                        #Spoon
                        if critnumber >= 1 and critnumber <= 10:
                            q("a... ")
                            wait(.5)
                            q("rusty... ", .5)
                            wait(.6)
                            confirm("spoon?")
                            atkSPOON += 1

                        #Knife
                        elif critnumber >= 11 and critnumber <= 50:
                            q("some small, well-balanced knives.")
                            atkKNIFE += 3
                        
                        #Healing Potion
                        elif critnumber >= 51 and critnumber <= 89:
                            confirm("a potent red potion that gives you energy just by holding it.")
                            atkPOTS += 1

                        #Chain link fence
                        elif critnumber >= 90 and critnumber <= 99:
                            q("a chain link fence that looks like it would crumble at a moment's notice, but also looks incredibly sturdy at the same time.")
                            atkFENCE += 1
                        
                        #HE HAS A GUN
                        elif critnumber == 100:
                            
                            #The other player had a gun
                            if atkGLOCK == 0 and defGLOCK >= 1:
                                q("Ok, great. Now the OTHER guy has a gun.")
                                wait(.5)
                                confirm("\nI'm leaving.", .2)
                            
                            #The current player already had a gun
                            elif atkGLOCK >= 1:
                                q("You did it again.")
                                wait(1)
                                q("\nLanded a 1 in 100 chance to get a literal GUN.")
                                wait(1)
                                q("\nThat thing could've won you the game intstanly.")
                                wait(1)
                                q("\nAnd you kept going.")
                                wait(1)
                                q("\n")
                                print("\nWHY?!?!?")
                                wait(1)
                                q("Alright, I'm ending this here and now.")
                                wait(1)
                                confirm("\nGod landed a destructive hit, doing " + str(999+P2HP) + " damage to player " + str(defP) + ".", 1)
                                defHP = 0
                                for i in range (5):
                                    print("Calculating, please wait.")
                                    wait(.5)
                                    q("\n")
                                    wait(1)
                                    q("\n")
                                    wait(.5)
                                    print("Calculating failed.")
                                    wait(.3)
                                    if i > 5:
                                        print("Retrying...")
                                        wait(.2)
                                confirm("Player " + str(defP) + " has ValueError HP left.")
                            
                            #The first gun in the game
                            elif atkGLOCK == 0 and defGLOCK == 0:
                                q("a ")
                                wait(.3)
                                print("GUN?!?!")
                                wait(.3)
                                q("Not even an old gun, like a musket.\n")
                                wait(.3)
                                q("Just a Glock-19\n")
                                wait(.3)
                                confirm("I quit.")
                            
                            else:
                                explode()
                            atkGLOCK += 1
                            oc = False
                            mc = False
                
                #Gain advantage - 3MP
                elif option == 3:
                    
                    #Not enough MP
                    if atkMP < 3:
                        confirm("You don't have enough MP for this.\n")
                    
                    else:

                        #If defending Player has advantage
                        if defAD == 1:
                            confirm("You gained advantage on your next turn.\n")
                            atkMP -= 3
                            atkAD = 1
                            atkADTR = 2
                            oc = False
                            mc = False
                
                #Impose disadvantage - 4MP
                elif option == 4:

                    #Not enough MP
                    if atkMP < 4:
                        confirm("You don't have enough MP for that.")
                    
                    else:
                        atkMP -= 4
                        oc = False
                        mc = False
                        #If the defending player already had advantage
                        if defAD == 1:
                            confirm("You got rid of player " + str(defP) + "'s advantage.")
                            defAD = 0
                            defADTR = 0

                        #If the defending player has no hit modifiers
                        elif defAD == 0:
                            confirm("You gave player " + str(defP) + " disadvantage on their next turn.")
                            defAD = 2
                            defADTR = 1
                        
                        #If the defending player has disadvantage
                        elif defAD == 2:
                            confirm("You continuted player " + str(defP) + "'s disadvantage by one more turn.")
                            defAD = 2
                            defADTR = 1
                        
                        else:
                            explode()
                    
                #Heal 20% - 4MP
                elif option == 5:
                    
                    #Not enough MP
                    if atkMP < 4:
                        confirm("You don't have enough MP for that.")
                    
                    #Already at max HP
                    elif atkHP == atkMAX_HP:
                        confirm("You're already at max HP.")
                    
                    else:
                        atkMP -= 4
                        HEAL = atkMAX_HP/5
                        confirm("You healed " + str(HEAL) + " points of damage.",.2)
                        atkHP += HEAL

                        #Going over max hp
                        if atkHP > atkMAX_HP:
                            q("But that would've taken you over your max HP.",.2)
                            atkHP = atkMAX_HP
                        wait(.3)
                        oc = False
                        mc = False

                #Damage boost - 2MP
                elif option == 6:
                    
                    #Not enough MP
                    if atkMP < 2:
                        confirm("You don't have enough MP.")
                    
                    #Already have the boost
                    elif atkDMG_BON > 0:
                        q("You are already under the effect of this.")
                    
                    else:
                        atkMP -= 2
                        atkDMG_BON = round(atkATK/3)
                        confirm("You gained a damage boost of " + str(atkDMG_BON) + " damage.")
                        oc = False
                        mc = False
                
                #Spell descriptions
                elif option == 7:
                    q("Fireball generates a random number between your MAX_MP and 1.5x your MAX_MP and compares it to 1/4 of your opponent's DEF.")
                    wait(1)
                    confirm("\nIf the fireball number beats the DEF, then it will do that much damage.")
                    q("Summoning a random item generates a random item from the game and gives it to you.")
                    wait(1)
                    confirm("\nFor descriptions on each item or chance of appearance, please check the more in-depth descriptions found in the guide.")
                    q("Gain advantage gives you advantage until the end of your next turn, and Impose disadvantage gives your opponent disadvantage until the end of their next turn.")
                    wait(1)
                    confirm("\nAdvantage details can be found in the guide.")
                    confirm("Heal 20 percent takes 1/5 of your MAX_HP and adds it to your HP. This cannot be used to go over your MAX_HP, though.")
                    confirm("Damage boost adds 1/3 of your ATK to your next attack")

                #Cancel
                elif option == 0:
                    q("You canceled your magic usage.\n")
                    wait(.3)
                    mc = False
                
                else:
                    q("Please give a provided number.\n")
                    wait(.3)
                    mc = True
            
        #Items
        elif option == 3:

            #If there are no more item uses left and you just selected it from the menus
            if items_left == 0:
                confirm("You've used all your items this turn.")
            
            #If you have items left to use, start the loop
            else:
                q("1: Spoon - " + str(atkSPOON) + "\n")
                wait()
                q("2: Knife - " + str(atkKNIFE) + "\n")
                wait()
                q("3: Potion - " + str(atkPOTS) + "\n")
                wait()
                q("4: Chain Fence (uses 3 item uses) - " + str(atkFENCE) + "\n")
                wait()

                #Print Properly if the gun is in play
                if atkGLOCK >= 1:
                    q("5: Glock\n")
                wait()
                q("0: Cancel\n")
                wait()
                ic = True
                while ic:
                    
                    #No more items
                    if items_left == 0:
                        option = 0
                        ic = False
                    else:
                        option = ask("What would you like to use? ")
                        
                        #Spoons
                        if option == 1:
                            
                            #No spoons
                            if atkSPOON < 1:
                                confirm("You don't have any spoons. No soup for you.")
                            
                            else:
                                critnumber = random_num(1,1000,False)

                                #The chance to instantly kill the defending player due to tetanus
                                if critnumber == 1000:
                                    
                                    #Fence
                                    if defFENCE_SET == 1:
                                        confirm("You struck " + str(defP) + "'s fence.")
                                        items_left -= 1
                                    else:
                                        confirm("Player " + str(defP) + " got tetanus from being hit with the spoon, dying on the spot.")
                                        defHP = 0
                                        items_left = 0
                                    atkSPOON -= 1
                                    ic = False
                                    oc = False
                                
                                #The chance to instally die due to tetanus from holding the spoon
                                elif critnumber == 1:
                                    confirm("Player " + str(atkP) + " wasn't safe from the spoon. While they were holding it, they got tetanus and died.")
                                    atkHP = 0
                                    atkSPOON -= 1
                                    items_left = 0
                                    ic = False
                                    oc = False
                                
                                #Everything is good
                                else:

                                    #Fence
                                    if defFENCE_SET == 1:
                                        confirm("You struck player " + str(defP) + "'s fence.")
                                    else:
                                        confirm("Player " + str(atkP) + " did 1 point of damage to player " + str(defP) + ".")
                                        defHP -= 1
                                    items_left -= 1
                                    atkSPOON -= 1
                        
                        #Knife
                        elif option == 2:
                            
                            #No knife
                            if atkKNIFE < 1:
                                ask("You don't have any knives. Want a pencil instead? ",.3)
                                q("Well I don't have any.\n")
                                wait(.5)
                            
                            else:
                                critnumber = random_num(1,50,show)

                                #Miss
                                if critnumber == 1:
                                    confirm("You threw a knife, completely missing your opponent.")

                                #Hit
                                else:
                                    
                                    #Fence
                                    if defFENCE_SET == 1:
                                        confirm("You struck player " + str(defP) + "'s fence.")
                                    else:
                                        critnumber = random_num(1,5,show)
                                        confirm("You threw a knife, doing " + str(critnumber) + " damage to player " + str(defP) + ".")
                                        defHP -= critnumber
                                atkKNIFE -= 1
                                items_left -= 1
                        
                        #Healing Potion
                        elif option == 3:

                            #No potions
                            if atkPOTS < 1:
                                q("You don't have any healing poitions.")
                                wait(.3)
                                confirm("str(potion_joke) + '.'")
                            
                            else:
                                HEAL = round(atkMAX_HP/10)
                                confirm("You healed " + str(HEAL) + " points of damage.",.2)
                                atkHP += HEAL
                                if atkHP > atkMAX_HP:
                                    confirm("But that woul've taken you over your maximum HP.\n",.2)
                                    atkHP = atkMAX_HP
                                wait(.3)
                                atkPOTS -= 1
                                items_left -= 1
                        
                        #Chain link fence
                        elif option == 4:
                            
                            #No fence
                            if atkFENCE < 1:
                                confirm("You don't have a fence. Besides, who carries whole fences on them?")
                            
                            elif not items_left == 3:
                                confirm("You need three item uses to set this up.")

                            else:
                                confirm("You set up an enitre fence in front of you. Looks like it could block a hit")
                                atkFENCE_SET = True
                                atkFENCE -= 1
                                items_left -= 3
                                ic = False
                        
                        #Gun if possible
                        elif option == 5 and atkGLOCK >= 1:
                            critnumber = random_num(1,1000)
                            
                            #Miss
                            if critnumber == 1:
                                confirm("You missed.",.2)
                                q("And that's the last shot in the clip.\n")
                                wait(1)
                                confirm("My man really summoned a one-shot weapon with one shot.")
                                atkGLOCK -= 1
                            
                            #So anyway, I started blasting
                            else:
                                
                                #FENCE
                                if defFENCE_SET == 1:
                                    confirm("You shot player " + str(defP) + "'s fence.")
                                    items_left -= 1
                                else:
                                    confirm("You shot your gun, hitting player " + str(defP) + " and doing ValueError damage to them.")
                                    defHP = 0
                                    items_left = 0
                                    ic = False
                                atkGLOCK -= 1
                        
                        #Cancel
                        elif option == 0:
                            q("You canceled your item usage.\n")
                            ic = False
                            wait(.5)

                        else:
                            q("Please give a provided number.\n")
                            wait(.3)
        
        #Pass
        elif option == 4:
            q("1: Yes\n")
            wait()
            q("2: No\n")
            wait()
            
            #YesNoCorrect
            ync = True
            while ync:
                yesorno = ask("Are you sure you want to pass your turn? ")
                
                #Yes
                if yesorno == 1:
                    q("You passed your turn.\n")
                    wait(.5)
                    ync = False
                    oc = False
                
                #No
                elif yesorno == 2:
                    q("You did not pass your turn.\n")
                    wait(.5)
                    ync = False
                    oc = True

                else:
                    q("Please give a provided number.\n")
                    wait(.3)

        #Forfeit
        elif option == 5:
            q("1: Yes\n")
            wait()
            q("2: No\n")
            wait()
            
            #YesNoCorrect
            ync = True
            while ync:
                yesorno = ask("Are you sure you want to run away (forfeit the match)? ")
                
                #Yes
                if yesorno == 1:
                    q("You forfeit the match.\n")
                    atkHP = 0
                    ync = False
                    oc = False
                
                #No
                elif yesorno == 2:
                    q("You did not forfeit the match.\n")

                else:
                    q("Please give a provided number.\n")
                    wait(.3)
        
        else:
            q("Please give a provided number.\n")
            wait(.3)
    return atkHP, atkMP, atkATK_BON, atkDMG_BON, atkAD, atkADTR, atkSPOON, atkKNIFE, atkPOTS, atkFENCE, atkFENCE_SET, atkGLOCK,  defHP, defAD, defADTR, defFENCE_SET, defGLOCK
##########

#Setting default rule values
print_random = False

#THE GAME#
#Insert loading sequence here when you figure out how to do that

q("Welcome to Dungeons and Damage")
wait(.5)
q("\nNot to be confused with Dungeons and Dragons")
wait(.5)
q("\nAlthough this game does feel like it")
wait(.5)
q("\n")
wait(.5)
q("\n")
wait(.5)

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
        P1KNIVES = 5
        P2KNIVES = 5
        P1POTS = 1
        P2POTS = 1
        P1FENCE = 0
        P2FENCE = 0
        P1FENCESET = 0
        P2FENCESET = 0
        P1GLOCK = 0
        P2GLOCK = 0
        P1WINS = 0
        P2WINS = 0
        roundnum = 1

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
        
        #OptionCorrect
        oc = True
        while oc:
            q("On your turn, you may do 1 of 5 things:")
            wait(.3)
            q("\n1: Attack\n")
            wait()
            q("2: Use magic\n")
            wait()
            q("3: Use an item\n")
            wait()
            q("4/5: Pass/Run\n")
            wait()
            q("0: Back\n")
            wait()
            option = ask("What would you like to learn more about? ")

            #Attack details
            if option == 1:
                q("\n")
                wait(.5)
                q("When you attack, there are 3 numbers at play:")
                wait(.5)
                q("\natkATK, ")
                wait(.3)
                q("atkATK_BON, ")
                wait(.3)
                confirm("and defDEF.")
                q("\n")
                wait(.5)
                q("When you attack, you generate a random number 1-20 based on your advantage.")
                wait(1)
                q("\nIf you have advantage, the game generates 2 numbers and spits out the higher number.")
                wait(1)
                q("\nIf you have disadvantage, 2 numbers are generated and the smaller one is outputted.")
                wait(1)
                confirm("\nNeutral advantage just generates one number.")
                q("\n")
                wait(.5)
                q("If that number is 20, then the attack will hit.")
                wait(.5)
                q(" Guarenteed.")
                wait(.5)
                confirm("\nThe resulting damage is double the atkATK + atkDMG_BON")
                q("Your atkBON is then added to this number and compared to your opponent's defence.")
                wait(1)
                q("\nIf the number meets or beats the defence, then the attack hits. If it falls short, the attack misses.")
                wait(1)
                q("\nIf the attack hits, then it will do atkATK + atkDMG_BON damage.")
                wait(1)
                confirm("\nIf you hit a fence, all damage will be negated, regardless of how much damage it would've done, and all damage buffs will be used up.")
                wait(.5)
                q("\n")
                wait(.5)
                oc = False

            #Magic details
            elif option == 2:
                confirm("Just fyi, you can use the spell descriptions option in game for a refresher.")
                q("When selecting magic, you are given these options: ")
                wait(1)
                q("You may cast any of the spells as long as you have the corresponding amount of MP.")
                wait(1)
                
                mc = True
                while mc:
                    q("\n1: Fireball - 5MP\n")
                    wait()
                    q("2: Summon item - 2MP\n")
                    wait()
                    q("3: Gain advantage - 3MP\n")
                    wait()
                    q("4: Impose disadvantage - 4MP\n")
                    wait()
                    q("5: Heal 20% - 4MP\n")
                    wait()
                    q("6: Damage Boost - Varies\n")
                    wait()
                    q("0: Back\n")
                    wait(1)
                    
                    option = ask("\nWhat would you like to learn more about? ")
                    
                    #Fireball description
                    if option == 1:
                        q("\nFireball summons a ball of fire that is thrown at your opponent. The damage is based on your MAXMP, the minimum being your MAXMP and the maximum being your MAXMP*1.5 (rounded up).")
                        wait(3)
                        confirm("\nIf that damage is less than a fourth of your opponent's DEF, then the fireball will be blocked.")
                    
                    #Item descriptions
                    elif option == 2:
                        q("\nSummoning a random item generates a random item from the loot table:")
                        wait(1)
                        q("\nRusty Spoon - 10%\n")
                        wait()
                        q("3 Knives - 40%\n")
                        wait()
                        q("Healing potion - 40%\n")
                        wait()
                        confirm("Chain link fence - 10%")
                        q("\n")
                        confirm("For more information on items, please visit the set of item details.")
                        
                    #Advantage Description
                    elif option == 3:
                        q("\nWhen you are given advantage, the next time you attack the game generates 2 numbers.")
                        wait(1)
                        q("\nThese numbers are then compared, and the higher number is taken.")
                        wait(1)
                        confirm("\nWhen you use this spell, you gain advantage until the end of your next turn.")
                        q("Disadvantage is the opposite.")
                        wait(1)
                        confirm("\n2 numbers are generated, but the game will output the lower number.")
                    
                    #Disadvantage description
                    elif option == 4:
                        q("\nWhen you are given disadvantage, the next time you attack the game generates 2 numbers.")
                        wait(1)
                        q("\nThese numbers are then compared, and the lower number is taken.")
                        wait(1)
                        confirm("\nWhen you use this spell, your opponent will gain disadvantage until the end of their next turn.")
                        q("Advantage is the opposite.")
                        wait(1)
                        confirm("\n2 numbers are generated, but the game will output the higher number.")
                    
                    #Heal 20% desription
                    elif option == 5:
                        q("\nThis spell heals you by 1/5 of your maximum HP.")
                        wait(2)
                        confirm("\nThat's it.")
                    
                    #Damage Boost description
                    elif option == 6:
                        q("\nWhen you activate this spell, you will be prompted to put MP into this spell.")
                        wait(.5)
                        q("\nIf you wish to cancel, provide it with 0.")
                        wait(1)
                        confirm("\nThis amount is then multiplied by 1.5 and added to your next attack (after doubling from a crit).")
                        confirm("If you try to put more MP than you have into the spell, it won't work.")
                    
                    #Back
                    elif option == 0:
                        mc = False

                    else:
                        confirm("Please give an option we can use")

            #Item details
            elif option == 3:
                q("\nOn your turn, you may use 3 items.")
                wait(1)
                mc = True
                while mc:
                    q("\n1: Spoon\n")
                    wait()
                    q("2: Knives\n")
                    wait()
                    q("3: Healing potion\n")
                    wait()
                    q("4: Chain link fence\n")
                    wait()
                    q("0: Back\n")
                    wait()
                    option = ask("What would you like to know more about? ")

                    #Spoon
                    if option == 1:
                        q("A metal spoon that appears to have been left out in the rain for a while.")
                        wait(1)
                        confirm("\nDoes 1 point of damage, but could infect either player with tetanus.")
                    
                    #Knives
                    elif option == 2:
                        q("Some small knives that are very well-balanced.")
                        wait(1)
                        confirm("\nThey do 1 to 5 points of unblockable damage when thrown.")
                    
                    #Healing Potion
                    elif option == 3:
                        q("A bottle filled to the brim with a red liquid.")
                        wait(1)
                        confirm("\nUsing it will heal 3 to 7 points of damage.")
                    
                    #Chain link fence
                    elif option == 4:
                        q("It's a fence that you often see around children's playgrounds.")
                        wait(1)
                        confirm("\nIt blocks 1 hit, regardless of damage.")
                    
                    #Back
                    elif option == 0:
                        mc = False

            #Pass/Run
            elif option == 4:
                q("Passing your turn ends your turn. Why would you want to do that?")
                wait(1)
                confirm("\nYou get MP refresh and lose advantage or disadvantage.")
                confirm("Running is basically a forfeit. It ends the game with you as the loser.")
            
            #Back
            elif option == 0:
                oc = False

    #Options
    elif option == 3:
        
        #OptionCorrect
        oc = True
        while oc:
            q("1: print_random: " + str(print_random) + "\n")
            wait()
            q("0: Back\n")
            wait()
            option = ask("What would you like to change? ")
            
            #print_random
            if option == 1:
                
                if print_random:
                    print_random == False
                    q("print_random has been set to False")
                    wait(.5)
                    q("\n")
                
                elif not print_random:
                    print_random == True
                    q("print_random has been set to True")
                    wait(.5)
                    q("\n")
                
                else:
                    explode()
            
            #Back
            elif option == 0:
                oc = False

            else:
                q("Please choose a given option.")
                wait(.5)
    
    #Quit
    elif option == 4:
        ac = False
    
    #Game Start
    elif option == 1:
        P1HP,P1MAXHP,P1ATK,P1ATKBON,P1DEF,P1MP,P1MAXMP,P1MPBON,P1SPD = charSelect(1)
        P2HP,P2MAXHP,P2ATK,P2ATKBON,P2DEF,P2MP,P2MAXMP,P2MPBON,P2SPD = charSelect(2)
        
        #GameCorrect
        gc = True
        while gc:
        
            #P1 is faster than P2
            if P1SPD > P2SPD:
                
                confirm("This is the start of round " + str(roundnum) + ".",.3)
                confirm("Player 1 has " + str(P1HP) + "/" + str(P1MAXHP) + " HP left, and " + str(P1MP) + "/" + str(P1MAXMP) + " MP left",.15)
                confirm("Player 2 has " + str(P2HP) + "/" + str(P2MAXHP) + " HP left, and " + str(P2MP) + "/" + str(P2MAXMP) + " MP left",.15)
                
                #Player 1's turn
                P1HP, P1MP, P1ATKBON, P1DMGBOOST, P1AD, P1ADTR, P1SPOONS, P1KNIVES, P1POTS, P1FENCE, P1FENCESET, P1GLOCK,  P2HP, P2AD, P2ADTR, P2FENCESET, P2GLOCK = combat(1, P1HP, P1MAXHP, P1MP, P1MAXMP, P1ATK, P1ATKBON, P1DMGBOOST, P1AD, P1ADTR, P1SPOONS, P1KNIVES, P1POTS, P1FENCE, P1FENCESET, P1GLOCK,  2, P2HP, P2DEF, P2AD, P2ADTR, P2FENCESET, P2GLOCK, print_random)
                
                #If P1 has no more HP
                if P1HP <= 0:
                    confirm("Player 1 is out of HP. They have lost the game.")
                    gc = False
                    P2WINS += 1
                
                #If P2 has no more HP
                elif P2HP <= 0:
                    confirm("Player 2 is out of HP. They have lost the game.")
                    gc = False
                    P1WINS += 1
                
                else:

                    #Player 2's turn
                    P2HP, P2MP, P2ATKBON, P2DMGBOOST, P2AD, P2ADTR, P2SPOONS, P2KNIVES, P2POTS, P2FENCE, P2FENCESET, P2GLOCK,  P1HP, P1AD, P1ADTR, P1FENCESET, P1GLOCK = combat(2, P2HP, P2MAXHP, P2MP, P2MAXMP, P2ATK, P2ATKBON, P2DMGBOOST, P2AD, P2ADTR, P2SPOONS, P2KNIVES, P2POTS, P2FENCE, P2FENCESET, P2GLOCK,  1, P1HP, P1DEF, P1AD, P1ADTR, P1FENCESET, P1GLOCK, print_random)
                    
                    #If P1 has no more HP
                    if P1HP <= 0:
                        confirm("Player 1 is out of HP. They have lost the game.")
                        gc = False
                        P2WINS += 1
                    
                    #If P2 has no more HP
                    elif P2HP <= 0:
                        confirm("PLayer 2 is out of HP. They have lost the game.")
                        gc = False
                        P1WINS += 1
                    
                    else:
                        roundnum += 1
                        
                        P1MP += P1MPBON
                        #Over MAXMP
                        if P1MP > P1MAXMP:
                            P1MP = P1MAXMP
                        
                        P2MP += P2MPBON
                        #Over MAXMP
                        if P2MP > P2MAXMP:
                            P2MP = P2MAXMP
            
            #If P2 is faster than P1
            elif P2SPD > P1SPD:
                confirm("This is the start of round " + str(roundnum) + ".",.3)
                confirm("Player 2 has " + str(P2HP) + "/" + str(P2MAXHP) + " HP left, and " + str(P2MP) + "/" + str(P2MAXMP) + " MP left",.15)
                confirm("Player 1 has " + str(P1HP) + "/" + str(P1MAXHP) + " HP left, and " + str(P1MP) + "/" + str(P1MAXMP) + " MP left",.15)
                
                #Player 2's turn
                P2HP, P2MP, P2ATKBON, P2DMGBOOST, P2AD, P2ADTR, P2SPOONS, P2KNIVES, P2POTS, P2FENCE, P2FENCESET, P2GLOCK,  P1HP, P1AD, P1ADTR, P1FENCESET, P1GLOCK = combat(2, P2HP, P2MAXHP, P2MP, P2MAXMP, P2ATK, P2ATKBON, P2DMGBOOST, P2AD, P2ADTR, P2SPOONS, P2KNIVES, P2POTS, P2FENCE, P2FENCESET, P2GLOCK,  1, P1HP, P1DEF, P1AD, P1ADTR, P1FENCESET, P1GLOCK, print_random)
                
                #P2 has no more HP
                if P2HP <= 0:
                    confirm("Player 2 is out of HP. They have lost the game.")
                    gc = False
                    P1WINS += 1
                
                #P1 has no more HP
                elif P1HP <= 0:
                    confirm("Player 1 is out of HP. They have lost the game.")
                    gc = False
                    P2WINS += 1
                
                else:
                    
                    #Player 1's turn
                    P1HP, P1MP, P1ATKBON, P1DMGBOOST, P1AD, P1ADTR, P1SPOONS, P1KNIVES, P1POTS, P1FENCE, P1FENCESET, P1GLOCK,  P2HP, P2AD, P2ADTR, P2FENCESET, P2GLOCK = combat(1, P1HP, P1MAXHP, P1MP, P1MAXMP, P1ATK, P1ATKBON, P1DMGBOOST, P1AD, P1ADTR, P1SPOONS, P1KNIVES, P1POTS, P1FENCE, P1FENCESET, P1GLOCK,  2, P2HP, P2DEF, P2AD, P2ADTR, P2FENCESET, P2GLOCK, print_random)
                    
                    #If P2 has no more HP
                    if P2HP <= 0:
                        confirm("Player 2 is out of HP. They have lost the game.")
                        gc = False
                        P1WINS += 1
                    
                    #If P1 has no more HP
                    elif P1HP <= 0:
                        confirm("Player 1 is out of HP. They have lost the game.")
                        gc = False
                        P2WINS += 1
                    else:
                        roundnum += 1
                        P1MP += P1MPBON
                        
                        #Over MAXMP
                        if P1MP > P1MAXMP:
                            P1MP = P1MAXMP
                        P2MP += P2MPBON
                        
                        #Over MAXMP
                        if P2MP > P2MAXMP:
                            P2MP = P2MAXMP
            else:
                q("Player 1 and player 2 are tied for speed. Choosing a random character to go first.")
                wait(.5)
                q("\n")
                first = random.randint(1,2)
                
                #Player 1 goes first now
                if first == 1:
                    P1SPD += 1
                    confirm("Player 1 has randomly been chosen to go first.")
                
                #Player 2 goes first now
                elif first == 2:
                    P2SPD += 1
                    confirm("Player 2 has randomly been chosen to go first.")

                else:
                    explode()

    else:
        q("Please give a provided number.")
        wait(.3)
        q("\n")
