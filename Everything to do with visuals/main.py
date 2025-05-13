import random
from pyray import *
global control_scheme,last_clicked
last_clicked = ''
control_scheme = 'KBM'
fpsCounter = True
class UI():
    def hide(self):
        self.hidden = True
    def show(self):
        self.hidden = False
class Slider(UI):
    def __init__(self,locX,locY,width,height,colorR,colorC):
        self.vector_loc = [locX,locY]
        self.vector_size = [width,height]
        self.circle_vector_loc = [locX,locY]
        self.locX = locX
        self.locY = locY
        self.width = width
        self.height = height
        self.colorR = colorR
        self.colorC = colorC
        self.__value = round(height/2)
        self.__value_range = height
        self.__id = "volume"
        self.hidden = False
    def get_value(self):
        return self.__value
    def next_frame(self):
        if not self.hidden:
            draw_rectangle_v(self.vector_loc,self.vector_size,self.colorR)
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
class Button(UI):
    def __init__(self,locX,locY,width,height,color,colorC,colorT,text = ''):
        self.vector_loc = [locX,locY]
        self.vector_size = [width,height]
        self.locX = locX
        self.locY = locY
        self.width = width
        self.height = height
        self.color = color
        self.colorC = colorC
        self.colorT = colorT
        self.text = text
        self.__clicked = False
        self.hidden = False
    def next_frame(self):
        if not self.hidden:
            if control_scheme == "KBM":
                if check_collision_point_rec(get_mouse_position(),self.vector_loc):
                    self.__clicked = True
        if self.__clicked:
            draw_rectangle_v(self.vector_loc,self.vector_size,self.colorC)
        else:
            draw_rectangle_v(self.vector_loc,self.vector_size,self.color)
        draw_text(self.text,round(self.locX-(self.width/2)),round(self.locY-(self.height/2)),round(self.height*.75),self.colorT)
    def is_clicked(self):
        return self.__clicked
init_window(1280,720, "dungeons_and_damage")
set_target_fps(60)
#toggle_borderless_windowed()
volume = Slider(1265,310,10,100,BLUE,DARKBLUE)
start = Button(640,360, 100,40, BLUE,DARKBLUE, YELLOW,"Game Start")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    if fpsCounter:
        draw_text(f"{get_fps()}\nFPS",10,10,50,VIOLET)
    start.next_frame()
    if start.is_clicked():
        start.hide()
        draw_text("Starting game",640,360,20,BLUE)
    set_master_volume = volume.next_frame()
    end_drawing()
close_window()