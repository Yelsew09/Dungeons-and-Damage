from pyray import KeyboardKey as Key
from pyray import *


class Hitbox():
    boxes = []
    def __init__(self,p,s,e):
        self.position = p
        self.size = s
        self.extras = e
        self.rectangle = Rectangle(self.position.x,self.position.y,self.size.x,self.size.y)
        Hitbox.boxes.append(self)
    def next_frame(self,p,s):
        self.position = p
        self.size = s
        self.rectangle = Rectangle(self.position.x,self.position.y,self.size.x,self.size.y)
    def check_collision(self,other_box):
        if check_collision_recs(self.rectangle,other_box.rectangle):
            return self
        else:
            return Hitbox(Vector2(0,0),Vector2(0,0),None)
    def delete(self):
        del self
        Hitbox.boxes.remove(self)

class Player():
    def __init__(self,tf,h,s = {},p = Vector2(0,0)):
        self.texture_folder = f"textures/{tf}"
        self.hitbox = h
        self.stats = s
        self.position = p
    def next_frame(self):
        move_x = 0
        move_y = 0
        if is_key_down(Key.KEY_W):
            self.position.y += 1
            move_y = 1
        elif is_key_down(Key.KEY_S):
            self.position.y -= 1
            move_y = -1
        if is_key_down(Key.KEY_D):
            self.position.x += 1
            move_x = 1
        elif is_key_down(Key.KEY_A):
            self.position.x -= 1
            move_x = -1
        for box in Hitbox.boxes:
            collision = box.check_collision(self.hitbox)
            if not collision.extras == None:
                self.position.x -= move_x
                self.position.y -= move_y
    def draw(self,texture,rotation = 0.0,scale = 1,tint = WHITE):
        if file_exists(f"{self.texture_folder}/{texture}"):
            texture = load_texture(f"{self.texture_folder}/{texture}.png")
        else:
            texture = load_texture("textures/missing.png")
            scale = scale*16
        draw_texture_ex(texture,self.position,rotation,scale,tint)
        unload_texture(texture)

class Tile():
    def __init__(self,p,t,h,e):
        self.position = p
        self.texture = f"textures/tiles/{t}"
        self.hitboxes = []
        self.extras = e
        if h[0]:
            self.hitbox = Hitbox(self.position,Vector2(32,32),e)
            self.hitboxes.append(self.hitbox)
        else:
            if h[1]:
                self.topbox = Hitbox(Vector2(self.position.x,self.position.y+32),Vector2(32,1),e)
                self.hitboxes.append(self.topbox)
            if h[2]:
                self.rightbox = Hitbox(Vector2(self.position.x+32,self.position.y),Vector2(1,32),e)
                self.hitboxes.append(self.rightbox)
            if h[3]:
                self.downbox = Hitbox(Vector2(self.position.x,self.position.y),Vector2(32,1),e)
                self.hitboxes.append(self.downbox)
            if h[4]:
                self.leftbox = Hitbox(Vector2(self.position.x,self.position.y),Vector2(1,32),e)
                self.hitboxes.append(self.leftbox)
    def next_frame(self):
        for hitbox in self.hitboxes:
            hitbox.next_frame(self.position,hitbox.size)
    def draw(self,position,rotation = 0.0,scale = 1,tint = WHITE):
        if file_exists(texture):
            texture = load_texture(f"{self.texture}.png")
        else:
            texture = load_texture("textures/missing.png")
            scale = scale*16
        draw_texture_ex(texture,position,rotation,scale,tint)
        unload_texture(texture)
    def delete(self):
        for hitbox in self.hitboxes:
            hitbox.delete()

class Zone():
    def __init__(self,de,di,e):
        self.dimensions = di
        self.details = de
        self.extras = e
    def next_frame(self,camera):
        for tile in self.details:
            if check_collision_recs(Rectangle(tile.position.x,tile.position.y,32,32),camera.view_area):
                tile.next_frame()
                tile.draw(get_world_to_screen_2d(tile.position,camera))