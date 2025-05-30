import main as m
from raylib import *
from pyray import *
class UI():
    def hide(self):
        self.__hidden = True
    def show(self):
        self.__hidden = False
    def is_visible(self):
        return self.__hidden

class Slider(UI):
    def __init__(self,l,s,sv,rC,cC,csC,r,h=True):
        self.location = Vector2(l[0],l[1])
        self.size = Vector2(s[0],s[1])
        self.rColor = rC
        self.cColor = cC
        self.csColor = csC
        self.rotated = r
        self.id = str(self)
        self.__value = sv
        self.__hidden = h

    def get_value(self):
        return self.__value

    def is_hidden(self):
        return self.__hidden

    def next_frame(self,pointer):
        if not self.is_hidden():
            body = Rectangle(self.location,self.size)
            circleCol = self.cColor
            if pointer.is_selecting(self.id) and pointer.is_locked():
                circleCol = self.csColor
                if self.rotated:
                    circleRad = self.size[0]
                    if is_key_down(m.LEFT):
                        self.__value -= 1
                    elif is_key_down(m.RIGHT):
                        self.__value += 1
                    circleAlt = (self.size[0]/100)*self.get_value()
                    circleLoc = Vector2(self.size[0]+circleAlt)
                else:
                    circleRad = self.size[1]
                    if is_key_down(m.DOWN):
                        self.__value -= 1
                    elif is_key_down(m.UP):
                        self.__value += 1
            elif pointer.is_selecting(self.id) and not pointer.is_locked() and is_key_down(m.START):
                pointer.lock()
            elif pointer.is_selecting(self.id) and pointer.is_locked() and is_key_down(m.START):
                pointer.unlock()
            draw_rectangle_rounded(body,.5,4,self.rColor)
            draw_circle_v(circleLoc,circleRad,circleCol)
    

class Options(UI):
    def __init__(self,op,lo,sz,le,fs,rC,tC,bC):
        self.options = op
        self.num_options = len(self.options)
        self.location = Vector2[lo[0],lo[1]]
        self.size = sz
        self.list_length = le
        self.rColor = rC
        self.tColor = tC
        self.bColor = bC
        self.font_size = fs
        self.id = str(self)
        self.__hidden = True
    class Option():
        def __init__(self,tx,lo,sz,rC,tC,bC):
            self.text = tx
            self.location = Vector2(lo[0],lo[1])
            self.size = Vector2(sz[0],sz[1])
            self.rColor = rC
            self.tColor = tC
            self.bColor = bC
            self.temp_id = f"option {self}"
        def next_frame(self,pointer):
            draw_rectangle_v(self.location,self.size,self.rColor)
            border = Rectangle()