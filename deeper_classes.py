import random,time,sys
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
        q("You rolled a " + str(critnumber) + "!")
        wait(.5)
        q("\n")
    return critnumber
def confirm(str, t = .5):

    #Makes sure the player has read the terms
    q(str)
    input(' >')
    wait(t)
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
    for i in range (amount):
        final_number += random.randint(1,sides)
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
        confirm("You don't have enough mp for that.")
    else:
        damage = diceroll(3,8)
        if damage < round(target.defence/2):
            confirm("The magic was too weak, and it was blocked by player " + str(target.id) + "'s armor.")
        else:
            confirm("You did " + str(damage) + " points of damage to player " + str(target.id) + ".")
            target.damage(damage)

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
        self.spoons = 0
        self.knives = 0
        self.potions = 0
        self.fences = 0
        self.adv = 0
        self.adtr = 0
    def attack(self,target,damage):
        critnum = random_num(1,20,self.adv,print_random)
        if critnum == 20:
            q("IT'S A CRITICAL HIT!!!")
            wait()
            confirm("\nYou did " + str(damage*2) + " damage to player " + str(target.id) + "!")
            target.damage(damage*2)
        elif critnum + self.atkBON >= target.defence:
            confirm("You landed a hit, doing " + str(damage) + " damage to player " + str(target.id) + "!")
            target.damage(damage)
        elif critnum + self.atkBON < target.defence:
            confirm("You missed your attack.")
        else:
            explode()
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
