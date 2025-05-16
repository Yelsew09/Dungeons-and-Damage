import random
from pyray import *
from raylib import *
import numpy as np
global control_scheme,last_clicked
last_clicked = ''
with open("settings.txt","rt") as options:
    control_scheme = options.readline()
    UP = options.readline()
    LEFT = options.readline()
    DOWN = options.readline()
    RIGHT = options.readline()
    A = options.readline()
    B = options.readline()
    L = options.readline()
    R = options.readline()
    START = options.readline()
    SELECT = options.readline()

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
                #Horizontal control
                if self.rotated:
                    if control_scheme == "Keyboard":
                        if IsKeyDown(LEFT) or IsKeyDown(L):
                            self.__value -= self.size[1] / 100
                        elif IsKeyDown(RIGHT) or IsKeyDown(R):
                            self.__value += self.size[1] / 100
                #Vertical control
                elif not self.rotated:
                    if control_scheme == "Keyboard":
                        if IsKeyDown(DOWN):
                            self.__value -= self.size[1] / 100
                        elif IsKeyDown(UP):
                            self.__value += self.size[1] / 100
            if self.rotated:
                draw_rectangle_v(self.location,self.size,self.rColor)
                draw_circle_v([self.location[0]+self.__value,self.location[1]],self.size[1],self.cColor)
            elif not self.rotated:
                draw_rectangle_v(self.location,self.size,self.rColor)
                draw_circle_v([self.location[0],self.location[1]+self.__value],self.size[0],self.cColor)
    def get_value(self):
        return self.__value
class OptionList(UI):
    def __init__(self,li,di,lo,h,c,Sc,Tc):
        self.options = li
        self.tColor = Tc
        self.dimensions = di
        self.xLength = di[0]
        self.yLength = di[1]
        self.locX = lo[0]
        self.locY = lo[1]
        self.Color = c
        self.sColor = Sc
        self.__hidden = h
    class Option(UI):
        def __init__(self,t,):
            self.text = t
            self.id = str(self)
        def next_frame(self,p):
            if not self.__hidden:
                if p.is_selecting() == self.id:
                    if control_scheme == "Keyboard" and IsKeyDown(A):
                        self.__pressed = True
                if self.__pressed == True:
                    draw_rectangle_lines(self.locX,self.locY,self.width,self.height,self.sColor)
                    draw_text(self.text,self.locX+2,self.locY+2,self.fontsize,self.tColor)
                elif not self.__pressed == True:
                    draw_rectangle_lines(self.locX,self.locY,self.width,self.height,self.Color)
                    draw_text(self.text,self.locX+2,self.locY+2,self.fontsize,self.tColor)
        def is_pressed(self):
            return self.__pressed
class Pointer(UI):
    def __init__(self,p,s,r,c,h):
        self.__pointed_at = p
        self.size = s
        self.id = str(self)
        self.rotated = r
        self.color = c
        self.__locked = False
        self.__hidden = h
    def next_frame(self,options,oLength,oHeight):
        if not self.__hidden:
            sv = self.__pointed_at
            if control_scheme == "Keyboard":
                if IsKeyDown(UP):
                    try:
                        self.__pointed_at = options[sv-oLength]
                    except IndexError:
                        self.__pointed_at = options[sv+(oLength*(oHeight-1))]
                elif IsKeyDown(DOWN):
                    try:
                        self.__pointed_at = options[sv+oLength]
                    except IndexError:
                        self.__pointed_at = options[sv-(oLength*(oHeight-1))]
                elif IsKeyDown(RIGHT):
                    if (sv + 1) % oLength == 0:
                        self.__pointed_at = options[sv-(oLength-1)]
                    else:
                        self.__pointed_at = options[sv+1]
                elif IsKeyDown(LEFT):
                    if sv % oLength == 0:
                        self.__pointed_at = options[sv+(oLength-1)]
                    else:
                        self.__pointed_at = options[sv-1]
            if self.rotated:
                vert1 = [self.__pointed_at.locX+self.__pointed_at.width/2,self.__pointed_at.locY+10]
                vert2 = [vert1[0]-15,vert1[1]+15]
                vert3 = [vert1[0]+15,vert1[1]+15]
            else:
                vert1 = [self.__pointed_at.locX-10,self.__pointed_at.locY-self.__pointed_at.height/2]
                vert2 = [vert1[0]-15,vert1[1]+15]
                vert3 = [vert1[0]-15,vert1[1]-15]
            draw_triangle(vert1,vert2,vert3,self.color)
    def is_selecting(self):
        return self.__pointed_at
    def lock(self):
        self.__locked = True
    def unlock(self):
        self.__locked = False
class Screen():
    def __init__(self,e,p,gr_lay):
        self.elements = e
        self.pointer = p
        self.layout = gr_lay
        self.yLength = gr_lay[1]
    def next_frame(self):
        if self.__is_active:
            self.pointer.next_frame()
            for element in self.elements:
                element.next_frame(self.pointer)
    def is_showing(self):
        return self.__is_active
