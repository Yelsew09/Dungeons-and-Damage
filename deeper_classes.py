import random,time,sys
global print_random,AntiMagic,AntiMagictr
print_random = True
AntiMagic = False
AntiMagictr = 0

#Commands that help with the program
def q(str, t = .02):

    #I have no idea how this works, it just does
    #It rolls text instead of printing it all at once
    for char in str:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(t)
def wait(t = .15):

    #Used for timings between text
    #I could just use time.sleep, but I'm lazy
    time.sleep(t)
def confirm(str, t = .5):

    #Makes sure the player has read the terms
    q(str)
    input(' >')
    wait(t)
def random_num(minimum,maximum,ad):

    #Generates a random number, accounting for advantage
    num1 = random.randint(minimum,maximum)
    num2 = random.randint(minimum,maximum)
    if ad == 1:
        critnumber = max(num1,num2)
    elif ad == 2:
        critnumber = min(num1,num2)
    else:
        critnumber = random.randint(minimum,maximum)
    if print_random:
        confirm(f"You rolled a {critnumber}!")
    return critnumber
def ask(str,t = .5):

    #Asks for an option, will only output a number
    ec = True
    while ec:
        try:
            q(str)
            option = int(input(''))
            ec = False
            time.sleep(t)
        except ValueError:
            q(f"Please provide a number.")
            time.sleep(t)
            q(f"\n")
    return option
def y_or_n(asking):

    #Asks a yes or no question, just saves space later
    #Be sure to set it equal to a correct variable
    ync = True
    while ync:
        q(f"1: Yes\n")
        wait()
        q(f"2: No\n")
        wait()
        option = ask(asking)
        if option == 1:
            loop = False
            ync = False
        elif option == 2:
            loop = True
            ync = False
        else:
            q(f"Please give a valid option\n")
    return loop
def diceroll(amount,sides,starting = 0):

    #Dice rolls
    final_number = starting
    printed = "You rolled values of: "
    for i in range (amount):
        added = random.randint(1,sides)
        final_number += added
        if i == 0:
            printed += str(added)
        else:
            printed += ", " + str(added)
    if print_random:
        confirm(printed)
    return final_number
def explode():
    
    #Boom
    try:
        explode()
    except:
        explode()
def qlist(list,returntype,asking = "What would you like to do? ",):
    for option in range(len(list)):
        q(f"{option} - {list[option]}\n")
        wait()
    option = ask(asking)
    if returntype:
        try:
            option = list[option]
        except:
            pass
    else:
        pass
    return option

#Spell commands
def AntiMagicArea(user):
    if user.mp < 10:
        confirm(f"You don't have enough MP for that.")
        loop = True
    elif AntiMagic:
        confirm(f"There is already an Antimagic Bubble up.")
        loop = True
    else:
        confirm(f"You set up an Antimagic Bubble. Spells are now uncastable for the next 2 turns.")
        user.mp -= 10
        AntiMagic = True
        AntiMagictr = 3
    return user,loop
def BladeWard(user,target):
    if user.mp < 7:
        confirm(f"You don't have enough MP for that.")
        loop = True
    elif target.BladeWard:
        confirm(f"Player {target.id} is already under the effect of that spell.")
        loop = True
    else:
        confirm(f"Player {str(target.id)} will take 1/2 damage the next time they are damaged by a physical attack.")
        target.BladeWard = True
        user.mp -= 7
        loop = False
    return user,target,loop
def Frost(user,target):
    if user.mp < 3:
        confirm(f"You don't have enough MP for that.")
        loop = True
    else:
        confirm(f"You slowed player {target.id} for a turn.")
        target.frost = True
        target.frostr = 2
        user.mp -= 3
        loop = False
    return user,target,loop
def CounterSpell(user):
    if user.mp < 3:
        confirm(f"You don't have enough MP for that.")
        loop = True
    elif user.counterspell:
        confirm(f"You are already under the effect of this spell.")
        loop = True
    else:
        confirm(f"The next spell that you are the target of just won't work.")
        user.counterspell = True
        loop = True
