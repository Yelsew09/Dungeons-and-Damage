import random,time,sys
global print_random
print_random = True

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
def Fireball(attacker,target):
    if attacker.mp < 5:
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
            attacker.mp -= 5
            loop = False
    return attacker,target,loop
def Frostshot(attacker,target):
    if attacker.mp < 3:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        damage = diceroll(2,4)
        confirm("You did " + str(damage) + " damage to player " + str(target.id) + ", and gave them a -1 to their atkBON for a turn.")
        target.damage(damage)
        target.frost = True
        target.frostr = 2
        attacker.mp -= 3
        loop = False
    return attacker,target,loop
def Firebolt(attacker,target):
    if attacker.mp < 3:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        damage = diceroll(2,6)
        confirm("You did " + str(damage) + " damage to player " + str(target.id) + ".")
        target.damage(damage)
        loop = False
    return attacker,target,loop
def MagicArmor(attacker,target):
    if attacker.mp < 2:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        target.defBON = diceroll(2,4)
        confirm("Player " + str(target.id) + " gained a defence bonus of " + str(target.defBON) + ".")
        attacker.mp -= 2
        loop = False
    return attacker,target,loop
def DaggerCloud(attacker,target):
    if attacker.mp < 2:
        confirm("You don't have enough MP for that.")
        loop = True
    elif attacker.knives < 5:
        confirm("You need at least 5 knives to cast this spell. You have " + str(attacker.knives) + ".")
    else:
        damage = diceroll(5,5)
        confirm("You did " + str(damage) + " damage to player " + str(target.id) + ".")
        attacker.knives -= 5
        attacker.mp -= 2
        loop = False
    return attacker,target,loop
def PoisonDart(attacker,target):
    if attacker.mp < 6:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        target.poison = diceroll(1,4)
        target.poisontr = random.randint + 1
        confirm("You did " + str(target.poison + 2) + " damage to player " + str(target.id) + ".")
        target.damage(target.poison)
        attacker.mp -= 6
        loop = False
    return attacker,target,loop
def Dispel(attacker,target):
    if attacker.mp < 5:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        target.mp = round(target.mp/2)
        confirm("You halved player " + str(target.id) + "'s MP, leaving them on " + str(target.mp) + "MP.")
        attacker.mp -= 5
        loop = False
    return attacker,target,loop
def Slow(attacker,target):
    if attacker.mp < 7:
        confirm("You don't have enough MP for that.")
        loop = True
    else:
        target.spd = round(target.spd/2)
        confirm("You halved player " + str(target.id) + "'s MP, leaving them with a speed of " + str(target.spd) + " for a turn.")
        target.slowtr = 2
        attacker.mp -= 7
        loop = False
    return attacker,target,loop

#Classes
class Player():
    num_players = 0
    def __init__(self,h,a,aB,d,m,mR,s,i,iM,p,n):
        Player.num_players += 1
        self.hp = h
        self.hpMAX = h
        self.atk = a
        self.atkBON = aB
        self.defence = d
        self.mp = m
        self.mpMAX = m
        self.mpREF = mR
        self.spd = s
        self.items = i
        self.itemMAX = iM
        self.id = p
        self.classname = str(n)
        self.alive = True
        self.dmgBON = 0
        self.defBON = 0
        self.spoons = 0
        self.knives = 0
        self.potions = 0
        self.fences = 0
        self.adv = 0
        self.adtr = 0
        self.frost = False
        self.frostr = 0
        self.poison = 0
        self.poisontr = 0
    def attack(self,target,damage):
        critnum = random_num(1,20,self.adv,print_random)
        if critnum == 20:
            q("IT'S A CRITICAL HIT!!!")
            wait()
            confirm("\nYou did " + str(damage*2) + " damage to player " + str(target.id) + "!")
            target.damage(damage*2)
        elif critnum + self.atkBON >= target.defence + target.defBON:
            confirm("You landed a hit, doing " + str(damage) + " damage to player " + str(target.id) + "!")
            target.damage(damage)
        elif critnum + self.atkBON < target.defence + target.defBON:
            confirm("You missed your attack.")
        else:
            explode()
        self.dmgBON = 0
        target.defBON = 0
    def damage(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            self.alive = False
    def heal(self,heal):
        self.hp += heal
        if self.hp > self.hpMAX:
            self.hp = self.hpMAX
    def next_turn(self):
        self.mp += self.mpREF
        if self.mp > self.mpMAX:
            self.mp = self.mpMAX
            self.adtr -= 1
        if self.adtr == 0:
            self.adv = 0
            self.frostr -= 1
        if self.frostr == 0:
            self.frost = False
        if self.poisontr > 0:
            self.damage(random.randint(0,self.poison))
            self.poisontr -= 1
        if self.slowtr > 0:
            self.spd = self.reset(self.spd)
class Knight():
    passive = "Fortitude"
    activated = "Second Wind"
    options = [
        {'number': 1, 'option': "Attack"},
        {'number': 2, 'option': "Magic"},
        {'number': 3, 'option': "Second Wind"},
        {'number': 4, 'option': "Items"},
        {'number': 5, 'option': "Pass"},
    ]
    spells = [
        {'number': 1, 'name': ""},
        {'number': 2, 'name': ""},
        {'number': 3, 'name': ""},
        {'number': 4, 'name': ""},
    ]


testing = [
    {'number': 1, 'option': "Attack"},
    {'number': 2, 'option': "Magic"},
    {'number': 3, 'option': "Second Wind"},
    {'number': 4, 'option': "Items"},
    {'number': 5, 'option': "Pass"},
]
option = int(input("Give an option. "))
#How to get 1 to change to "Attack", or 2 to "Magic" using the values of testing
option = str(testing[option])
if option == "Attack":
    print("Do this")