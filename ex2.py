import graphics as gr

window = gr.GraphWin("Tanya project", 500, 500)

def draw_sky():
    sky = gr.Rectangle(gr.Point(0,500),gr.Point(500,0))
    sky.setFill('skyblue')

    sky.draw(window)
    

def draw_sun():
    sun = gr.Circle(gr.Point(460, 40), 40)
    sun.setFill('yellow')

    sun.draw(window)

def draw_clouds():
    cloud11 = gr.Circle(gr.Point(440,55),25)
    cloud12 = gr.Circle(gr.Point(475,55),25)
    cloud13 = gr.Circle(gr.Point(435,75),25)
    cloud14 = gr.Circle(gr.Point(460,75),25)
    cloud15 = gr.Circle(gr.Point(490,75),25)

    cloud21 = gr.Circle(gr.Point(345,75),25)
    cloud22 = gr.Circle(gr.Point(370,75),25)
    cloud23 = gr.Circle(gr.Point(335,95),25)
    cloud24 = gr.Circle(gr.Point(360,95),25)
    cloud25 = gr.Circle(gr.Point(390,95),25)

    cloud31 = gr.Circle(gr.Point(255,35),25)
    cloud32 = gr.Circle(gr.Point(280,35),25)
    cloud33 = gr.Circle(gr.Point(245,55),25)
    cloud34 = gr.Circle(gr.Point(270,55),25)
    cloud35 = gr.Circle(gr.Point(300,55),25)

    cloud11.setFill('white')
    cloud12.setFill('white')
    cloud13.setFill('white')
    cloud14.setFill('white')
    cloud15.setFill('white')

    cloud21.setFill('white')
    cloud22.setFill('white')
    cloud23.setFill('white')
    cloud24.setFill('white')
    cloud25.setFill('white')

    cloud31.setFill('white')
    cloud32.setFill('white')
    cloud33.setFill('white')
    cloud34.setFill('white')
    cloud35.setFill('white')

    cloud11.draw(window)
    cloud12.draw(window)
    cloud13.draw(window)
    cloud14.draw(window)
    cloud15.draw(window)

    cloud21.draw(window)
    cloud22.draw(window)
    cloud23.draw(window)
    cloud24.draw(window)
    cloud25.draw(window)

    cloud31.draw(window)
    cloud32.draw(window)
    cloud33.draw(window)
    cloud34.draw(window)
    cloud35.draw(window)


def draw_vase():
    vase1 = gr.Rectangle(gr.Point(60,500),gr.Point(220,350))
    vase2 = gr.Rectangle(gr.Point(20,350),gr.Point(240,300))

    vase1.setFill('brown')
    vase2.setFill('brown')

    vase1.draw(window)
    vase2.draw(window)

def draw_stem():
    stem = gr.Line(gr.Point(140, 300), gr.Point(140, 150))
    stem.setWidth(10)
    stem.setFill('green')
    stem.draw(window)

def draw_flower():
    flower1 = gr.Circle(gr.Point(70, 80), 50)
    flower2 = gr.Circle(gr.Point(70, 150), 50)
    flower3 = gr.Circle(gr.Point(210, 80), 50)
    flower4 = gr.Circle(gr.Point(210, 150), 50)
    flower5 = gr.Circle(gr.Point(140, 50), 50)
    flower6 = gr.Circle(gr.Point(140, 185), 50)
    flower = gr.Circle(gr.Point(140, 110), 40)

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
    caterpillar1 = gr.Circle(gr.Point(80, 480), 20)
    caterpillar2 = gr.Circle(gr.Point(120, 480), 20)
    caterpillar3 = gr.Circle(gr.Point(160, 480), 20)
    caterpillar4 = gr.Circle(gr.Point(200, 480), 20)
    caterpillar5 = gr.Circle(gr.Point(240, 480), 20)
    caterpillar = gr.Circle(gr.Point(250, 440), 25)
    caterpillarx1 = gr.Line(gr.Point(250, 415), gr.Point(265, 390))
    caterpillarx2 = gr.Line(gr.Point(250, 415), gr.Point(235, 390))

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