def Fireball(user,target):
    if user.mp < 5:
        confirm(f"You don't have enough MP for that.")
        loop = True
    else:
        damage = diceroll(3,8)
        if damage < round(target.defence/2):
            confirm(f"The magic was too weak, and it was blocked by player {target.id}'s armor.")
            loop = True
        else:
            confirm(f"You did {damage} points of damage to player {target.id}.")
            target.damage(damage)
            user.mp -= 5
            loop = False
    return user,target,loop
def Frostshot(user,target):
    if user.mp < 5:
        confirm(f"You don't have enough MP for that.")
        loop = True
    else:
        damage = diceroll(2,4)
        confirm(f"You did {damage} damage to player {target.id}, and slowed them for a turn.")
        target.damage(damage)
        target.frost = True
        target.frostr = 2
        user.mp -= 5
        loop = False
    return user,target,loop
def Firebolt(user,target):
    if user.mp < 3:
        confirm(f"You don't have enough MP for that.")
        loop = True
    else:
        damage = diceroll(2,6)
        confirm(f"You did {damage} damage to player {target.id}.")
        target.damage(damage)
        loop = False
    return user,target,loop
def MagicArmor(user,target):
    if user.mp < 2:
        confirm(f"You don't have enough MP for that.")
        loop = True
    else:
        target.defBON = diceroll(2,4)
        confirm(f"Player " + str(target.id) + " gained a defence bonus of " + str(target.defBON) + ".")
        user.mp -= 2
        loop = False
    return user,target,loop
def DaggerCloud(user,target):
    if user.mp < 2:
        confirm(f"You don't have enough MP for that.")
        loop = True
    elif user.knives < 5:
        confirm(f"You need at least 5 knives to cast this spell. You have " + str(user.knives) + ".")
    else:
        damage = diceroll(5,5)
        confirm(f"You did " + str(damage) + " damage to player " + str(target.id) + ".")
        user.knives -= 5
        user.mp -= 2
        loop = False
    return user,target,loop
def PoisonDart(user,target):
    if user.mp < 6:
        confirm(f"You don't have enough MP for that.")
        loop = True
    else:
        target.poison = diceroll(1,4)
        target.poisontr = random.randint + 1
        confirm(f"You did {target.poison + 2} damage to player {target.id}.")
        target.damage(target.poison)
        user.mp -= 6
        loop = False
    return user,target,loop
def Dispel(user,target):
    if user.mp < 5:
        confirm(f"You don't have enough MP for that.")
        loop = True
    else:
        target.mp = round(target.mp/2)
        confirm(f"You halved player {target.id}'s MP, leaving them on {target.mp}MP.")
        user.mp -= 5
        loop = False
    return user,target,loop
def Slow(user,target):
    if user.mp < 7:
        confirm(f"You don't have enough MP for that.")
        loop = True
    else:
        target.spd = round(target.spd/2)
        confirm(f"You halved player {target.id}'s MP, leaving them with a speed of {target.spd} for a turn.")
        target.slowtr = 2
        user.mp -= 7
        loop = False
    return user,target,loop
def TrueStrike(user,target):
    if user.mp < 4:
        confirm(f"You don't have enough MP for that.")
        loop = True
    elif target.TrueHit:
        confirm(f"The target is already guaranteed to hit their next attack.")
        loop = True
    else:
        confirm(f"You will hit your next attack, guarenteed.")
        target.TrueHit = True
        user.mp -= 4
        loop = False
    return user,target,loop

""" FORMAT FOR PRINTING AND USING ACTIONS

#The list of actions
actions = ["Attack","Magic",etc.]

#Whatever correct variable is being used
CorrectVar = True
while CorrectVar:

    #Prints the list of options with a corrosponding number
    for action in range(len(attacker.actions)):
        q(f{action + 1} - {actions[action]}\n")
        wait()
    
    #User input
    option = ask(f"What would you like to do? ")

    #Converts option to a string value
    option = str(attacker.actions[option - 1])
    
    #Compares string value to list of given actions
    if option == "Attack":
        #Attack
    elif option == "Magic":
        #Magic
    elif option == "etc.":
        #etc.

Thanks Ian
I also learned about pass from that
"""

