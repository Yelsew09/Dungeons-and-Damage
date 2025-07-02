import random
from pyray import KeyboardKey as Key
from pyray import *
from classes import *

if not directory_exists("textures"):
    raise FileNotFoundError("This isn't really a \"FileNotFoundError\", but the texture folder just doesn't exist. Please re-install")
if not file_exists("textures/missing.png"):
    raise FileNotFoundError("Cannot find missing.png; this is needed to detect rendering errors\nI wish I could just add it, but I can't")

player = Player({},"temporary_player",{})

main_camera = Camera2D()
main_camera.target = player.position
main_camera.offset = Vector2(get_screen_width()/2,get_screen_height()/2)

init_window(320,180,"test")
toggle_borderless_windowed()
global global_scale
global_scale = get_screen_width()/45
hide_cursor()
print(get_screen_width())
set_target_fps(get_monitor_refresh_rate(get_current_monitor()))
tile = load_texture("textures/missing.png")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_fps(10,10)
    draw_texture_ex(tile,get_mouse_position(),0.0,8*global_scale,WHITE)
    end_drawing()
unload_texture(tile)
close_window()