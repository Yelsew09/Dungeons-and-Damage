import random
from pyray import *
control_scheme = "KBM"
fpsCounter = True
class slider():
    def __init__(self,locX,locY,width,height,colorR,colorC):
        self.locX = locX
        self.locY = locY
        self.width = width
        self.height = height
        self.colorR = colorR
        self.colorC = colorC
        self.__value = round(height/2)
        self.__value_range = height
    def get_value(self):
        return self.__value
    def adjust(self):
        draw_rectangle(self.locX,self.locY,self.width,self.height,self.colorR)
        draw_circle(round(self.locX+(self.width/2)),self.locY+self.get_value(),self.width,self.colorC)
        if control_scheme == "KBM":
            if is_mouse_button_down(5):
                if get_mouse_x() <= self.locX+(self.width/2) and get_mouse_x >= self.locX+(self.width/2):
                    if get_mouse_y() <= self.get_value()+self.width and get_mouse_y() >= self.get_value()-self.width:
                        draw_text("This works.",190, 200, 20, VIOLET)
init_window(1280,720, "dungeons_and_damage")
set_target_fps(60)
#toggle_borderless_windowed()
volume = slider(1265,310,10,100,BLUE,DARKBLUE)
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    if fpsCounter:
        draw_text(f"{get_fps()} FPS",10,10,50,VIOLET)
    volume.adjust()
    end_drawing()
close_window()