class Player():
    numplayers = 0
    def __init__(self,h,a,aM,d,m,mR,s,i,n):
        Player.numplayers += 1
        self.hp = h
        self.hpMAX = h
        self.atk = a
        self.atkMOD = aM
        self.defence = d
        self.mp = m
        self.mpMAX = m
        self.mpREF = mR
        self.spd = s
        self.itemuses = i
        self.classname = str(n)
        self.id = Player.numplayers
        self.abil = False
        self.abilTR = 0
        self.spoons = 0
        self.knives = 0
        self.potions = 0
        self.fences = 0
        self.dmgBON = 0
        self.defBON = 0
        self.fence_set = False
        self.alive = True
        #Add status variables here
        self.adv = 0
        self.advtr = 0
    def heal(self,amount):
        self.hp += amount
        if self.hp > self.hpMAX:
            self.hp = self.hpMAX
    def damage(self,amount):
        self.hp -= amount
        if self.hp <= 0:
            self.alive = False
    def die(self):
        self.hp -= self.hp
        self.alive = False
    def next_turn(self):
        print(f"Reset variables for next turn.")
class Knight():
    passive = "Fortitude"
    activated = "Second Wind"
    stats = {
        'hp': 35,
        'atk': 7,
        'atkBON': 5,
        'def': 16,
        'mp': 5,
        'mpREF': 2,
        'spd': 3,
        'items': 2,
    }
    actions = [
        "Attack",
        "Magic",
        "Second Wind",
        "Items",
        "Pass",
        "Run",
    ]
    spells = [
        "",
        ",",
    ]
    def __init__(self):
        self.stats = Knight.stats
        Player.__init__(self,self.stats['hp'],self.stats['atk'],self.stats['atkBON'],self.stats['def'], \
            self.stats['mp'],self.stats['mpREF'],self.stats['spd'],self.stats['items'],"Knight")
        self.passive = Knight.passive
        self.activated = Knight.activated
        self.actions = Knight.actions
        self.spells = Knight.spells
        self.abilREF = 3
        self.knives = 3
        self.potions = 5
        self.fences = 1
    def heal(self,amount):
        Player.heal(self,amount)
    def damage(self,amount):
        if amount >= 3:
            amount -= 2
        Player.damage(self,amount)
    def die(self):
        Player.die(self)
    def next_turn(self):
        Player.next_turn(self)
class Peashooter():
    passive = "Charge"
    activated = "Volley"
    stats = {
        'hp': 26,
        'atk': 9,
        'atkBON': 4,
        'def': 14,
        'mp': 7,
        'mpREF': 3,
        'spd': 5,
        'items': 3,
    }
    actions = [
        "Attack",
        "Magic",
        "Volley",
        "Items",
        "Pass",
        "Run",
    ]
    spells = [
        "",
        ",",
    ]
    def __init__(self):
        self.stats = Peashooter.stats
        Player.__init__(self,self.stats['hp'],self.stats['atk'],self.stats['atkBON'],self.stats['def'], \
            self.stats['mp'],self.stats['mpREF'],self.stats['spd'],self.stats['items'],"Peashooter")
        self.passive = Peashooter.passive
        self.activated = Peashooter.activated
        self.actions = Peashooter.actions
        self.spells = Peashooter.spells
        self.spoons = 1
        self.knives = 2
        self.potions = 2
    def heal(self,amount):
        Player.heal(self,amount)
    def damage(self,amount):
        Player.heal(self,amount)
    def die(self):
        Player.die(self)
    def next_turn(self):
        if self.mp == self.mpMAX:
            self.dmgBON += 3
        Player.next_turn(self)
