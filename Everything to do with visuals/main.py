import random
from pyray import *
from raylib import *
global control_scheme,last_clicked,fpsCounter
last_clicked = None
fpsCounter = True
with open("Everything to do with visuals/settings.txt","rt") as options:
    control_scheme = str(options.readline())
    UP = options.readline()
    LEFT = options.readline()
    DOWN = options.readline()
    RIGHT = options.readline()
    A = options.readline()
    B = options.readline()
    L = options.readline()
    R = options.readline()
    START = options.readline()
    SELECT = options.readline()
import UI_Elements as UI