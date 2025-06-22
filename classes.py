from pyray import KeyboardKey as Key
from pyray import *

class Hitbox():
    hitboxes = []
    def __init__(self,x,y,l,w,t = None,e = None):
        self.location = Vector2(x,y)
        self.dimensions = Vector2(l,w)
        self.tags = t
        self.extras = e
        Hitbox.hitboxes.append(self)
    def check_collision(self,tags,layer):
        valid_hitboxes = []
        for hitbox in Hitbox.hitboxes:
            if tags in hitbox.extras and hitbox.extras['layer'] == layer:
                valid_hitboxes.append(hitbox)
        for box in valid_hitboxes:
            colliding = check_collision_recs(Rectangle(self.location.x,self.location.y,self.dimensions.x,self.dimensions.y),
                                 Rectangle(box.location.x,box.location.y,box.dimensions.x,box.dimensions.y))
            if colliding:
                return box
        return False
    def update_position(self,new_position):
        self.location = new_position
    def delete(self):
        Hitbox.hitboxes.remove(self)
        del self

class Tile():
    def __init__(self,x,y,t,e):
        self.location = Vector2(x,y)
        self.t = t
        self.texture = load_texture(f"textures/tiles/{self.t}")
        self.extras = e
    def next_frame(self,current_location,draw):
        self.boxes = []
        if self.extras[1]:
            self.tileBox = Hitbox(current_location.x,current_location.y,16,16,["hitbox"],{'layer': self.extras[0]})
            self.boxes.append(self.tileBox)
        if self.extras[2]:
            self.topBox = Hitbox(current_location.x,current_location.y+15,16,1,["hitbox"],{'layer': self.extras[0]})
            self.boxes.append(self.topBox)
        if self.extras[3]:
            self.rightBox = Hitbox(current_location.x+15,current_location.y,1,16,["hitbox"],{'layer': self.extras[0]})
            self.boxes.append(self.rightBox)
        if self.extras[4]:
            self.bottomBox = Hitbox(current_location.x,current_location.y,16,1,["hitbox"],{'layer': self.extras[0]})
            self.boxes.append(self.bottomBox)
        if self.extras[5]:
            self.leftBox = Hitbox(current_location.x,current_location.y,1,16,["hitbox"],{'layer': self.extras[0]})
            self.boxes.append(self.leftBox)
        if draw:
            self.draw(current_location)
    def draw(self,current_position,tint = WHITE):
        draw_texture(self.texture,current_position.x,current_position.y,tint)
    def delete(self):
        for box in self.boxes:
            box.delete()
        unload_texture(f"textures/tiles/{self.t}")
        del self

class Player():
    def __init__(self,stats,texture_folder,extras):
        self.position = Vector2(0,0)
        self.size = Vector2(16,16)
        self.stats = stats
        self.extras = extras
        self.textures = f"textures/player/{texture_folder}"
        self.collision_box = Hitbox(self.position.x,self.position.y,self.size.x,self.size.y,["player"])
    def draw(self,position,rotation,texture_name,tint = WHITE):
        texture = f"{self.textures}/{texture_name}"
        if file_exists(texture):
            texture = load_texture(texture)
        else:
            texture = load_texture("textures/missing.png")
        if self.size.x/16 == self.size.y/16:
            scale = self.size.x/16
        else:
            scale = 1
        draw_texture_ex(texture,position,rotation,scale,tint)
        unload_texture(texture)
    def next_frame(self):
        if is_key_down(Key.KEY_W):
            self.position.y += 1
            self.collision_box.update_position(self.position)
            box = self.collision_box.check_collision(["wall"],{'layer': self.extras['layer']})
            if type(box) == Hitbox:
                self.position.y -= 1
                self.collision_box.update_position(self.position)
        if is_key_down(Key.KEY_D):
            self.position.x += 1
            self.collision_box.update_position(self.position)
            box = self.collision_box.check_collision(["wall"],{'layer': self.extras['layer']})
            if type(box) == Hitbox:
                self.position.x -= 1
                self.collision_box.update_position(self.position)
        if is_key_down(Key.KEY_S):
            self.position.y -= 1
            self.collision_box.update_position(self.position)
            box = self.collision_box.check_collision(["wall"],{'layer': self.extras['layer']})
            if type(box) == Hitbox:
                self.position.y += 1
                self.collision_box.update_position(self.position)
        if is_key_down(Key.KEY_A):
            self.position.x -= 1
            self.collision_box.update_position(self.position)
            box = self.collision_box.check_collision(["wall"],{'layer': self.extras['layer']})
            if type(box) == Hitbox:
                self.position.x += 1
                self.collision_box.update_position(self.position)
        self.collision_box.update_position(self.position)