class Rouge():
    passive = "Accelerate"
    activated = "Sneak Attack"
    stats = {
        'hp': 20,
        'atk': 10,
        'atkBON': 3,
        'def': 13,
        'mp': 6,
        'mpREF': 2,
        'spd': 4,
        'items': 4,
    }
    actions = [
        "Attack",
        "Magic",
        "Sneak Attack",
        "Item",
        "Pass",
    ]
    spells = [
        "",
        ",",
    ]
    def __init__(self):
        self.stats = Rouge.stats
        Player.__init__(self,self.stats['hp'],self.stats['atk'],self.stats['atkBON'],self.stats['def'], \
            self.stats['mp'],self.stats['mpREF'],self.stats['spd'],self.stats['items'],"Rouge")
        self.passive = Rouge.passive
        self.activated = Rouge.activated
        self.actions = Rouge.actions
        self.spells = Rouge.spells
        self.spoons = 2
        self.knives = 3
        self.potions = 1
        self.fences = 1
    def heal(self,amount):
        Player.heal(self,amount)
    def damage(self,amount):
        Player.damage(self,amount)
    def die(self):
        Player.die(self)
    def next_turn(self):
        if self.spd >= 9:
            pass
        else:
            self.spd += 1
        Player.next_turn(self)
class Mage():
    passive = "Zoning in"
    activated = "Magical Fury"
    stats = {
        'hp': 21,
        'atk': 5,
        'atkBON': 2,
        'def': 11,
        'mp': 5,
        'mpREF': 2,
        'spd': 4,
        'items': 2,
    }
    actions = [
        "Attack",
        "Magic",
        "Magical Fury",
        "Item",
        "Pass",
    ]
    spells = [
        "",
        ",",
    ]
    def __init__(self):
        self.stats = Mage.stats
        Player.__init__(self,self.stats['hp'],self.stats['atk'],self.stats['atkBON'],self.stats['def'], \
            self.stats['mp'],self.stats['mpREF'],self.stats['spd'],self.stats['items'],"Mage")
        self.passive = Mage.passive
        self.activated = Mage.activated
        self.actions = Mage.actions
        self.spells = Mage.spells
        self.spoons = 1
        self.knives = 1
        self.potions = 4
        self.fences = 2
    def heal(self,amount):
        Player.heal(self,amount)
    def damage(self,amount):
        Player.damage(self,amount)
    def die(self):
        Player.die(self)
    def next_turn(self):
        if self.mp >= 10:
            pass
        else:
            self.mp += 1
            self.mpMAX += 1
            self.mpREF = round(self.mpMAX/2)
class Skele():
    passive = "Impervious"
    activated = "Swirling"
    stats = {
        'hp': 30,
        'atk': 7,
        'atkBON': 3,
        'def': 12,
        'mp': 7,
        'mpREF': 5,
        'spd': 6,
        'items': 4,
    }
    actions = [
        "Attack",
        "Magic",
        "Swirl",
        "Item",
        "Pass",
    ]
    spells = [
        "",
        ",",
    ]
    def __init__(self):
        self.stats = Skele.stats
        Player.__init__(self,self.stats['hp'],self.stats['atk'],self.stats['atkBON'],self.stats['def'], \
            self.stats['mp'],self.stats['mpREF'],self.stats['spd'],self.stats['items'],"Skele")
        self.passive = Skele.passive
        self.activated = Skele.activated
        self.actions = Skele.actions
        self.spells = Skele.spells
        self.knives = 6
    def heal(self,amount):
        Player.heal(self,amount)
    def damage(self,amount):
        if amount > 15:
            confirm(f"But Impervious stops Skele from taking more than 15 damage at a time.")
            amount = 15
        Player.damage(self,amount)
    def die(self):
        Player.die(self)
    def next_turn(self):
        Player.next_turn(self)
