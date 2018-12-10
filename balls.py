from tkinter import *
import graphics as gr
import random

root = Tk()
root.geometry("600x600")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

balls = []

def generate_balls():
    for _ in range(7):
        global ball, x, y, r, dx, dy, appearance
        x = random.randint(20, 270)
        y = random.randint(20, 270)
        r = random.randint(10, 50)
        dx = random.randint(-15, 15)
        dy = random.randint(-10, 10)
        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        gree = random.randint(0, 255)
        appearance = canvas.create_oval(x - r, y - r, x + r, y + r, fill=gr.color_rgb(red, blue, gree))
        ball = [x, y, r, dx, dy, appearance]
        balls.append(ball)

def tick_handler():
    for ball in range(len(balls)):
        global x, y, r, dx, dy, appearance
        x, y, r, dx, dy, appearance = balls[ball]
        
        # Отражение от края холста
        if x < 0:
            dx = -dx; x = 0
        elif x > 600-40:
            dx = -dx
            x = 600-40
        if y < 0:
            dy = -dy
            y = 0
        elif y > 600-40:
            dy = -dy
            y = 600-40
        x = x + dx; y = y + dy
        canvas.move(appearance, dx, dy)
        balls[ball] = [x, y, r, dx, dy, appearance]


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        print("Заморозка!")
        freeze = True
        return
    tick_handler()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)

def unfreezer(event):
    global freeze
    if freeze == True:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)

speed_scale = Scale(root, orient=HORIZONTAL, length=300,
               from_=0, to=10, tickinterval=1, resolution=1)
speed_scale.pack()

# Скорость = 1
speed_scale.set(1);
freeze = False

generate_balls()
root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)
root.mainloop()
