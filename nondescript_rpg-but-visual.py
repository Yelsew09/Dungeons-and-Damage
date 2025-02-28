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

    #VARIABLE STUFF#
    player = 1
    ################

    #GETS RID OF OLD BUTTONS#
    btnOne.grid_forget()
    btnTwo.grid_forget()
    btnThree.grid_forget()
    btnFour.grid_forget()
    #########################

    #SHOWS THAT THERE ARE STATS TO BE DIPLAYED LATER#
    lblInfo1 = tk.Label(root, text = "HP: -/-")
    lblInfo2 = tk.Label(root, text = "Attack Damage: -")
    lblInfo3 = tk.Label(root, text = "Attack Roll Bonus: -")
    lblInfo4 = tk.Label(root, text = "Defence: -")
    lblInfo5 = tk.Label(root, text = "MP: -/-. Refresh: -")
    lblInfo6 = tk.Label(root, text = "Speed: -")
    ##################################################
    
    #SETTING UP CHARACTER SELECT DROPDOWN MENU#
    classes = [
        "Knight",
        "Peashooter",
        "Rouge",
        "Mage",
        "Skele",
        "Bard",
        "Barbarian"
    ]
    selected_class = tk.StringVar()
    selected_class.set("Please select a class")
    optClassSelect = tk.OptionMenu(root, selected_class, *classes)
    ###########################################

    #Updates tags to show stats
    def view_class():
        global HP, MAXHP, ATK, ATKBON, DEF, MP, MAXMP, MPBON, SPD
        HP = 0
        option = selected_class.get()

        #SETS VARIABLES TO CORRECT VALUES FOR USAGE LATER#
        if option == "Knight":
            HP = 35
            MAXHP = HP
            ATK = 7
            ATKBON = 5
            DEF = 16
            MP = 5
            MAXMP = MP
            MPBON = 3
            SPD = 3
            btnConfirm.grid()
        elif option == "Peashooter":
            HP = 26
            MAXHP = HP
            ATK = 9
            ATKBON = 4
            DEF = 14
            MP = 7
            MAXMP = MP
            MPBON = 3
            SPD = 5
        elif option == "Rouge":
            HP = 20
            MAXHP = HP
            ATK = 10
            ATKBON = 6
            DEF = 13
            MP = 6
            MAXMP = MP
            MPBON = 2
            SPD = 7
        elif option == "Mage":
            HP = 21
            MAXHP = HP
            ATK = 5
            ATKBON = 2
            DEF = 11
            MP = 10
            MAXMP = MP
            MPBON = 5
            SPD = 4
        elif option == "Skele":
            HP = 30
            MAXHP = HP
            ATK = 7
            ATKBON = 3
            DEF = 12
            MP = 7
            MAXMP = MP
            MPBON = 5
            SPD = 6
        elif option == "Bard":
            HP = 27
            MAXHP = HP
            ATK = 6
            ATKBON = 4
            DEF = 14
            MP = 4
            MAXMP = MP
            MPBON = 2
            SPD = 2
        elif option == "Barbarian":
            HP = 40
            MAXHP = HP
            ATK = 12
            ATKBON = 2
            DEF = 15
            MP = 2
            MAXMP = MP
            MPBON = 1
            SPD = 1
        elif option == "Random":
            option = random.choice(classes)
        ##################################################

        if not HP == 0:
            #UPDATES LABELS TO DISPLAY PROPER INFORMATION#
            lblInfo1.config(text = "HP: " + str(HP) + "/" + str(MAXHP))
            lblInfo2.config(text = "Attack Damage: " + str(ATK))
            lblInfo3.config(text = "Attack Roll Bonus: " + str(ATKBON))
            lblInfo4.config(text = "Defence: " + str(DEF))
            lblInfo5.config(text = "MP: " + str(MP) + "/" + str(MAXMP) + ". Refresh: " + str(MPBON))
            lblInfo6.config(text = "SPEED: " + str(SPD))
            ##############################################
            print("Need this here to have colapse work")
    def confirm_class():
        global P1HP, P1MAXHP, P1ATK, P1ATKBON, P1DEF, P1MP, P1MAXMP, P1MPBON, P1SPD, P2HP, P2MAXHP, P2ATK, P2ATKBON, P2DEF, P2MP, P2MAXMP, P2MPBON, P2SPD, player
        if player == 1:
            P1HP = HP
            P1MAXHP = HP
            P1ATK = ATK
            P1ATKBON = ATKBON
            P1DEF = DEF
            P1MP = MP
            P1MAXMP = MP
            P1MPBON = MPBON
            P1SPD = SPD
        elif player == 2:
            P2HP = HP
            P2MAXHP = HP
            P2ATK = ATK
            P2ATKBON = ATKBON
            P2DEF = DEF
            P2MP = MP
            P2MAXMP = MP
            P2MPBON = MPBON
            P2SPD = SPD
        player = player + 1


    #NEW BUTTONS#
    btnClassSelect = tk.Button(root, text = "View Class", command = view_class)
    btnConfirm = tk.Button(root, text = "Confirm Class", command = confirm_class)
    btnRandom = tk.Button(root, text = "Random Class", command = view_class)
    #############

    #PUTTING THINGS IN THE WINDOW#
    optClassSelect.grid(row = 0, column = 0, columnspan = 2)
    btnConfirm.grid(row = 2, column = 0)
    btnClassSelect.grid(row = 1, column = 0)
    btnRandom.grid(row = 1, column = 1)
    lblInfo1.grid(row = 0, column = 2)
    lblInfo2.grid(row = 1, column = 2)
    lblInfo3.grid(row = 2, column = 2)
    lblInfo4.grid(row = 3, column = 2)
    lblInfo5.grid(row = 4, column = 2)
    lblInfo6.grid(row = 5, column = 2)
    ##############################
    print("Need this here to get colapse to work")

#WINDOW STUFF#
root = tk.Tk()
root.geometry("1280x720")
root.title("dungeons_and_damage")
root.resizable(False,False)
##############

#MAIN MENU#
btnOne = tk.Button(root, text = "Game start", command = game_start)
btnTwo = tk.Button(root, text = "Guide")
btnThree = tk.Button(root, text = "Options")
btnFour = tk.Button(root, text = "Quit")

btnOne.grid(row = 0, column = 0)
btnTwo.grid(row = 1, column = 0)
btnThree.grid(row = 2, column = 0)
btnFour.grid(row = 3, column = 0)
###########

root.mainloop()