class Bard():
    passive = "Boosted"
    actiavted = "Jack of All Trades"
    stats = {
        'hp': 25,
        'atk': 5,
        'atkBON': 5,
        'def': 14,
        'mp': 4,
        'mpREF': 2,
        'spd': 2,
        'items': 5,
    }
    actions = [
        "Attack",
        "Magic",
        "Stat Change",
        "Item",
        "Pass",
    ]
    spells = [
        "",
        ",",
    ]
    def __init__(self):
        self.stats = Bard.stats
        Player.__init__(self,self.stats['hp'],self.stats['atk'],self.stats['atkBON'],self.stats['def'], \
            self.stats['mp'],self.stats['mpREF'],self.stats['spd'],self.stats['items'],"Bard")
        self.passive = Bard.passive
        self.activated = Bard.actiavted
        self.actions = Bard.actions
        self.spells = Bard.spells
        self.spoons = 5
        self.knives = 5
        self.potions = 3
        self.fences = 2
    def heal(self,amount):
        Player.heal(self,amount)
    def damage(self,amount):
        Player.damage(self,amount)
    def die(self):
        Player.die(self)
    def next_turn(self):
        # Select new stat block
        Player.next_turn(self)
class Barbarian():
    passive = "Healthy"
    activated = "Brutal"
    stats = {
        'hp': 40,
        'atk': 12,
        'atkBON': 2,
        'def': 15,
        'mp': 2,
        'mpREF': 2,
        'spd': 1,
        'items': 1,
    }
    actions = [
        "Attack",
        "Magic",
        "Smash",
        "Item",
        "Pass",
    ]
    spells = [
        "",
        ",",
    ]
    def __init__(self):
        Player.__init__(self,self.stats['hp'],self.stats['atk'],self.stats['atkBON'],self.stats['def'], \
            self.stats['mp'],self.stats['mpREF'],self.stats['spd'],self.stats['items'],"Barbarian")
        self.passive = Barbarian.passive
        self.activated = Barbarian.passive
        self.actions = Barbarian.actions
        self.spells = Barbarian.spells
    def heal(self,amount):
        amount = round(amount*1.5)
        Player.heal(self,amount)
    def damage(self,amount):
        Player.damage(self,amount)
    def die(self):
        Player.die(self)
    def next_turn(self):
        self.heal(2)
        Player.next_turn(self)
class Custom():
    passive = None
    activated = None
    actions = [
        "Attack",
        "Item",
        "Pass",
    ]
    spells = [
        "",
        ",",
    ]
    def __init__(self,h,a,aB,d,m,mB,s,i,n):
        self.stats = {
            'hp': h,
            'atk': a,
            'atkBON': aB,
            'def': d,
            'mp': m,
            'mpREF': mB,
            'spd': s,
            'items': i,
        }
        self.passive = Custom.passive
        self.activated = Custom.activated
        Player.__init__(self,self.stats['hp'],self.stats['atk'],self.stats['atkBON'],self.stats['def'], \
            self.stats['mp'],self.stats['mpREF'],self.stats['spd'],self.stats['items'],str(n))
        self.actions = Custom.actions
        self.spells = Custom.spells
        if self.mp > 0:
            self.actions = [
                "Attack",
                "Magic",
                "Item",
                "Pass",
            ]
    def heal(self,amount):
        Player.heal(self,amount)
    def damage(self,amount):
        Player.damage(self,amount)
    def die(self):
        Player.die(self)
    def next_turn(self):
        Player.next_turn(self)
