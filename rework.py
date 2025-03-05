import tkinter as tk
import references as ref
import random

#Setting up variables
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

#Setting up stuff
root = tk.Tk()
root.geometry("1280x720")
root.title("dungeons_and_damage")
root.resizable(False,False)

#Starts the game
def class_select():
    
    #Updating screen
    lblTitle.config("Player " + str(player) + ", please select a class")
    lblGeneral.grid_forget()
    btnStart.grid_forget()
    btnGuide.grid_forget()
    btnOptions.grid_forget()
    btnQuit.grid_forget()
    #########

    #Everything that isn't a button
    lblInfo1 = tk.Label(root, text = "HP: -/-")
    lblInfo2 = tk.Label(root, text = "Attack Damage: -")
    lblInfo3 = tk.Label(root, text = "Attack Roll Bonus: -")
    lblInfo4 = tk.Label(root, text = "Defence: -")
    lblInfo5 = tk.Label(root, text = "MP: -/-. Refresh: -")
    lblInfo6 = tk.Label(root, text = "Speed: -")
    #Dropdown
    selected_class = tk.StringVar()
    optClassSelect = tk.OptionMenu(root, selected_class, *classes)
    ###########

    #New commands
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
    def confirm_class():
        if player == 2:
            def game_start():

                #Clearing screen
                lblInfo1.grid_forget()
                lblInfo2.grid_forget()
                lblInfo3.grid_forget()
                lblInfo4.grid_forget()
                lblInfo5.grid_forget()
                lblInfo6.grid_forget()
                #########
            
            game_start()
        else:
            player = player + 1
    def random_class():
        selected_class.set(random.choice(classes))
        view_class()

    #Defining Buttons
    btnViewClass = tk.Button(root, text = "Show Class", command = view_class)
    btnConfirmClass = tk.Button(root, text = "Confirm Class", command = confirm_class)
    btnRandomClass = tk.Button(root, text = "Random Class", command = random_class)
    #########

    #Placing thing in window
    
    ########


#Defining things for main menu
lblTitle = tk.Label(root, text = "Dungeons and Damage", font = ("Arial", 16))
lblGeneral = tk.Label(root, text = "Further info here")
btnStart = tk.Button(root, text = "Game Start", command = class_select, font = ("Arial", 14))
btnGuide = tk.Button(root, text = "Guide", command = lambda: lblGeneral.config(text = "Guide coming soon"), font = ("Arial", 12))
btnOptions = tk.Button(root, text = "Options", command = lambda: lblGeneral.config(text = "Options coming soon"), font = ("Arial", 12))
btnQuit = tk.Button(root, text = "Quit", command = lambda: root.destroy(), font = ("Arial", 12))
#Placing things in main menu
lblTitle.grid(row = 0, column = 0)
btnStart.grid(row = 1, column = 0)
btnGuide.grid(row = 2, column = 0)
btnOptions.grid(row = 3, column = 0)
btnQuit.grid(row = 4, column = 0)
lblGeneral.grid(row = 5, column = 0)
#########

root.mainloop()