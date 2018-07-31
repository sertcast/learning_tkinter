from bucky import useful
from tkinter import *

class MyButton:

    def __init__(self, canvas, text, x, y, font="Times 20"):
        self.setup( canvas, text, x, y, font)
        self.shape = canvas.create_rectangle(self.txtProperties[0] - 10, self.txtProperties[1] - 5,
                                             self.txtProperties[2] + 10, self.txtProperties[3] + 5,
                                             fill = useful.color(255, 255, 255))
        self.text = canvas.create_text(100, 100, text="hello", fill="red", font=font)

    def setup(self, canvas, text, x, y, font):
        self.canvas = canvas
        self.str = text
        self.textX = x
        self.textY = y
        self.text = canvas.create_text(100, 100, text="hello", fill="red", font=font)
        self.txtProperties = canvas.bbox(self.text)
        self.rectX = self.txtProperties[0] - 10
        self.rectY = self.txtProperties[1] - 5
        self.w = (self.txtProperties[2] - self.txtProperties[0]) + 20
        self.h = (self.txtProperties[3] - self.txtProperties[1]) + 10
        self.canvas.delete(self.text)

    def set_visible(self, vis):
        pass

    def clicked(self, event):
        mouseX = event.x
        mouseY = event.y
        if (mouseX >= self.rectX and mouseX <= self.rectX + self.w) and (mouseY >= self.rectY and mouseY <= self.rectY + self.h):
            return True
        return False