class God():
    passive = "Unkillable"
    activated = "Destructive Hit"
    stats = {
        'hp': 88224646790,
        'atk': 88224646790,
        'atkBON': 88224646790,
        'def': 88224646790,
        'mp': 88224646790,
        'mpREF': 88224646790,
        'spd': 88224646790,
        'items': 88224646790,
    }
    actions = [
        "Attack",
        "Magic",
        "Destructive Hit",
        "Item",
        "Pass",
    ]
    spells = [
        "Literally everything",
        ",",
    ]
    def __init__(self):
        self.stats = God.stats
        Player.__init__(self,self.stats['hp'],self.stats['atk'],self.stats['atkBON'],self.stats['def'], \
            self.stats['mp'],self.stats['mpREF'],self.stats['spd'],self.stats['items'],"-.- --- -. .- -- .. ....... -.-. --- -.. .")
        self.passive = God.passive
        self.activated = God.activated
        self.actions = God.actions
        self.spells = God.spells
        self.spoons = 88224646790
        self.knives = 88224646790
        self.potions = 88224646790
        self.fences = 88224646790
    def heal(self,amount):
        amount = self.hpMAX
        Player.heal(self,amount)
    def damage(self,amount):
        amount = round(amount/10)
        Player.damage(amount)
    def die(self):
        confirm("This character has the 'Unkillable' trait, so even the coder of this game can't instantly kill them.")
    def next_turn(self):
        self.heal(1)
        self.adv = 1
        self.advtr = 2
        Player.next_turn(self)

# FINALLY, THE ACTUAL GAME
# Commands used as part of the actual game
def charselect(playernum):
    #CharacterCorrect
    cc = True
    while cc:
        options = [
        "Back",
        "Knight",
        "Peashooter",
        "Rouge",
        "Mage",
        "Skele",
        "Bard",
        "Barbarian",
        "Custom",
        "Random",
    ]
        option = qlist(options,True, f"Please select a class, player {playernum}: ")
        rc = True
        while rc:

            #Back
            if option == "Back":
                rc = False
                cc = False
                skip = True
            
            #Knight
            elif option == "Knight":
                player = Knight()
                rc = False
            
            #Peashooter
            elif option == "Peashooter":
                player = Peashooter()
                rc = False
            
            #Rouge
            elif option == "Rouge":
                player = Rouge()
                rc = False
            
            #Mage
            elif option == "Mage":
                player = Mage()
                rc = False
            
            #Skele
            elif option == "Skele":
                player = Skele()
                rc = False
            
            #Bard
            elif option == "Bard":
                player = Bard()
                rc = False
            
            #Barbarian
            elif option == "Barbarian":
                player = Barbarian()
                rc = False
            
            #Random
            elif option == "Random":
                option = random.randint(1,7)
                option = options[option]
            
            #Custom
            elif option == "Custom":
                hp = 10
                atk = 0
                atkBON = 0
                de = 0
                mp = 0
                mpBON = 0
                spd = 1
                itus = 3
                points = 35

                oc = True
                while oc:
                    options = [
                        f"Back",
                        f"Health Points - {hp}",
                        f"Attack Damage - {atk}",
                        f"Attack Roll Bonus (can be up to 1/2 your Attack Damage) - {atkBON}",
                        f"Defence - " + str(de),
                        f"Magic Points (or magic power) - " + str(mp),
                        f"Magic Point Refresh (can be up to 1/2 your Magic Points) - {mpBON}",
                        f"Speed (minimum 1) - {spd}",
                        f"Item Uses (max 6) - {itus}",
                        f"I'm done",
                    ]
                    option = qlist(options,False, f"What would you like to change (you have {points} points left)? ")
                    if option >= 1 and option <= 7:
                        spent = ask(f"How much would you like to spend on that? ")

                        #Not enough points
                        if spent > points:
                            spent = points

                        #Health Points
                        if option == 1:
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
                    if option == 0:
                        rc = True
                    elif option == 9:
                        if points > 0:
                            rc = y_or_n(f"Are you sure you are done? You still have points to spend. ")
                        else:
                            rc = False
                    else:
                        q(f"Please give a valid option.")
                        wait(.5)
                        q(f"\n")
                player = Custom()
                rc = False
            
            #GOD
            elif option == 88224646790:
                player = God()
                rc = False
            
            else:
                q(f"Please choose a valid option")
                rc = False
                skip = True
        if skip:
            pass
        else:
            cc = y_or_n(f"You have chosen the {player.name} class, is this correct? ")
