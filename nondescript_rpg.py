#I learned about classes and how to use them properly in coding class recently
#It allows for more control over what does what, and cuts down on space for certain actions
#This wouldn't have been a thing if it wasn't for a school project,
#where one of the options was to create a program that lets you make a custom character,
#with bonus points if you make an inventory system or an attack system. Guess what I had lying around.
#So, I then made the characters class-based, with minor passives being added and room for more differentiation

#The main control structures we use in this utilize Correct variables
#This is the best control structure for text-based games with menus
#They are used for controling which "menu" the game is in
#Each Correct Boolean corrosponds to a seperate menu,
#so if someone presses back, we go to the previous menu
#If someone attacks, we break all needed loops to get to the other player's turn
#Game's over? Loop back to the big ol' AllCorrect loop, putting you back at the main menu

#Imports random, which is used to generate random numbers used for combat within the game
#Imports time, which is used in a LOT of spots in the code, it's used for timings between text
#Imports sys, IDK what it does. All I know is that it's used in the q command
import random, time, sys

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
def y_or_n(asking):
    ync = True
    while ync:
        q("1: Yes\n")
        wait()
        q("2: No\n")
        wait()
        option = ask(str(asking))
        if option == 1:
            loop = False
            ync = False
        elif option == 2:
            loop = True
            ync = False
        else:
            q("Please give a valid option\n")
    return loop

