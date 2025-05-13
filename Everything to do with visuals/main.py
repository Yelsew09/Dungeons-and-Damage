import random
from raylib import *
global control_scheme,last_clicked
last_clicked = ''
control_scheme = 'Keyboard'
fpsCounter = True
class UI():
    def hide(self):
        self.hidden = True
    def show(self):
        self.hidden = False
    def get_value(self):
        try:
            return self.__value
        except:
            return None
class Slider(UI): #A slider that gives a value that changes depending on user input
    def __init__(self,l,s,rc,cc,sv,r):
        self.location = l
        self.size = s
        self.rColor = rc
        self.cColor = cc
        self.__value = sv
        self.rotated = r
        self.id = str(self)
    def next_frame(self,pointer):
        if not self.hidden:
            if self.rotated:
                if control_scheme == "Keyboard" and pointer.selecting == self.id:
                        if IsKeyDown(KEY_D) or IsKeyDown(KEY_RIGHT):
                            self.__value += 1
                        elif IsKeyDown(KEY_A) or IsKeyDown(KEY_LEFT):
                            self.__value -= 1
            else:
                if control_scheme == "Keyboard" and pointer.selecting == self.id:
                        if IsKeyDown(KEY_W) or IsKeyDown(KEY_UP):
                            self.__value += 1
                        elif IsKeyDown(KEY_S) or IsKeyDown(KEY_DOWN):
                            self.__value -= 1


class Selection(UI): #Basically a button
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
            if control_scheme == "Keyboard":
                pass
    def is_clicked(self):
        return self.__clicked
class Pointer(UI):
    def __init__(self,color):
        self.selecting = None
InitWindow(1280,720, "dungeons_and_damage")
SetTargetFPS(60)
#toggle_borderless_windowed()
volume = Slider()
start = Selection()
while not WindowShouldClose():
    BeginDrawing()
    ClearBackground(WHITE)
    if fpsCounter:
        DrawText(f"{GetFPS()}\nFPS",10,10,50,VIOLET)
    start.next_frame()
    if start.is_clicked():
        start.hide()
        DrawText("Starting game",640,360,20,BLUE)
    set_master_volume = volume.next_frame()
    EndDrawing()
CloseWindow()