def take_turn(atkP,defP):

    confirm(f"This is player {atkP.id}'s turn.")
    items_left = atkP.itus
    #OptionCorrect
    oc = True
    while oc:
        option = qlist(atkP.options,True)
        if option == "Attack":
            if defP.fence_set:
                confirm(f"You struck player {defP.id}'s fence.")
                defP.fence_set = False
            else:
                critnumber = random_num(1,20,atkP.adv)
                if critnumber == 20:
                    q(f"IT'S A CRITICAL HIT!!!")
                    wait(.5)
                    confirm(f"\nYou did {(atkP.atk*2) + atkP.dmgBON} to player {defP.id}.")
                    defP.damage((atkP.atk*2) + atkP.dmgBON)
                elif critnumber + atkP.atkMOD >= defP.defence + defP.defBON:
                    confirm(f"You landed a hit, doing {atkP.atk + atkP.dmgBON}")
                    defP.damage(atkP.atk + atkP.dmgBON)
                elif critnumber + atkP.atkMOD < defP.defence + defP.defBON:
                    confirm(f"You missed your attack.")
                oc = False
                atkP.dmgBON = 0
        elif option == "Magic":
            
            #MagicCorrect
            mc = True
            while mc:
                q(f"0 - Back\n")
                wait()
                option = qlist(atkP.spells,True, f"What would you like to cast? ")
                if option == "Fireball":
                    mc = Fireball(atkP,defP)
                #Repeat for list of spells
                else:
                    q(f"Please choose a valid option.")
                    wait(.5)
                    q("\n")
        elif option == "Item":
            ic = True
            while ic:
                if items_left == 0:
                    confirm(f"You are out of item uses")
                    ic = False
                else:
                    options = [
                        "Back",
                    ]
                    if atkP.spoons > 0:
                        options += f"Spoons - {atkP.spoons}"
                    if atkP.knives > 0:
                        options += f"Knives - {atkP.knives}"
                    if atkP.potions > 0:
                        options += f"Potions - {atkP.potions}"
                    if atkP.fences > 0:
                        options += f"Fences - {atkP.fences}"
                    if atkP.glocks > 0:
                        options += f"Glocks - {atkP.glocks}"
                    
                    while items_left > 0:
                        option = qlist(options,True, f"What would you like to use? ")
                        if option == f"Spoons - {atkP.spoons}":
                            if defP.fence_set:
                                confirm(f"You struck player {defP.id}'s fence.")
                                defP.fence_set = False
                            else:
                                critnumber = random.randint(1,1000)
                                if critnumber == 1:
                                    q(f"The spoon infected you (player {atkP.id}) with tetanus.")
                                    wait()
                                    confirm(f"\nUnfortunatly, this game takes place before the tetanus shot, so you died instantly.")
                                    atkP.die()
                                elif critnumber == 1000:
                                    q(f"The spoon infected player {defP.id} with tetanus.")
                                    wait()
                                    confirm(f"\nUnfortunatly, this game takes place before the tetanus shot, so they died instantly.")
                                    defP.die()
                                else:
                                    confirm(f"You threw a spoon, doing 1 point of damage to player {defP.id}.")
                                    defP.damage(1)
                            atkP.spoons -= 1
                            items_left -= 1
                        elif option == f"Knives - {atkP.knives}":
                            if defP.fence_set:
                                confirm(f"You struck player {defP.id}'s fence.")
                                defP.fence_set = False
                            else:
                                critnumber = random.randint(1,10)
                                if critnumber == 1:
                                    confirm(f"You missed your throw.")
                                else:
                                    critnumber = random.randint(1,5)
                                    confirm(f"You threw a knife, doing {critnumber} damage to player {defP.id}.")
                                    defP.damage(critnumber)
                            atkP.knives -= 1
                            items_left -= 1
                        elif option == f"Potions - {atkP.Potions}":
                            if atkP.hp == atkP.hpMAX:
                                confirm(f"You are already at maximum hp")
                            else:
                                confirm(f"You healed {round(atkP.hpMAX/10)}HP.")
                                atkP.heal(round(atkP.hpMAX/10))
                                atkP.potions -= 1
                                items_left -= 1
                        elif option == f"Fences - {atkP.fences}":
                            if atkP.fence_set:
                                confirm(f"You already have a fence set up.")
                            elif atkP.itus <= 3 and not items_left == atkP.itus:
                                confirm(f"As a {atkP.classname}, you need all of your item uses to use a fence.")
                            elif atkP.itus > 3 and not items_left >= 3:
                                confirm(f"You need 3 item uses to use a fence.")
                            else:
                                confirm(f"You set up a fence.")
                                atkP.fence_set = True
                                atkP.fences -= 1
                        elif option == f"Glocks - {atkP.glocks}":
                            print(f"BANG")
                            critnumber = random.randint(1,1000)
                            if critnumber == 1:
                                q(f"You missed your shot.")
                                wait(2)
                                confirm(f"\nMy man really conjured a one-shot weapon with one shot.")
                            else:
                                confirm(f"The shot landed, instantly killing player {defP.id}.")
                                defP.die()
                            atkP.glocks -= 1
                            items_left = 0
                            ic = False
                            oc = False
                        else:
                            q(f"Please provide a valid option.")
                            wait(.5)
                            q("\n")
        elif option == "Pass":
            confirm("You passed your turn.")
            oc = False
        else:
            q("Please choos a valid option.")
            wait(.5)
            q("\n")

    return atkP, defP

