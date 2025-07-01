import random
from pyray import KeyboardKey as Key
from pyray import *
import classes

if not directory_exists("textures"):
    raise FileNotFoundError("This isn't really a \"FileNotFoundError\", but the texture folder just doesn't exist. Please re-install")
if not file_exists("textures/missing.png"):
    raise FileNotFoundError("Cannot find missing.png; this is needed to detect rendering errors\nI wish I could just add it, but I can't")

player = classes.Player({},"temporary_player",{})

main_camera = Camera2D()
main_camera.target = player.position
main_camera.offset = player.position

init_window(320,180,"test")
toggle_borderless_windowed()
set_target_fps(60)
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_fps(10,10)
    end_drawing()
close_window()