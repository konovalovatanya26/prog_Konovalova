from tkinter import *
import time
import random
import graphics as gr
count = 0


def tick():
    global x, y, r
    root.after(1000, tick)
    canv.delete(ALL)
    x = random.randint(10, 600)
    y = random.randint(10, 600)
    r = random.randint(10, 100)
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    canv.create_oval(x-r, y-r, x+r, y+r, fill=gr.color_rgb(red, blue, green))
    canv.create_text(400, 300, text=str(count), font='Arial 25')


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
root.after_idle(tick)


def click(event):
    x1 = event.x
    y1 = event.y
    global count
    if abs(x1 - x) < r and abs(y1 - y) < r:
        count = count + 1
    else:
        count = count - 1


canv.bind('<Button-1>', click)
canv.bind('<Button-3>', click)
root.mainloop()
