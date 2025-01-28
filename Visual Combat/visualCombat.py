import tkinter as tk
import time, random, sys

def wait(temporal_distance = .15):
    time.sleep(temporal_distance)
def q(str):
    lblText.config(text = str)
def next_text():
    lblText.config(text = "")
def combat():
    q("Combat")


root = tk.Tk()
visual = tk.Canvas(root, width = "640", height = "480")
root.title("nondescript_rpg")
root.geometry("1280x720")
root.maxsize(1920,1080)
root.minsize(640,480)



#Labels
lblText = tk.Label(root, text = "")

#Buttons
btnCont = tk.Button(root, text = "==>", command = next_text)
btnOne = tk.Button(root, text = "Game Start", command = combat)

#Text Entries


##GRID##


root.mainloop()