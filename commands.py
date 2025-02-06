import tkinter as tk
from tkinter import messagebox
import time, sys, random


def wait(t):
    time.sleep(t)
def explode(errornum):
    print("Logging error.")
    print("error num " + str(errornum))
    try:
        explode(errornum)
    except:
        explode(errornum)
def random_num(minimum,maximum,show,ad = 0):
    if ad == 1:
        num1 = random.randint(minimum,maximum)
        num2 = random.randint(minimum,maximum)
        critnumber = max(num1,num2)
    elif ad == 2:
        num1 = random.randint(minimum,maximum)
        num2 = random.randint(minimum,maximum)
        critnumber = min(num1,num2)
    else:
        critnumber = random.randint(minimum,maximum)
    if show:
        messagebox.showinfo("number_generated", "You rolled a:\n" + str(critnumber))