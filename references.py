import random, time
import tkinter as tk
from tkinter import messagebox

def q(label, text, starting = "", t = .02):
    string = str(starting)
    for i in range(len(text)):
        add = text[i]
        string = string + add
        label.config(text = string)
        time.sleep(t)
def wait(t = .15):
    time.sleep(t)
def random_num(minimum,maximum,show,advantage = 0):
    if advantage == 1:
        num1 = random.randint(minimum,maximum)
        num2 = random.randint(minimum,maximum)
        critnumber = max(num1,num2)
    elif advantage == 2:
        num1 = random.randint(minimum,maximum)
        num2 = random.randint(minimum,maximum)
        critnumber = min(num1,num2)
    else:
        critnumber = random.randint(minimum,maximum)
    if show:
        messagebox.showinfo("You rolled a " + str(critnumber))
    return critnumber

class Stat:
    def __init__(self, hp, atk, atk_bon, defence, mp, mpbon, spd):
        self.hp = hp
        self.maxhp = hp
        self.atk = atk
        self.atk_bon = atk_bon
        self.defence = defence
        self.mp = mp
        self.maxmp = mp
        self.mpbon = mpbon
        self.speed = spd
    
    def damage(self,damage):
        self.hp = self.hp - damage
    
    def heal(self,heal):
        self.hp = self.hp + heal
        if self.hp > self.maxhp:
            self.hp = self.maxhp
