from tkinter import *
from bucky import MyButton

WIDTH = 1000
HEIGHT = 650



root = Tk()
root.title("this is the amariqa")

canvas = Canvas(root, width=WIDTH, height=HEIGHT)

button1 = MyButton.MyButton(canvas, "click", 100, 100, font="Times 40")

def mouseClicked(event):
    print(button1.clicked(event))
def mouseMoved(event):
    button1.mouse_on(event)
    button1.update()


def draw():
    print("hello")
canvas.bind("<Button-1>", mouseClicked)
canvas.bind("<Motion>", mouseMoved)
canvas.pack()
root.mainloop()


