import random
from pyray import *
global control_scheme,last_clicked
last_clicked = ''
control_scheme = 'KBM'
fpsCounter = True
class slider():
    def __init__(self,locX,locY,width,height,colorR,colorC):
        self.vector_loc = [locX,locY]
        self.vector_size = [width,height]
        self.locX = locX
        self.locY = locY
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
        draw_rectangle_v(self.vector_loc,self.vector_size)
        if control_scheme == "KBM":
            if check_collision_point_circle(get_mouse_position(),self.circle_vector_loc,self.width):
                if is_mouse_button_down("mouse_button_left"):
                    temp_val = get_mouse_y()
                    if temp_val > self.locY+(self.height/2):
                        self.__value = 0
                    elif temp_val < self.locY-(self.height/2):
                        self.__value = 100
                    else:
                        self.__value = temp_val - (get_screen_height()-self.height)
        self.circle_vector_loc = [self.locX+(self.width/2),self.locY+self.get_value()]
        draw_circle_v(self.circle_vector_loc,self.width,self.colorC)
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