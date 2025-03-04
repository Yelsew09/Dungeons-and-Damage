import tkinter as tk
from tkinter import messagebox
import time, random

def q(label, text, t = .02):
    string = ''
    for i in range(len(text)):
        add = text[i]
        string = string + add
        label.config(text = string)
        time.sleep(t)
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

#Here to make stuff collapseable
for i in range (1):
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

def guide():
    btnTwo.config(text = "Guide coming soon")
def options():
    btnThree.config(text = "Option menu coming soon")
def quit():
    root.destroy()
def game_start():

    #VARIABLE STUFF#
    global player
    player = 1
    ################

    #GETS RID OF OLD BUTTONS#
    btnOne.grid_forget()
    btnTwo.grid_forget()
    btnThree.grid_forget()
    btnFour.grid_forget()
    #########################

    #SHOWS THAT THERE ARE STATS TO BE DIPLAYED LATER#
    lblTitle = tk.Label(root, text = "Player " + str(player) + ", please select a class", font = ("Arial", 14))
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
    selected_class.set("Select a class")
    optClassSelect = tk.OptionMenu(root, selected_class, *classes)
    ###########################################

    #GAME START BECAUSE ORDERING IS BAD#
    def game_start():
        optClassSelect.grid_forget()
        btnConfirm.grid_forget()
        btnClassSelect.grid_forget()
        btnRandom.grid_forget()
        lblTitle.grid_forget()
        lblInfo1.grid_forget()
        lblInfo2.grid_forget()
        lblInfo3.grid_forget()
        lblInfo4.grid_forget()
        lblInfo5.grid_forget()
        lblInfo6.grid_forget()
        def attack(atkATK,atkATK_BON,atkDMG_BOOST,atkAD,defDEF,defHP,defFENCE_SET,defP):
            critnumber = random_num(1,20,atkAD)
            if defFENCE_SET:
                q(lblInfo1, "You stuck player " + str(defP) + "'s fence.")
            elif not defFENCE_SET:
                if critnumber == 20:
                    damage = atkATK*2 + atkDMG_BOOST
                    defHP = defHP - damage
                    q(lblInfo1, "You did " + str(damage) + " damage to player " + str(defP))
                elif critnumber + atkATK_BON > defDEF:
                    damage = atkATK + atkDMG_BOOST
                    defHP = defHP - damage
                    q(lblInfo1, "You did " + str(damage) + " damage to player " + str(defP))
                elif critnumber + atkATK_BON < defDEF:
                    q(lblInfo1, "You missed your attack")
                else:
                    explode(1)
            else:
                explode(1)
            atkATK_BON = 0
        def magic(atkMP,atkMAX_MP,defDEF,defFENCE_SET,defP):
            def FIREBALL(mp,max_mp,fence_set,defP):
                print("FIREBALL")
            def random_item(mp,spoons,knives,potions,fences):
                print("Random item")
            def advantage_spell(mp,ad,adtr):
                print("Gain advantage")
            def disadvantage_spell(mp,defAD,defADTR):
                print("Impose disadvantage")
            def heal(mp,hp,max_hp):
                print("Heal 20%")
            def damage_boost(mp):
                print("Damage boost")
            
            spells = [
                "Fireball - 5MP",
                "Summon Random Item - 2MP",
                "Gain Advantage - 3MP",
                "Impose Disadvantage - 4MP",
                "Heal 20% - 5MP",
                "Damage Boost - Varies"
            ]
            selected_spell = tk.StringVar()
            selected_spell.set("Select a spell")
            optSpellSelect = tk.OptionMenu(root, selected_spell, *spells)

            def spell_select():
                option = selected_spell.get()
                if option == "Fireball - 5MP":
                    print("Do a fireball")
                elif option == "Summon Random Item - 2MP":
                    print("Summon a random item")
                elif option == "Gain Advantage - 3MP":
                    print("Give user advantage")
                elif option == "Impose Disadvantage - 4MP":
                    print("Give defending player disadvantage")
                elif option == "Heal 20% - 5MP":
                    print("Heal user by 20 percent of their max_hp")
                elif option == "Damage Boost - Varies":
                    print("Do damage boost shenanagains")
                else:
                    q(lblInfo1, "Please select a spell.")
    ####################################

    #CLASS SELECT COMMANDS#
    #Updates tags to show stats
    def view_class(option = 0):
        global HP, MAXHP, ATK, ATKBON, DEF, MP, MAXMP, MPBON, SPD
        HP = 0
        if option == 0:
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
            SPD = 2
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
            SPD = 3
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
        if player == 2:
            print("Update screen to start")
            game_start()
        else:
            player = player + 1
            lblTitle.config(text = "Player " + str(player) + ", please select a class.")
    def random_class():
        clas = random.choice(classes)
        view_class(clas)
        selected_class.set(clas)

    #NEW BUTTONS#
    btnClassSelect = tk.Button(root, text = "View Class", command = view_class)
    btnConfirm = tk.Button(root, text = "Confirm Class", command = confirm_class)
    btnRandom = tk.Button(root, text = "Random Class", command = random_class)
    #############

    #PUTTING THINGS IN THE WINDOW#
    optClassSelect.grid(row = 1, column = 0, columnspan = 2)
    btnConfirm.grid(row = 3, column = 0)
    btnClassSelect.grid(row = 2, column = 0)
    btnRandom.grid(row = 2, column = 1)
    lblTitle.grid(row = 0, column = 0, columnspan = 3)
    lblInfo1.grid(row = 1, column = 2)
    lblInfo2.grid(row = 2, column = 2)
    lblInfo3.grid(row = 3, column = 2)
    lblInfo4.grid(row = 4, column = 2)
    lblInfo5.grid(row = 5, column = 2)
    lblInfo6.grid(row = 6, column = 2)
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