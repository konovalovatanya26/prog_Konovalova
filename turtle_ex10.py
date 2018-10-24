import turtle
turtle.shape('turtle')

Number = 100
Step = 5


def circle(Number, Step):
    for step in range(Number):
        turtle.forward(Step)
        turtle.left(360/Number)
    for step in range(Number):
        turtle.forward(Step)
        turtle.right(360/Number)
        

for x in range(3):
    circle(Number,Step)
    turtle.left(60)
    
    
