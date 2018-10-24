import graphics as gr
import time
from collections import namedtuple


window = gr.GraphWin("Tanya project", 500, 500)

def draw_sky():
    sky = gr.Rectangle(gr.Point(0,500),gr.Point(500,0))
    sky.setFill('skyblue')

    sky.draw(window)
    
def draw_sun():
    global sun
    sun = gr.Circle(gr.Point(460, 40), 40)
    sun.setFill('yellow')
    sun.setOutline('yellow')

    sun.draw(window)

def draw_clouds(x,x1,y):
    for m in range(3):
        for m in range(2):
            cloud = gr.Circle(gr.Point(x,y),25)
            cloud.setFill('white')
            cloud.setOutline('white')
            cloud.draw(window)
            x = x + 35

        for m in range(3):
            cloud1 = gr.Circle(gr.Point(x1,y+20),25)
            cloud1.setFill('white')
            cloud1.setOutline('white')
            cloud1.draw(window)
            x1 = x1 + 30
        x = x - 150
        x1 = x1 - 180
        y = y + 50
        
def draw_vase(z1,z2,z3,z4):
    for z in range(2):
        vase = gr.Rectangle(gr.Point(z1,z2),gr.Point(z3,z4))
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

def draw_flower(y1,y2,y3):
    for x in range(2):
        flower1 = gr.Circle(gr.Point(70, y1), 50)
        flower1.setFill('red')
        flower1.draw(window)
        y1 = y1 + 70

    for x in range(2):
        flower1 = gr.Circle(gr.Point(210, y2), 50)
        flower1.setFill('red')
        flower1.draw(window)
        y2 = y2 + 70

    for x in range(2):
        flower1 = gr.Circle(gr.Point(140, y3), 50)
        flower1.setFill('red')
        flower1.draw(window)
        y3 = y3 + 135

    flower = gr.Circle(gr.Point(140, 110), 40)
    flower.setFill('yellow')

    flower.draw(window)

def draw_caterpillar(x,y):
    for x1 in range(5):
        caterpillar = gr.Circle(gr.Point(x, 480), 20)
        caterpillar.setFill('green')
        caterpillar.draw(window)
        x = x + 40
        
    
    for y1 in range(2):
        caterpillarx = gr.Line(gr.Point(250, 415), gr.Point(y, 390))
        caterpillarx .setWidth(4)
        caterpillarx .setFill('black')
        caterpillarx .draw(window)
        y = y -30 
        
    
    caterpillarh = gr.Circle(gr.Point(250, 440), 25)
    caterpillarh.setFill('green')
    caterpillarh.draw(window)
   

def draw_beautiful_picture():
    draw_sky()
    draw_sun()
    draw_clouds(440,435,55)
    draw_vase(60,500,220,350)
    draw_stem()
    draw_flower(80,80,50)
    draw_caterpillar(80,265)

    for i in range(20):
        sun.move(-1,0)

        time.sleep(0.2)



draw_beautiful_picture()
    
window.getMouse()

window.close()

