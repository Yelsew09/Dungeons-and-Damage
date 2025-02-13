import tkinter as tk
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
        ]
        option = tk.StringVar()
        option.set("Select a class")
        classelect = tk.OptionMenu(root, option, *classes)
        def lockclass():
            global option
            option = classelect.get()
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