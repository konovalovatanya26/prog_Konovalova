import turtle
turtle.shape('turtle')

i = 20
for x in range (10):
    for x in range (4):
        turtle.forward(i)
        turtle.left(90)
    i=i+10
    turtle.penup()
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(180)
    turtle.pendown()

    

  