##GAME LOGIC##
confirm(f"If you are a new player, please consult the guide.",1)

q(f"\n")
q(f"Welcome to Dungeons and Damage")
wait(1)
q(f"\nNot to be confused with Dungeons and Dragons")
wait(1)
q(f"\nEven though this is a *somewhat* blatent rip-off")
wait(.5)
q(f"\n")
wait(.5)

#AllCorrect
ac = True
while ac:
    roundnum = 1
    options = [
        "",
        "Game Start",
        "Guide",
        "Options",
        "Quit",
    ]
    option = qlist(options,True,f"Please select an option: ")
    if option == "Guide":
        confirm(f"Guide coming soon.")
    elif option == "Options":
        confirm(f"Options coming soon.")
    elif option == "Quit":
        ac = False
    elif option == "Game Start":
        player1 = charselect(1)
        player2 = charselect(2)

        #GameCorrect
        gc = True
        while gc:

            #Player 1 is dead
            if not player1.alive:
                confirm(f"Player 1 is out of HP. They have lost.")
                gc = False
            
            #Player 2 is dead
            elif not player2.alive:
                confirm(f"Player 2 is out of HP. They have lost.")
                gc = False
            
            #Everyone's health
            else:
                #Player 1 is faster than player 2
                if player1.spd > player2.spd:
                    first = player1.id
                
                #Player 2 is faster than player 1
                elif player2.spd > player1.spd:
                    first = player2.id
                
                #Both players are tied for speed
                else:
                    confirm(f"Both players are tied for speed. Picking a random player to go first.")
                    first = random.randint(player1.id,player2.id)
                    confirm(f"Player {first} is going first")
                if first == player1.id:
                    confirm(f"This is the start of round {roundnum}.")
                    confirm(f"Player 1 has {player1.hp}/{player1.hpMAX}HP remaining; {player1.mp}/{player1.mpMAX}MP remaining.")
                    confirm(f"Player 2 has {player2.hp}/{player2.hpMAX}HP remaining; {player2.mp}/{player2.mpMAX}MP remaining.")
                    player1,player2 = take_turn(player1,player2)

                    if not player1.alive:
                        confirm(f"Player 1 is out of HP. They have lost.")
                        gc = False
                    
                    elif not player2.alive:
                        confirm(f"Player 2 is out of HP. They have lost.")
                        gc = False