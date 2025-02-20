import tkinter as tk
import random
import commands as cm

def guide():
    btnTwo.config(text = "Guide coming soon")
def options():
    btnThree.config(text = "Option menu coming soon")
def quit():
    root.destroy()
def game_start():
    btnOne.grid_forget()
    btnTwo.grid_forget()
    btnThree.grid_forget()
    btnFour.grid_forget()
    def charselect(player):
        global option
        classes = [
            "Knight"
            "Peashooter"
            "Rouge"
            "Mage"
            "Skele"
            "Bard"
            "Barbarian"
            "Random"
        ]
        option = tk.StringVar()
        option.set("Select a class")
        classelect = tk.OptionMenu(root, option, *classes)
        def lockclass():
            global option
            option = classelect.get()
            rc = True
            while rc:
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
                    rc = False
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
                    rc = False
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
                    rc = False
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
                    rc = False
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
                    rc = False
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
                    rc = False
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
                    rc = False
                elif option == "Random":
                    option = random.choice("Knight", "Peashooter", "Rouge", "Mage", "Skele", "Bard", "Barbarian")

            
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