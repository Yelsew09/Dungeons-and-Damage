import random
from pyray import KeyboardKey as Key
from pyray import *
from classes import *

if not directory_exists("textures"):
    raise FileNotFoundError("This isn't really a \"FileNotFoundError\", but the texture folder just doesn't exist. Please re-install")
if not file_exists("textures/missing.png"):
    raise FileNotFoundError("Cannot find missing.png; this is needed to detect rendering errors\nI wish I could just add it, but I can't")





init_window(320,180,"test")
set_target_fps(60)
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    end_drawing()
close_window()