import graphics as gr
import random
import time

window = gr.GraphWin("Tanya project", 500, 500)


def draw_sky():
    sky = gr.Rectangle(gr.Point(0, 500), gr.Point(500, 0))
    sky.setFill('skyblue')

    sky.draw(window)
    

def draw_sun():
    global sun
    sun = gr.Circle(gr.Point(460, 40), 40)
    sun.setFill('yellow')
    sun.setOutline('yellow')

    sun.draw(window)


def draw_clouds(x, y):
    for _ in range(3):
        for _ in range(7):
            x -= random.randint(0, 10)
            r = random.randint(20, 25)
            distance_x = random.randint(50, 60)
            distance_y = random.randint(50, 60)
            cloud = gr.Circle(gr.Point(x + distance_x, y + distance_y), r)
            cloud.setOutline('white')
            cloud.setFill('white')
            cloud.draw(window)

        x = x - 60
        y = y - 10
        

def draw_vase(z1, z2, z3, z4):
    for _ in range(2):
        vase = gr.Rectangle(gr.Point(z1, z2), gr.Point(z3, z4))
        vase.setFill('brown')
        vase.draw(window)
        z1 = z1 - 20
        z2 = z2 - 150
        z3 = z3 + 20
        z4 = z4 - 50
    

def draw_stem():
    stem = gr.Line(gr.Point(140, 300), gr.Point(140, 150))
    stem.setWidth(10)
    stem.setFill('green')
    stem.draw(window)


def draw_flower(y1, y2, y3):
    for _ in range(2):
        flower_1 = gr.Circle(gr.Point(70, y1), 50)
        flower_1.setFill('red')
        flower_1.draw(window)
        y1 = y1 + 70

    for _ in range(2):
        flower_2 = gr.Circle(gr.Point(210, y2), 50)
        flower_2.setFill('red')
        flower_2.draw(window)
        y2 = y2 + 70

    for _ in range(2):
        flower_3 = gr.Circle(gr.Point(140, y3), 50)
        flower_3.setFill('red')
        flower_3.draw(window)
        y3 = y3 + 135

    flower = gr.Circle(gr.Point(140, 110), 40)
    flower.setFill('yellow')

    flower.draw(window)


def draw_caterpillar(x, y):
    for x1 in range(5):
        caterpillar = gr.Circle(gr.Point(x, 480), 20)
        caterpillar.setFill('green')
        caterpillar.draw(window)
        x = x + 40

    for y1 in range(2):
        caterpillar_x = gr.Line(gr.Point(250, 415), gr.Point(y, 390))
        caterpillar_x .setWidth(4)
        caterpillar_x .setFill('black')
        caterpillar_x .draw(window)
        y = y - 30

    caterpillarh = gr.Circle(gr.Point(250, 440), 25)
    caterpillarh.setFill('green')
    caterpillarh.draw(window)
   

def draw_beautiful_picture():
    draw_sky()
    draw_sun()
    draw_clouds(400, 90)
    draw_vase(60, 500, 220, 350)
    draw_stem()
    draw_flower(80, 80, 50)
    draw_caterpillar(80, 265)

    for _ in range(20):
        sun.move(-1, 0)
        time.sleep(0.2)


draw_beautiful_picture()
window.getMouse()
window.close()
