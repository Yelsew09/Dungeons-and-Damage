import tkinter as tk
import references as ref

classes = [
    "Knight",
    "Peashooter",
    "Rouge",
    "Mage",
    "Skele",
    "Bard",
    "Barbarian"
]
spells = [
    "Fireball - 5MP",
    "Summon Random Item - 2MP",
    "Gain Advantage - 3MP",
    "Impose Disadvantage - 4MP",
    "Heal 20% - 5MP",
    "Damage Boost - Varies"
]
global player
player = 1

def setup_window(window):
    print("Buch of if commands. Sets up windows when needed")
def option_menu():
    lblInfo1.config(text = "Options coming soon")
def guide():
    lblInfo1.config(text = "Guide coming soon")
def quit_game():
    root.destroy()
def game_start():

    #New stuff for window
    lblTitle.config(root, text = "Player " + str(player) + ", please select a class", font = ("Arial", 14))
    lblInfo1 = tk.Label(root, text = "HP: -/-")
    lblInfo2 = tk.Label(root, text = "Attack Damage: -")
    lblInfo3 = tk.Label(root, text = "Attack Roll Bonus: -")
    lblInfo4 = tk.Label(root, text = "Defence: -")
    lblInfo5 = tk.Label(root, text = "MP: -/-. Refresh: -")
    lblInfo6 = tk.Label(root, text = "Speed -")
    btnVeiwClass = tk.Button(root, text = "View Class", command = view_class)
    btnConfirm = tk.Button(root, text = "Confirm Class", command = lambda: btnConfirm.config(text = ""))
    #Dropdown menu for class select
    selected_class = tk.StringVar()
    selected_class.set("Select a class")
    optClassSelect = tk.OptionMenu(root, selected_class, *classes)
    def view_class():
        
        option = selected_class.get()
        if player == 1:
            if option == "Knight":
                P1 = ref.Stat(35,7,5,16,5,3,2)
            elif option == "Peashooter":
                P1 = ref.Stat(26,9,4,14,7,3,5)
            elif option == "Rouge":
                P1 = ref.Stat(20,10,6,13,6,2,7)
            elif option == "Mage":
                P1 = ref.Stat(20,5,2,11,10,5,4)
            elif option == "Skele":
                P1 = ref.Stat(30,7,3,12,7,5,6)
            elif option == "Bard":
                P1 = ref.Stat(27,6,4,14,4,2,3)
            elif option == "Barbarian":
                P1 = ref.Stat(40,12,2,15,2,1,1)
            lblInfo1.config(text = "HP: " + str(P1.hp) + "/" + str(P1.maxhp))
            lblInfo2.config(text = "Attack Damage: " + str(P1.atk))
            lblInfo3.config(text = "Attack Roll Bonus: " + str(P1.atk_bon))
            lblInfo4.config(text = "Defence: " + str(P1.defence))
            lblInfo5.config(text = "MP: " + str(P1.mp) + "/" + str(P1.maxmp) + ". Refresh: " + str(P1.mpbon))
            lblInfo6.config(text = "Speed: " + str(P1.speed))
        elif player == 2:
            if option == "Knight":
                P2 = ref.Stat(35,7,5,16,5,3,2)
            elif option == "Peashooter":
                P2 = ref.Stat(26,9,4,14,7,3,5)
            elif option == "Rouge":
                P2 = ref.Stat(20,10,6,13,6,2,7)
            elif option == "Mage":
                P2 = ref.Stat(20,5,2,11,10,5,4)
            elif option == "Skele":
                P2 = ref.Stat(30,7,3,12,7,5,6)
            elif option == "Bard":
                P2 = ref.Stat(27,6,4,14,4,2,3)
            elif option == "Barbarian":
                P2 = ref.Stat(40,12,2,15,2,1,1)
            lblInfo1.config(text = "HP: " + str(P2.hp) + "/" + str(P2.maxhp))
            lblInfo2.config(text = "Attack Damage: " + str(P2.atk))
            lblInfo3.config(text = "Attack Roll Bonus: " + str(P2.atk_bon))
            lblInfo4.config(text = "Defence: " + str(P2.defence))
            lblInfo5.config(text = "MP: " + str(P2.mp) + "/" + str(P2.maxmp) + ". Refresh: " + str(P2.mpbon))
            lblInfo6.config(text = "Speed: " + str(P2.speed))


#Window Details
root = tk.Tk()
root.geometry("1280x720")
root.title("dungeons_and_damage")
root.resizable(False,False)

#Window Elements
lblTitle = tk.Label(root, text = "Dungeons and Damage", font = ("Arial", 16))
lblInfo1 = tk.Label(root, text = "Further information will be displayed here")
btnOptions = tk.Button(root, text = "Options", command = option_menu)
btnGuide = tk.Button(root, text = "Guide", command = guide)
btnQuit = tk.Button(root, text = "Quit", command = quit_game)
btnStart = tk.Button(root, text = "Game Start", command = game_start)

#Placing things in window
lblTitle.grid(row = 0, column = 0)
btnStart.grid(row = 1, column = 0)
btnGuide.grid(row = 2, column = 0)
btnOptions.grid(row = 3, column = 0)
btnQuit.grid(row = 4, column = 0)
lblInfo1.grid(row = 5, column = 0)

root.mainloop()