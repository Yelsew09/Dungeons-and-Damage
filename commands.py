import random, sys, time
from dataclasses import dataclass

@dataclass
class effectList:
    adv: int
    adtr: int
    dmgBON: int
    abilCoolCurrent: int
    abilCool: int

def q(text, newline = True, delay = .02):
    # No idea how this works, all I know is that it does
    # Rolls text instead of pasting it all at once
    if newline:
        text += "\n"
    for t in text:
        print(t, end="")
        sys.stdout.flush()
        time.sleep(delay)
def explode(errorcode):
    # A failsafe
    # If something shouldn't work, blow up the program
    print(f"Something went wrong\nErrorCode:{errorcode}\nTerminating program")
    quit()
def wait(t = .15):
    # Pure laziness. I do not want to write time.sleep(time) every pause in the program
    time.sleep(t)
def confirm(text, delay1 = .02, delay2 = .5):
    # Halts program execution until player input
    q(text, False, delay1)
    input(' >')
    time.sleep(delay2)
def ask(question, delay1 = .02, delay2 = .5):
    while True:
        try:
            q(question, False, delay1)
            option = int(input(''))
            time.sleep(delay2)
            break
        except ValueError:
            time.sleep(delay2)
            q("Please give a number.", False, delay1)
            continue
    return option
def random_num(minimum, maximum, show, ad = 0, newlineshow = True, delay1 = .02, delay2 = .5):
    # Generates a random number keeping advantage in mind
    num1 = random.randint(minimum, maximum)
    num2 = random.randint(minimum, maximum)
    if ad == 1:
        returnval = max(num1, num2)
    elif ad == 2:
        returnval = min(num1, num2)
    else:
        returnval = random.randint(minimum,maximum)
    if show:
        q(f"You rolled a {returnval}!", newlineshow, delay1)
        time.sleep(delay2)
    return returnval
def qlist(options, question, newline = True, delay1 = .02, delay2 = .5):
    while True:
        if "Back" in options:
            for i in range(len(options)):
                q(f"{i} - {options[i]}", newline, delay1)
            try:
                option = options[ask(question, delay1, delay2)]
                break
            except IndexError:
                q("Invalid option.\nPlease pick a valid number.")
                wait(delay2)
                continue
        else:
            for i in range(len(options)):
                q(f"{i+1} - {options[i]}", newline, delay1)
            try:
                option = options[ask(question, delay1, delay2) - 1]
                break
            except IndexError:
                q("Invalid option.\nPlease pick a valid number.")
                wait(delay2)
                continue
    return option
def y_or_n(asking, delay1 = .02, delay2 = .5):
    options = ["Yes", "No"]
    while True:
        option = qlist(options, asking, True, delay1, delay2)
        if option == "Yes":
            return False
        elif option == "No":
            return True
        else:
            explode("y_or_n failsafe")