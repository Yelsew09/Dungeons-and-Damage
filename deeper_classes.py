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
def random_num(minimum,maximum,ad,show):

    #Generates a random number, accounting for advantage
    num1 = random.randint(minimum,maximum)
    num2 = random.randint(minimum,maximum)
    if ad == 1:
        critnumber = max(num1,num2)
    elif ad == 2:
        critnumber = min(num1,num2)
    else:
        critnumber = random.randint(minimum,maximum)
    if show:
        confirm("You rolled a " + str(critnumber) + "!")
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
            q("Please provide a number.")
            time.sleep(t)
            q("\n")
    return option
def y_or_n(asking):

    #Asks a yes or no question, just saves space later
    #Be sure to set it equal to a correct variable
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
def diceroll(amount,sides):

    #Dice rolls
    final_number = 0
    printed = "You rolled values of : "
    for i in range (amount):
        added = random.randint(1,sides)
        final_number += added
        if i == 1:
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

#Spell commands
def AntiMagicArea(user):
    if user.mp < 10:
        confirm("You don't have enough MP for that.")
        loop = True
    elif AntiMagic:
        confirm("There is already an Antimagic Bubble up.")
        loop = True
    else:
        confirm("You set up an Antimagic Bubble. Spells are now uncastable for the next 2 turns.")
        user.mp -= 10
        AntiMagic = True
        AntiMagictr = 3
    return user,loop
def BladeWard(user,target):
    if user.mp < 7:
        confirm("You don't have enough MP for that.")
        loop = True
    elif target.BladeWard:
        confirm("Player " + str(target.id) + " is already under the effect of that spell.")
        loop = True
    else:
        confirm("Player " + str(target.id) + " will take 1/2 damage the next time they are damaged by a physical attack.")
        target.BladeWard = True
        user.mp -= 7
        loop = False
    return user,target,loop
def Frost(user,target):
    if user.mp < 3:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        confirm("You slowed player " + str(target.id) + " for a turn.")
        target.frost = True
        target.frostr = 2
        user.mp -= 3
        loop = False
    return user,target,loop
def CounterSpell(user):
    if user.mp < 3:
        confirm("You don't have enough MP for that.")
        loop = True
    elif user.counterspell:
        confirm("You are already under the effect of this spell.")
        loop = True
    else:
        confirm("The next spell that you are the target of just won't work.")
        user.counterspell = True
        loop = True
def Fireball(user,target):
    if user.mp < 5:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        damage = diceroll(3,8)
        if damage < round(target.defence/2):
            confirm("The magic was too weak, and it was blocked by player " + str(target.id) + "'s armor.")
            loop = True
        else:
            confirm("You did " + str(damage) + " points of damage to player " + str(target.id) + ".")
            target.damage(damage)
            user.mp -= 5
            loop = False
    return user,target,loop
def Frostshot(user,target):
    if user.mp < 5:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        damage = diceroll(2,4)
        confirm("You did " + str(damage) + " damage to player " + str(target.id) + ", and slowed them for a turn.")
        target.damage(damage)
        target.frost = True
        target.frostr = 2
        user.mp -= 5
        loop = False
    return user,target,loop
def Firebolt(user,target):
    if user.mp < 3:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        damage = diceroll(2,6)
        confirm("You did " + str(damage) + " damage to player " + str(target.id) + ".")
        target.damage(damage)
        loop = False
    return user,target,loop
def MagicArmor(user,target):
    if user.mp < 2:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        target.defBON = diceroll(2,4)
        confirm("Player " + str(target.id) + " gained a defence bonus of " + str(target.defBON) + ".")
        user.mp -= 2
        loop = False
    return user,target,loop
def DaggerCloud(user,target):
    if user.mp < 2:
        confirm("You don't have enough MP for that.")
        loop = True
    elif user.knives < 5:
        confirm("You need at least 5 knives to cast this spell. You have " + str(user.knives) + ".")
    else:
        damage = diceroll(5,5)
        confirm("You did " + str(damage) + " damage to player " + str(target.id) + ".")
        user.knives -= 5
        user.mp -= 2
        loop = False
    return user,target,loop
def PoisonDart(user,target):
    if user.mp < 6:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        target.poison = diceroll(1,4)
        target.poisontr = random.randint + 1
        confirm("You did " + str(target.poison + 2) + " damage to player " + str(target.id) + ".")
        target.damage(target.poison)
        user.mp -= 6
        loop = False
    return user,target,loop
def Dispel(user,target):
    if user.mp < 5:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        target.mp = round(target.mp/2)
        confirm("You halved player " + str(target.id) + "'s MP, leaving them on " + str(target.mp) + "MP.")
        user.mp -= 5
        loop = False
    return user,target,loop
def Slow(user,target):
    if user.mp < 7:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        target.spd = round(target.spd/2)
        confirm("You halved player " + str(target.id) + "'s MP, leaving them with a speed of " + str(target.spd) + " for a turn.")
        target.slowtr = 2
        user.mp -= 7
        loop = False
    return user,target,loop
def TrueStrike(user,target):
    if user.mp < 4:
        confirm("You don't have enough MP for that.")
        loop = True
    elif target.TrueHit:
        confirm("The target is already guaranteed to hit their next attack.")
        loop = True
    else:
        confirm("You will hit your next attack, guarenteed.")
        target.TrueHit = True
        user.mp -= 4
        loop = False
    return user,target,loop

"""    
# With what you're doing here, it seems like you want to map
# a specific number to a specific action.
actions = ['Attack', 'Magic', 'Second Wind', 'Items', 'Pass']
# Storing items in a list allows you to retrieve them using
# numerical values.
option = 0
#Just use a correct loop here
while option <= 0 or option > len(actions):
    try:
        option = int(input("Give an attack option: "))
    except ValueError:
        pass # This try/except is to handle if someone puts in "hi", or the like.
# Now, you can check what the user put in, and run an action accordingly.
# Shown here is how you can tell what action a player did.
print('Option Selected: ' + str(actions[option+1]))
if option == 1:
    print("Do what you would for Attack.")
elif option == 2:
    print("Do what you would do for Magic.")
# And so on, for all the other options in correspondence with the items in the array.

# Extra: If you want to show the user what actions they can do, you can set something up like this.
for action in range(len(actions)):
    q(str(action + 1) + " - " + str(actions[action]) + "\n")
    wait()
"""

class Player():
    numplayers = 0
    def __init__(self,h,a,aB,d,m,mR,s,i,n):
        Player.numplayers += 1
        self.hp = h
        self.hpMAX = h
        self.atk = a
        self.atkBON = aB
        self.defence = d
        self.mp = m
        self.mpMAX = m
        self.mpREF = mR
        self.spd = s
        self.itemuses = i
        self.classname = str(n)
        self.id = Player.numplayers
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
    def next_turn(self):
        print("Reset variables for next turn.")
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
        self.knives = 3
        self.potions = 5
        self.fences = 1
    def heal(self,amount):
        Player.heal(self,amount)
    def damage(self,amount):
        if amount >= 3:
            amount -= 2
        Player.damage(self,amount)
    def next_turn(self):
        Player.next_turn(self)
class Peashooter ():
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
            self.stats['mp'],self.stats['mpREF'],self.stats['spd'],self.stats['items'],"Knight")
        self.passive = Peashooter.passive
        self.activated = Peashooter.activated
        self.spoons = 1
        self.knives = 2
        self.potions = 2
    def heal(self,amount):
        self.hp += amount
        if self.hp > self.hpMAX:
            self.hp = self.hpMAX
    def damage