#Class for characters
class Player():
    def __init__(self,h,a,aB,d,m,mB,s,p,n,i):
        self.hp = h
        self.hpMAX = h
        self.atk = a
        self.atkBON = aB
        self.defence = d
        self.mp = m
        self.mpMAX = m
        self.mpBON = mB
        self.spd = s
        self.id = p
        self.classname = str(n)
        self.item_uses = i
        self.spoons = 0
        self.knives = 0
        self.potions = 0
        self.fences = 0
        self.glocks = 0
        self.fence_set = False
        self.alive = True
        self.adv = 0
        self.adtr = 0
        self.dmgBON = 0
    def damage(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            self.alive = False
    def heal(self,heal):
        self.hp += heal
        if self.hp > self.hpMAX:
            self.hp = self.hpMAX
    def next_turn(self):
        self.mp += self.mpBON
        if self.mp > self.mpMAX:
            self.mp = self.mpMAX
class Knight():
    passive = "Fortitude"
    def __init__(self,p):
        Player.__init__(self,35,7,5,16,5,2,3,p,"Knight",2)
        self.passive = Knight.passive
        self.knives = 3
        self.potions = 5
        self.fences = 1
    def heal(self,heal):
        Player.heal(self,heal)
    def damage(self,damage):
        damage -= 2
        Player.damage(self,damage)
    def next_turn(self):
        Player.next_turn(self)
class Peashooter():
    passive = "Charge"
    def __init__(self,p):
        Player.__init__(self,26,9,4,14,7,3,5,p,"Peashooter",3)
        self.passive = Peashooter.passive
        self.spoons = 1
        self.knives = 2
        self.potions = 2
    def heal(self,heal):
        Player.heal(self,heal)
    def damage(self,damage):
        Player.damage(self,damage)
    def next_turn(self):
        if self.mp == self.mpMAX:
            self.dmgBON += 2
        else:
            Player.next_turn(self)
class Rouge():
    passive = "Accelerate"
    def __init__(self,p):
        Player.__init__(self,20,10,3,13,6,2,4,p,"Rouge",4)
        self.passive = Rouge.passive
        self.spoons = 2
        self.knives = 3
        self.potions = 1
        self.fences = 1
    def heal(self,heal):
        Player.heal(self,heal)
    def damage(self,damage):
        Player.damage(self,damage)
    def next_turn(self):
        self.spd += 1
        if self.spd > 7:
            self.spd = 7
        self.atkBON += 1
        if self.atkBON > 9:
            self.atkBON = 9
        Player.next_turn(self)
class Mage():
    passive = "Zoning in"
    def __init__(self,p):
        Player.__init__(self,21,5,2,11,5,2,4,p,"Mage",2)
        self.passive = Mage.passive
        self.spoons = 1
        self.knives = 1
        self.potions = 4
        self.fences = 2
    def heal(self,heal):
        Player.heal(self,heal)
    def damage(self,damage):
        Player.damage(self,damage)
    def next_turn(self):
        self.mpMAX += 1
        if self.mpMAX > 10:
            self.mpMAX = 10
        else:
            self.mp += 1
        self.mpBON += 1
        if self.mpBON > self.mpMAX / 2:
            self.mpBON = round(self.mpMAX / 2)
        Player.next_turn(self)
class Skele():
    passive = "Focused"
    def __init__(self,p):
        Player.__init__(self,30,7,3,12,7,5,6,p,"Skele",4)
        self.passive = Skele.passive
        self.knives = 6
    def heal(self,heal):
        Player.heal(self,heal)
    def damage(self,damage):
        if damage >= 15:
            damage = 0
        Player.damage(self,damage)
    def next_turn(self):
        Player.next_turn(self)
class Bard():
    passive = "Jack of all Trades"
    def __init__(self,p):
        Player.__init__(self,25,5,5,14,4,2,2,p,"Bard",5)
        self.passive = Bard.passive
        self.spoons = 5
        self.knives = 5
        self.potions = 3
        self.fences = 2
    def heal(self,heal):
        Player.heal(self,heal)
    def damage(self,damage):
        Player.damage(self,damage)
    def next_turn(self):
        confirm("As a bard, you may change around some stats to fit a type of playstyle.")
        oc = True
        while oc:
            q("1: Offensive\n")
            wait()
            q("2: Defensive\n")
            wait()
            q("3: Utility\n")
            wait()
            q("4: Magical\n")
            wait()
            q("5: All-Rounded\n")
            wait()
            option = ask("What would you like to change to (damage carries over)?")
            
            #Offensive
            if option == 1:
                damage = self.hpMAX - self.hp
                if 20 - damage <= 0:
                    confirm("You cannot select that preset; you would be out of HP")
                else:
                    self.hp = 20 - damage
                    self.hpMAX = 20
                    self.atk = 10
                    self.atkBON = 4
                    self.defence = 12
                    damage = self.mpMAX - self.mp
                    self.mp = 5 - damage
                    self.mpMAX = 5
                    if self.mp < 0:
                        self.mp = 0
                    self.mpMAX = 5
                    self.mpBON = 3
                    self.item_uses = 4
                    oc = False
            
            #Defensive
            elif option == 2:
                damage = self.hpMAX - self.hp
                if 30 - damage <= 0:
                    confirm("You cannot select that preset; you would run out of HP")
                else:
                    self.hp = 30 - damage
                    self.hpMAX = 30
                    self.atk = 3
                    self.atkBON = 1
                    self.defence = 17
                    damage = self.mpMAX - self.mp
                    self.mp = 2 - damage
                    if self.mp < 0:
                        self.mp = 0
                    self.mpMAX = 2
                    self.mpBON = 1
                    self.item_uses = 1
                    oc = False
            
            #Utility
            elif option == 3:
                damage = self.hpMAX - self.hp
                if 25 - damage <= 0:
                    confirm("You cannot select that preset; you would run out of HP")
                else:
                    self.hp = 25 - damage
                    self.hpMAX = 25
                    self.atk = 4
                    self.atkBON = 4
                    self.defence = 13
                    damage = self.mpMAX - self.mp
                    self.mp = 2 - damage
                    if self.mp < 0:
                        self.mp = 0
                    self.mpMAX = 2
                    self.mpBON = 2
                    self.item_uses = 10
                    oc = False
            
            #Magical
            elif option == 4:
                damage = self.hpMAX - self.hp
                if 22 - damage <= 0:
                    confirm("You cannot select that preset; you would run out of HP")
                else:
                    self.hp = 22 - damage
                    self.hpMAX = 22
                    self.atk = 3
                    self.atkBON = 4
                    self.defence = 13
                    damage = self.mpMAX - self.mp
                    self.mp = 6 - damage
                    if self.mp < 0:
                        self.mp = 0
                    self.mpMAX = 6
                    self.mpBON = 4
                    self.item_uses = 3
                    oc = False
            
            #All-Rounded
            elif option == 5:
                damage = self.hpMAX - self.hpMAX
                if 25 - damage <= 0:
                    confirm("You cannot select that prest; you would run out of HP")
                else:
                    self.hp = 25 - damage
                    self.hpMAX = 25
                    self.atk = 5
                    self.atkBON = 5
                    self.defence = 14
                    damage = self.mpMAX - self.mp
                    self.mp = 4
                    if self.mp < 0:
                        self.mp = 0
                    self.mpMAX = 4
                    self.mpBON = 2
                    self.item_uses = 5
                    oc = False

            else:
                q("Please give a valid option")
                wait(1)
                q("\n")
        Player.next_turn()
class Barbarian():
    passive = "Healthy"
    def __init__(self,p):
        Player.__init__(self,40,12,2,15,2,2,1,p,"Barbarian",1)
        self.passive = Barbarian.passive
    def heal(self,heal):
        heal = round(heal * 1.5)
        Player.heal(self,heal)
    def damage(self,damage):
        Player.damage(self,damage)
    def next_turn(self):
        self.heal(2)
        Player.next_turn(self)                     
class Custom():
    passive = "None"
    def __init__(self,h,a,aB,d,m,mB,s,p,n,i):
        Player.__init__(self,h,a,aB,d,m,mB,s,p,n,i)
        self.passive = Custom.passive
    def heal(self,heal):
        Player.heal(self,heal)
    def damage(self,damage):
        Player.damage(self,damage)
    def next_turn(self):
        Player.next_turn(self)
class God():
    passive = "Godlike"
    def __init__(self,p):
        Player.__init__(self,88224646790,88224646790,88224646790,88224646790,88224646790,88224646790,88224646790,p,"-.- --- -. .- -- .. ....... -.-. --- -.. .",88224646790)
        self.passive = God.passive
        self.glocks = 100
    def heal(self,heal):
        heal = 88224646790
        Player.heal(self,heal)
    def damage(self,damage):
        damage /= 5
        Player.damage(damage)
    def next_turn(self):
        Player.next_turn(self)

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
    q("9: Custom\n")
    wait()

    #CharacterCorrect
    cc = True
    while cc:
        option = ask("Please pick a class, player " + str(player) + ": ")
        
        #RandomCorrect
        rc = True
        while rc:
            
            skip = False
            #Knight
            if option == 1:
                char = Knight(player)
                rc = False
            
            #Peashooter
            elif option == 2:
                char = Peashooter(player)
                rc = False
            
            #Rouge
            elif option == 3:
                char = Rouge(player)
                rc = False

            #Mage
            elif option == 4:
                char = Mage(player)
                rc = False
            
            #Skele
            elif option == 5:
                char = Skele(player)
                rc = False
            
            #Bard
            elif option == 6:
                char = Bard(player)
                rc = False
            
            #Barbarian
            elif option == 7:
                char = Barbarian(player)
                rc = False
            
            #Random
            elif option == 8:
                option = random.randint(1,7)

            #Custom
            elif option == 9:
                q("With this system you may create a custom character using the point buy system.")
                wait(1)
                confirm("\nThis is where you are given points, and you add points to different stats")
                
                hp = 10
                atk = 0
                atkBON = 0
                de = 0
                mp = 0
                mpBON = 0
                spd = 0
                item_uses = 3
                points = 35
                confirm("Don't worry about points going below 0, the game will keep track of that")
                oc = True
                while oc:
                    q("1: Heath Points - " + str(hp) + "\n")
                    wait()
                    q("2: Attack Damage - " + str(atk) + "\n")
                    wait()
                    q("3: Attack Roll Bonus (can be up to 1/2 of your attack damage) - " + str(atkBON) + "\n")
                    wait()
                    q("4: Defence - " + str(de) + "\n")
                    wait()
                    q("5: Magic Points (or Magic Power) - " + str(mp) + "\n")
                    wait()
                    q("6: Magic Point Bonus (can be up to 1/2 of your MP) - " + str(mpBON) + "\n")
                    wait()
                    q("7: Speed - " + str(spd) + "\n")
                    wait()
                    q("8: Item Uses - " + str(item_uses) + "\n")
                    wait()
                    q("9: I'm done\n")
                    wait()
                    q("0: Back\n")
                    option = ask("What would you like to boost (you have " + str(points) + " points left)? ")
                    spent = 0
                    if option >= 1 and option <= 8:
                        spent = ask("How much would you like to change this by (negative for bringing points back back)? ")

                        #Doesn't have enough points
                        if spent > points:
                            spent = points

                        #Health Points
                        elif option == 1:
                            if hp + spent < 0:
                                spent = hp
                            hp += spent
                            points -= spent

                        #Attack Damage
                        elif option == 2:
                            if atk + spent < 0:
                                spent = atk
                            atk += spent
                            points -= spent

                        #Attack Roll Bonus
                        elif option == 3:
                            if atkBON + spent < 0:
                                spent = atkBON
                            if atkBON + spent > round(atk/2):
                                difference = atkBON + spent - round(atk/2)
                                atkBON = round(atk/2)
                                points -= difference
                            else:
                                atkBON += spent
                                points -= spent

                        #Defence
                        elif option == 4:
                            if de + spent < 0:
                                spent = de
                            de += spent
                            points -= spent
                        
                        #Magic Power (or Magic Points)
                        elif option == 5:
                            if mp + spent < 0:
                                spent = mp
                            mp += spent
                            points -= spent

                        #Magic Power Refresh
                        elif option == 6:
                            if mpBON + spent < 0:
                                spent = mpBON
                            if mpBON + spent > round(mp/2):
                                difference = mpBON + spent - round(mp/2)
                                atkBON = round(atk/2)
                                points -= difference
                            else:
                                mpBON += spent
                                points -= spent

                        #Speed
                        elif option == 7:
                            if spd + spent < 0:
                                spent = spd
                            spd += spent
                            points -= spent

                        #Item Uses
                        elif option == 8:
                            if item_uses + spent < 1:
                                spent = item_uses - 1
                            elif item_uses + spent >= 6:
                                difference = item_uses + spent - 6
                                item_uses = 6
                                points -= difference
                            else:
                                item_uses += spent
                                points -= spent
                    else:
                        
                        #I'm done
                        if option == 9:
                            if points > 0:
                                oc = y_or_n("You still have points to spend, are you sure you are done? ")
                                q("Please name your class: ")
                                name = str(input(''))
                        
                        #Back
                        elif option == 0:
                            oc = False
                            skip = True
                        
                        else:
                            q("Please give a valid option.")
                            wait(1)
                            q("\n")
                char = Custom(hp,atk,atkBON,de,mp,mpBON,spd,player,name,item_uses)
                rc = False
                cc = False

            #-.- --- -. .- -- .. ....... -.-. --- -.. .
            elif option == 88224646790:
                char = God(player)
                rc = False
            
            else:
                q("Please give a valid opiton")
                wait(.3)
                q("\n")
        if not skip:
            ync = True
            while ync:
                q("1: Yes\n")
                wait()
                q("2: No\n")
                wait()
                yesorno = ask("You have chosen the " + char.classname + " class, is this correct? ")
                
                #Yes
                if yesorno == 1:
                    q("Player " + str(player) + " has chosen the " + char.classname + " class")
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
        else:
            cc = True
    return char
def combat(atkP,defP,show):
    
    #OptionCorrect
    oc = True
    items_left = atkP.item_uses
    confirm("This is the start of player " + str(atkP.id) + "'s turn.",.3)
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
            if defP.fence_set:
                confirm("You struck player " + str(defP.id) + "'s fence they set up.")
                defP.fence_set = False

            else:
                critnumber = random_num(1,20,atkP.adv,show)
                
                #You need to see what you rolled here
                if not show:
                    q("You rolled a " + str(critnumber) + "!")
                    wait(.5)
                    q("\n")
                
                #Critical hit
                if critnumber == 20:
                    q("It's a critical hit!")
                    wait(.3)
                    confirm("\nPlayer " + str(atkP) + " did " + str(atkP.atk*2 + atkP.dmgBON) + " damage to player " + str(defP.id) + ".")
                    defP.damage(atkP.atk*2 + atkP.dmgBON)

                elif critnumber + atkP.atkBON >= defP.defence:
                    confirm("You landed a hit, doing " + str(atkP.atk + atkP.dmgBON) + " damage to player " + str(defP.id) + ".")
                    defP.damage(atkP.atk + atkP.dmgBON)
                
                elif critnumber + atkP.atkBON < defP.defence:
                    confirm("You missed your attack.")
                
                else:
                    explode()
            atkP.dmgBON = 0
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
                    if atkP.mp < 5:
                        confirm("You don't have enough MP for that.")
                    
                    else:
                        critnumber = random_num(atkP.mpMAX,round(atkP.mpMAX*1.5),show)
                        atkP.mp -= 5
                        oc = False
                        mc = False
                        
                        #If the magic is weak enough, it will get blocked
                        if round(defP.defence/4) >= critnumber:
                            confirm("Your opponent's defence blocked the " + str(critnumber) + " damage you tried to do.")

                        #Fence
                        elif defP.fence_set == 1:
                            confirm("You struck player " + str(defP) + "'s fence.")
                            defP.fence_set = False

                        else:
                            confirm("Player " + str(atkP.id) + " did " + str(critnumber) + " damage to player " + str(defP.id) + ".")
                            defP.damage(critnumber)
                
                #Summon random item - 2MP
                elif option == 2:
                    
                    #Not enough MP
                    if atkP.mp < 2:
                        confirm("You don't have enough MP for that.")
                    
                    else:
                        critnumber = random_num(1,100,show)
                        atkP.mp -= 2
                        q("You conjured up ")

                        #Spoon
                        if critnumber >= 1 and critnumber <= 10:
                            q("a... ")
                            wait(.5)
                            q("rusty... ", .5)
                            wait(.6)
                            confirm("spoon?")
                            atkP.spoons += 1

                        #Knife
                        elif critnumber >= 11 and critnumber <= 50:
                            q("some small, well-balanced knives.")
                            atkP.knives += 3
                        
                        #Healing Potion
                        elif critnumber >= 51 and critnumber <= 89:
                            confirm("a potent red potion that gives you energy just by holding it.")
                            atkP.potions += 1

                        #Chain link fence
                        elif critnumber >= 90 and critnumber <= 99:
                            q("a chain link fence that looks like it would crumble at a moment's notice, but also looks incredibly sturdy at the same time.")
                            atkP.fences += 1
                        
                        #HE HAS A GUN
                        elif critnumber == 100:
                            
                            #The other player had a gun
                            if atkP.glocks == 0 and defP.glocks >= 1:
                                q("Ok, great. Now the OTHER guy has a gun.")
                                wait(.5)
                                confirm("\nI'm leaving.", .2)
                            
                            #The current player already had a gun
                            elif atkP.mp >= 1:
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
                                confirm("\nGod landed a destructive hit, doing " + str(999+defP.hp) + " damage to player " + str(defP.id) + ".", 1)
                                defP.damage(defP.hp + 999)
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
                                confirm("Player " + str(defP.id) + " has ValueError HP left.")
                            
                            #The first gun in the game
                            elif atkP.glocks == 0 and defP.glocks == 0:
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
                            atkP.glocks += 1
                            oc = False
                            mc = False
                
                #Gain advantage - 3MP
                elif option == 3:
                    
                    #Not enough MP
                    if atkP.mp < 3:
                        confirm("You don't have enough MP for this.\n")
                    
                    else:
                        confirm("You gained advantage on your next turn.\n")
                        atkP.mp -= 3
                        atkP.adv = 1
                        atkP.adtr = 2
                        oc = False
                        mc = False
                
                #Impose disadvantage - 4MP
                elif option == 4:

                    #Not enough MP
                    if atkP.mp < 4:
                        confirm("You don't have enough MP for that.")
                    
                    else:
                        atkP.mp -= 4
                        oc = False
                        mc = False
                        #If the defending player already had advantage
                        if defP.adv == 1:
                            confirm("You got rid of player " + str(defP) + "'s advantage.")
                            defP.adv = 0
                            defP.adtr = 0

                        #If the defending player has no hit modifiers
                        elif defP.adv == 0:
                            confirm("You gave player " + str(defP.id) + " disadvantage on their next turn.")
                            defP.adv = 2
                            defP.adv = 1
                        
                        #If the defending player has disadvantage
                        elif defP.adv == 2:
                            confirm("You continuted player " + str(defP.id) + "'s disadvantage by one more turn.")
                            defP.adv = 2
                            defP.adtr = 1
                        
                        else:
                            explode()
                    
                #Heal 20% - 4MP
                elif option == 5:
                    
                    #Not enough MP
                    if atkP.mp < 4:
                        confirm("You don't have enough MP for that.")
                    
                    #Already at max HP
                    elif atkP.hp == atkP.hpMAX:
                        confirm("You're already at max HP.")
                    
                    else:
                        atkP.mp -= 4
                        HEAL = round(atkP.hpMAX/5)
                        confirm("You healed " + str(HEAL) + " points of damage.")
                        atkP.heal(HEAL)
                        oc = False
                        mc = False

                #Damage boost - 2MP
                elif option == 6:
                    
                    #Not enough MP
                    if atkP.mp < 2:
                        confirm("You don't have enough MP.")
                    
                    #Already have the boost
                    elif atkP.dmgBON > 0:
                        q("You are already under the effect of this.")
                    
                    else:
                        atkP.mp -= 2
                        atkP.dmgBON = round(atkP.atk/3)
                        confirm("You gained a damage boost of " + str(atkP.dmgBON) + " damage.")
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
                q("1: Spoon - " + str(atkP.spoons) + "\n")
                wait()
                q("2: Knife - " + str(atkP.knives) + "\n")
                wait()
                q("3: Potion - " + str(atkP.potions) + "\n")
                wait()
                q("4: Chain Fence (uses 3 item uses) - " + str(atkP.fences) + "\n")
                wait()

                #Print Properly if the gun is in play
                if atkP.glocks >= 1:
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
                            if atkP.spoons < 1:
                                confirm("You don't have any spoons. No soup for you.")
                            
                            else:
                                critnumber = random_num(1,1000,False)

                                #Fence
                                if defP.fence_set:
                                    confirm("You struck player " + str(defP.id) + "'s fence")
                                    defP.fence_set = False
                                else:

                                    #The chance to instantly kill the other player due to tetanus
                                    if critnumber == 1000:
                                        confirm("Player " + str(defP) + " got tetanus from being hit with the spoon, dying on the spot.")
                                        defP.damage(defP.hp)
                                        items_left = 1
                                
                                    #The chance to intantly die due to tetanus from holding the spoon
                                    elif critnumber == 1:
                                        confirm("Player " + str(atkP.id) + " wasn't safe from the spoon. While they were holding it, they got tetanus and died.")
                                        atkP.damage(atkP.hp)
                                        items_left = 1
                                
                                    #Everything is good
                                    else:
                                        confirm("Player " + str(atkP.id) + " did 1 point of damage to player " + str(defP.id) + ".")
                                        defP.damage(1)
                                    
                                    items_left -= 1
                                    atkP.spoons -= 1
                        
                        #Knife
                        elif option == 2:
                            
                            #No knife
                            if atkP.knives < 1:
                                ask("You don't have any knives. Want a pencil instead? ",.3)
                                q("Well I don't have any.\n")
                                wait(.5)
                            
                            else:
                                critnumber = random_num(1,50,show)

                                #Miss
                                if critnumber == 1:
                                    confirm("You threw a knife, completely missing your opponent.")
                                
                                #Fence
                                elif defP.fence_set:
                                    confirm("You stuck player " + str(defP.id) + "'s fence")
                                    defP.fence_set = False

                                #Hit
                                else:
                                    critnumber = random_num(1,5,show)
                                    confirm("You threw a knife, doing " + str(critnumber) + " damage to player " + str(defP.id) + ".")
                                    defP.damage(critnumber)
                                atkP.knives -= 1
                                items_left -= 1
                        
                        #Healing Potion
                        elif option == 3:

                            #No potions
                            if atkP.potions < 1:
                                q("You don't have any healing poitions.")
                                wait(.3)
                                confirm("\nstr(potion_joke) + '.'")
                            
                            else:
                                HEAL = round(atkP.hpMAX/10)
                                confirm("You healed " + str(HEAL) + " points of damage.")
                                atkP.heal(HEAL)
                                atkP.potions -= 1
                                items_left -= 1
                        
                        #Chain link fence
                        elif option == 4:
                            
                            #No fence
                            if atkP.fences < 1:
                                confirm("You don't have a fence. Besides, who carries entire fences with them?")
                            
                            #Not enough item uses
                            elif items_left < 3:
                                confirm("You need three item uses to set this up.")
                            
                            #Already have a fence set up
                            elif atkP.fence_set:
                                confirm("You already have a fence set up.")

                            else:
                                confirm("You set up an enitre fence in front of you. Looks like it could block a hit")
                                atkP.fence_set = True
                                atkP.fences -= 1
                                items_left -= 3
                                ic = False
                        
                        #Gun if possible
                        elif option == 5 and atkP.glocks >= 1:
                            critnumber = random_num(1,1000)
                            
                            #Miss
                            if critnumber == 1:
                                confirm("You missed.",.2)
                                q("And that's the last shot in the clip.\n")
                                wait(1)
                                confirm("My man really summoned a one-shot weapon with one shot.")
                                atkP.glocks -= 1
                            
                            #So anyway, I started blasting
                            else:
                                
                                #FENCE
                                if defP.fence_set == 1:
                                    confirm("You shot player " + str(defP.id) + "'s fence.")
                                    items_left -= 1
                                else:
                                    confirm("You shot your gun, hitting player " + str(defP.id) + " and doing ValueError damage to them.")
                                    defP.hp = 0
                                    items_left = 0
                                    ic = False
                                    oc = False  
                                atkP.glock -= 1
                        
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
                    atkP.hp = 0
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
    return atkP, defP

#Setting default rule values
print_random = False

#THE GAME#
#Insert loading sequence here when you figure out how to do that
confirm("If you are a new player, please consult the guide",1)
q("\nWelcome to Dungeons and Damage")
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
        player1 = charSelect(1)
        player2 = charSelect(2)
        
        #GameCorrect
        gc = True
        while gc:
            
            #Player 1 is faster than Player 2
            if player1.spd > player2.spd:
                confirm("Player 1 has " + str(player1.hp) + "/" + str(player1.hpMAX) + "HP remaining; " + str(player1.mp) + "/" + str(player1.mpMAX) + "MP remaining.")
                confirm("Player 2 has " + str(player2.hp) + "/" + str(player2.hpMAX) + "HP remaining; " + str(player2.mp) + "/" + str(player2.mpMAX) + "MP remaining.")
                player1,player2 = combat(player1,player2,print_random)
                
                #If both Players are alive
                if player1.alive and player2.alive:
                    player2,player1 = combat(player2,player1,print_random)
                    
                    #If both Players are alive
                    if player2.alive and player1.alive:
                        player1.next_turn()
                        player2.next_turn()
                    
                    #At least one of them is dead
                    else:

                        #Both are dead
                        if not player1.alive and not player2.alive:
                            confirm("Both players are out of HP. The game is resulting in a tie.")
                        
                        #Just Player 2 is dead
                        elif not player2.alive:
                            confirm("Player 2 is out of HP. They have lost the game.")
                        
                        #Just Player 1 is dead
                        elif not player1.alive:
                            confirm("Player 1 is out of HP. They have lost the game.")
                        gc = False
                
                #At least one of them is dead
                else:
                    
                    #Both are dead
                    if not player2.alive and not player1.alive:
                        confirm("Both players are out of HP. The game is resulting in a tie.")
                    
                    #Just Player 1 is dead
                    elif not player1.alive:
                        confirm("Player 1 is out of HP. They have lost the game.")
                    
                    #Just Player 2 is dead
                    elif not player2.alive:
                        confirm("Player 2 is out of HP. They have lost the game")
                    gc = False
            elif player2.spd > player1.spd:
                confirm("Player 2 has " + str(player2.hp) + "/" + str(player2.hpMAX) + "HP remaining; " + str(player2.mp) + "/" + str(player2.mpMAX) + "MP remaining.")
                confirm("Player 1 has " + str(player1.hp) + "/" + str(player1.hpMAX) + "HP remaining; " + str(player1.mp) + "/" + str(player1.mpMAX) + "MP remaining.")
                player2,player1 = combat(player2,player1,print_random)
                
                #If both Players are alive
                if player2.alive and player1.alive:
                    player1,player2 = combat(player1,player2,print_random)
                    
                    #If both Players are alive
                    if player1.alive and player2.alive:
                        player2.next_turn()
                        player1.next_turn()
                    
                    #At least one of them is dead
                    else:

                        #Both are dead
                        if not player2.alive and not player1.alive:
                            confirm("Both players are out of HP. The game is resulting in a tie.")
                        
                        #Just Player 1 is dead
                        elif not player1.alive:
                            confirm("Player 1 is out of HP. They have lost the game.")
                        
                        #Just Player 2 is dead
                        elif not player2.alive:
                            confirm("Player 2 is out of HP. They have lost the game.")
                        gc = False
                
                #At least one of them is dead
                else:
                    
                    #Both are dead
                    if not player1.alive and not player2.alive:
                        confirm("Both players are out of HP. The game is resulting in a tie.")
                    
                    #Just Player 2 is dead
                    elif not player2.alive:
                        confirm("Player 2 is out of HP. They have lost the game.")
                    
                    #Just Player 1 is dead
                    elif not player1.alive:
                        confirm("Player 1 is out of HP. They have lost the game")
                    gc = False
            elif player1.spd == player2.spd:
                first = random.randint(1,2)
                if first == 1:
                    player1.spd += 1
                elif first == 2:
                    player2.spd += 1
                else:
                    explode()
            else:
                explode()

    else:
        q("Please give a provided number.")
        wait(.3)
        q("\n")
