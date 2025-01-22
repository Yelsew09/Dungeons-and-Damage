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

def q(str, newline = 13, temporal_distance = 0.02):

    #Not sure how this works, all I know is that it does
    #Lets the text roll instead of being printed all at once
    for char in str:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(temporal_distance)
    if not newline == 7:
        print("")
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
def ask(question, temporal_distance = .5)