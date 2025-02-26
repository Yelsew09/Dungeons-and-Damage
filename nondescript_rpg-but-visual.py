import tkinter as tk
from tkinter import messagebox
import time, sys, random

def q(label, text, t = .02):
    string = ''
    for i in range(len(text)):
        add = text[i]
        string = string + add
        label.config(text = string)
        time.sleep(t)

P1HP = 0
P1MAXHP = 0
P1ATK = 0
P1ATKBON = 0
P1DEF = 0
P1MP = 0
P1MAXMP = 0
P1MPBON = 0
P1SPD = 0
P2HP = 0
P2MAXHP = 0
P2ATK = 0
P2ATKBON = 0
P2DEF = 0
P2MP = 0
P2MAXMP = 0
P2MPBON = 0
P2SPD = 0

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

def guide():
    btnTwo.config(text = "Guide coming soon")
def options():
    btnThree.config(text = "Option menu coming soon")
def quit():
    root.destroy()
def game_start():

    #GETS RID OF OLD BUTTONS#
    btnOne.grid_forget()
    btnTwo.grid_forget()
    btnThree.grid_forget()
    btnFour.grid_forget()
    btnConfirm.grid_forget()
    #########################

    #SHOWS THAT THERE ARE STATS TO BE DIPLAYED LATER#
    lblInfo1 = tk.Label(root, text = "HP: -/-")
    lblInfo2 = tk.Label(root, text = "Attack Damage: -")
    lblInfo3 = tk.Label(root, text = "Attack Roll Bonus: -")
    lblInfo4 = tk.Label(root, text = "Defence: -")
    lblInfo5 = tk.Label(root, text = "MP: -/-. Refresh: -")
    lblInfo6 = tk.Label(root, text = "Speed = -")
    ##################################################
    
    #SETTING UP CHARACTER SELECT DROPDOWN MENU#
    classes = [
        "Knight"
        "Peashooter"
        "Rouge"
        "Mage"
        "Skele"
        "Bard"
        "Barbarian"
    ]
    selected_class = tk.StringVar()
    selected_class.set("Please select a class")
    optClassSelect = tk.OptionMenu(root, selected_class, *classes)
    ###########################################

    #Updates tags to show stats, and shows new button
    def view_class(player):
        option = selected_class.get()
        if option == "Knight":
            HP = 5
        elif option == "Peashooter":
            HP = 4
        elif option == "Rouge":
            HP = 3
        elif option == "Mage":
            HP = 4
        elif option == "Skele":
            HP = 3
        elif option == "Bard":
            HP = 4
        elif option == "Barbarian":
            HP = 6
        else:
            btnClassSelect.config(text = "Please select a class")
    
    #NEW BUTTONS#
    btnClassSelect = tk.Button(root, text = "View Class", command = view_class)
    btnConfirm = tk.Button(root, text = "Confirm Class", command = confirm_class)
    #############


root = tk.Tk()
root.geometry("1280x720")
root.title("dungeons_and_damage")
root.resizable(False,False)

btnOne = tk.Button(root, text = "Game start", command = game_start)
btnTwo = tk.Button(root, text = "Guide")
btnThree = tk.Button(root, text = "Options")
btnFour = tk.Button(root, text = "Quit")


btnOne.grid(row = 0, column = 0)
btnTwo.grid(row = 1, column = 0)
btnThree.grid(row = 2, column = 0)
btnFour.grid(row = 3, column = 0)

root.mainloop()