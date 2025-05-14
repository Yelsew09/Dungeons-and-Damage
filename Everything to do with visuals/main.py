import random
from pyray import *
from raylib import *
global control_scheme,last_clicked
last_clicked = ''
setting = open("settings.txt","r")
control_scheme = 'Keyboard'
fpsCounter = True
class UI():
    def hide(self):
        self.__hidden = True
    def show(self):
        self.__hidden = False
    def is_visible(self):
        return self.__hidden
class Slider(UI):
    def __init__(self,l,s,Rc,Cc,r,Sv,h):
        self.location = l
        self.size = s
        self.rColor = Rc
        self.cColor = Cc
        self.id = str(self)
        self.rotated = r
        self.__value = Sv
        self.__hidden = h
    def next_frame(self,pointer):
        if not self.__hidden:
            if pointer.is_selecting() == self.id:
                if self.rotated:
                    if control_scheme == "Keyboard":
                        if IsKeyDown(LEFT):
                            self.__value -= 1
                        elif IsKeyDown(RIGHT):
                            self.__value += 1
                elif not self.rotated:
                    if control_scheme == "Keyboard":
                        if IsKeyDown(DOWN):
                            self.__value -= 1
                        elif IsKeyDown(UP):
                            self.__value += 1
            if self.rotated:
                draw_rectangle_v(self.location,self.size,self.rColor)
                draw_circle_v([self.location[0]+self.__value,self.location[1]],self.size[1],self.cColor)
            elif not self.rotated:
                draw_rectangle_v(self.location,self.size,self.rColor)
                draw_circle_v([self.location[0],self.location[1]+self.__value],self.size[0],self.cColor)
    def get_value(self):
        return self.__value
class Option(UI):
    def __init__(self,l,s,c,Sc,h,t=''):
        self.location = l
        self.size = s
        self.Color = c
        self.sColor = Sc
        self.text = t
        self.id = str(self)
        self.__hidden = h
        self.__pressed = False
    def next_frame(self,pointer):
        if not self.__hidden:
            if pointer.is_selecting() == self.id:
                if control_scheme == "Keyboard" and IsKeyDown(KEY_J)
    def is_pressed(self):
        return self.__pressed