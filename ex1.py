import graphics as gr

window = gr.GraphWin("Tanya project", 500, 500)

def draw_sky():
    sky = gr.Rectangle(gr.Point(0,500),gr.Point(500,0))
    sky.setFill('skyblue')

    sky.draw(window)
    

def draw_sun():
    sun = gr.Circle(gr.Point(40, 40), 40)
    sun.setFill('yellow')

    sun.draw(window)

def draw_clouds():
    cloud1 = gr.Circle(gr.Point(20,55),25)
    cloud2 = gr.Circle(gr.Point(55,55),25)
    cloud3 = gr.Circle(gr.Point(15,75),25)
    cloud4 = gr.Circle(gr.Point(40,75),25)
    cloud5 = gr.Circle(gr.Point(70,75),25)

    cloud1.setFill('white')
    cloud2.setFill('white')
    cloud3.setFill('white')
    cloud4.setFill('white')
    cloud5.setFill('white')

    cloud1.draw(window)
    cloud2.draw(window)
    cloud3.draw(window)
    cloud4.draw(window)
    cloud5.draw(window)


def draw_vase():
    vase1 = gr.Rectangle(gr.Point(170,500),gr.Point(330,350))
    vase2 = gr.Rectangle(gr.Point(150,350),gr.Point(350,300))

    vase1.setFill('brown')
    vase2.setFill('brown')

    vase1.draw(window)
    vase2.draw(window)

def draw_stem():
    stem = gr.Line(gr.Point(250, 300), gr.Point(250, 150))
    stem.setWidth(10)
    stem.setFill('green')
    stem.draw(window)

def draw_flower():
    flower1 = gr.Circle(gr.Point(180, 80), 50)
    flower2 = gr.Circle(gr.Point(180, 150), 50)
    flower3 = gr.Circle(gr.Point(320, 80), 50)
    flower4 = gr.Circle(gr.Point(320, 150), 50)
    flower5 = gr.Circle(gr.Point(250, 50), 50)
    flower6 = gr.Circle(gr.Point(250, 185), 50)
    flower = gr.Circle(gr.Point(250, 110), 40)

    flower1.setFill('red')
    flower2.setFill('red')
    flower3.setFill('red')
    flower4.setFill('red')
    flower5.setFill('red')
    flower6.setFill('red')
    flower.setFill('yellow')

    flower1.draw(window)
    flower2.draw(window)
    flower3.draw(window)
    flower4.draw(window)
    flower5.draw(window)
    flower6.draw(window)
    flower.draw(window)

def draw_caterpillar():
    caterpillar1 = gr.Circle(gr.Point(20, 480), 20)
    caterpillar2 = gr.Circle(gr.Point(60, 480), 20)
    caterpillar3 = gr.Circle(gr.Point(100, 480), 20)
    caterpillar4 = gr.Circle(gr.Point(140, 480), 20)
    caterpillar5 = gr.Circle(gr.Point(180, 480), 20)
    caterpillar = gr.Circle(gr.Point(190, 440), 25)
    caterpillarx1 = gr.Line(gr.Point(190, 415), gr.Point(205, 390))
    caterpillarx2 = gr.Line(gr.Point(190, 415), gr.Point(175, 390))

    caterpillarx1 .setWidth(4)
    caterpillarx2 .setWidth(4)

    caterpillar1.setFill('green')
    caterpillar2.setFill('green')
    caterpillar3.setFill('green')
    caterpillar4.setFill('green')
    caterpillar5.setFill('green')
    caterpillar.setFill('green')
    caterpillarx1 .setFill('black')
    caterpillarx2 .setFill('black')

    caterpillar1.draw(window)
    caterpillar2.draw(window)
    caterpillar3.draw(window)
    caterpillar4.draw(window)
    caterpillar5.draw(window)
    caterpillar.draw(window)
    caterpillarx1 .draw(window)
    caterpillarx2.draw(window)

def draw_beautiful_picture():
    draw_sky()
    draw_sun()
    draw_clouds()
    draw_vase()
    draw_stem()
    draw_flower()
    draw_caterpillar()

draw_beautiful_picture()
    
window.getMouse()

window.close()

