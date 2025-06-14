import random
from pyray import KeyboardKey as Key
from pyray import *

if not directory_exists("textures"):
    raise FileNotFoundError("This isn't really a \"FileNotFoundError\", but the texture folder just doesn't exist. Please re-install")
if not file_exists("textures/missing.png"):
    raise FileNotFoundError("Cannot find missing.png; this is needed to detect rendering errors\nI wish I could just add it, but I can't")


class Hitbox():
    def __init__(self,x,y,w,l,t = None):
        self.spot = Vector2(x,y)
        self.dimensions = Vector2(w,l)
        self.tag = t
    def check_collision(self,current_position):

class Player():
    def __init__(self,texture_folder,stats,collision_box):
        self.stats = stats
        self.textures = f"textures/player/{texture_folder}"
        self.collision_box = Hitbox([16,16],self.position)
    def draw(self,position,rotation,scale,texture_name,tint = WHITE):
        texture = f"{self.textures}/{texture_name}"
        if file_exists(texture):
            texture = load_texture(texture)
        else:
            texture = load_texture("textures/missing.png")
        draw_texture_ex(texture,position,rotation,scale,tint)
        unload_texture(texture)
    def next_frame(self):
        if is_key_down(Key.KEY_W):
            self.collision_box.


class Tile():
    """
    Extra details is a list looking like:
    [
        int layer
        bool border above
        bool border right
        bool border below
        bool border right
    ]
    """
    def __init__(self,t,m,z,e = [1,False,False,False,False]):
        self.texture_path = f"textures/tiles/{t}"
        self.map_position = Vector2(m[0],m[1])
        self.zone = z
        self.extras = e
    def draw(self,position,scale = 1,rotation = 0,tint = WHITE):
        if self.extras[1]:
            self.above = Hitbox(position[0],position[1]+15,16,1)
        if self.extras[2]:
            self.right = Hitbox(position[0]+15,position,1,16)
        if self.extras[3]:
            self.below = Hitbox(position[0],position[1],16,1)
        if self.extras[4]:
            self.left = Hitbox(position[0],position[1],1,16)
        draw_texture_ex(self.texture,position,rotation,grass.scale,tint)
    def load(self):
        if file_exists(self.texture_path):
            self.texture = load_texture(self.texture_path)
            grass.scale = 2
        else:
            self.texture = load_texture("textures/missing.png")
            grass.scale = 16



grass = Tile("grass.png",[0,0],"overworld")
init_window(640,360,"test")
set_target_fps(60)
grass.load()
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    grass.draw(grass.map_position)
    end_drawing()
close_window()