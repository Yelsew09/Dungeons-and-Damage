import random,time,sys
print_random = True

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

class Player():
    num_players = 0
    def __init__(self,h,a,aB,d,m,mR,s,i,iM,p,n):
        Player.num_players += 1
        self.hp = h
        self.atk = a
        self.atkBON = aB
        self.defence = d
        self.mp = m
        self.mpREF = mR
        self.spd = s
        self.items = i
        self.itemMAX = iM
        self.id = p
        self.classname = str(n)
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
        target.damage(damage)