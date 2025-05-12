import random
from pyray import *
global control_scheme,last_clicked
last_clicked = ''
control_scheme = ''
fpsCounter = True
class slider():
    def __init__(self,locX,locY,width,height,colorR,colorC):
        self.vector_loc = [locX,locY]
        self.width = width
        self.height = height
        self.colorR = colorR
        self.colorC = colorC
        self.__value = round(height/2)
        self.__value_range = height
        self.__id = "volume"
    def get_value(self):
        return self.__value
    def adjust(self):
        draw_rectangle(self.locX,self.locY,self.width,self.height,self.colorR)
        draw_circle_v(self.vector_loc)
        if control_scheme == "KBM":
            if check_collision_point_circle() and is_mouse_button_down(MouseButton):
                    draw_text("This works.",190, 200, 20, VIOLET)
                    last_clicked = self.id
init_window(1280,720, "dungeons_and_damage")
set_target_fps(60)
#toggle_borderless_windowed()
volume = slider(1265,310,10,100,BLUE,DARKBLUE)
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    if fpsCounter:
        draw_text(f"{get_fps()} FPS",10,10,50,VIOLET)
    set_master_volume = volume.adjust()
    end_drawing()
close_window()