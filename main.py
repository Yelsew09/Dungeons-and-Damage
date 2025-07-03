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
main_camera.target = Vector2(0,0)
#main_camera.offset = Vector2(get_screen_width()/2,get_screen_height()/2)

window_width = 640
window_height = 360
collumns = 20
rows = 11
init_window(window_width,window_height,"test")
#toggle_borderless_windowed()
global global_scale
hide_cursor()
set_target_fps(get_monitor_refresh_rate(get_current_monitor()))
tile = load_texture("textures/missing.png")
begin_mode_2d(main_camera)

overworld = Zone([])
for i in range(11):
    for j in range(20):
        overworld.tiles.append(Tile(Vector2(j*32,i*32),"grass.png",[False,False,False,False,False]))
overworld.load()
while not window_should_close():
    global_scale = (get_screen_width()/window_width) * 2
    begin_drawing()
    clear_background(BLACK)
    overworld.next_frame(main_camera)
    draw_texture_ex(tile,get_mouse_position(),0.0,8*global_scale,WHITE)
    draw_rectangle(7,9,78,20,WHITE)
    draw_fps(10,10)
    end_drawing()
end_mode_2d()
overworld.unload()
unload_texture(tile)
close_window()