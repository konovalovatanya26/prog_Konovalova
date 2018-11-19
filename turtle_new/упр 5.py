import turtle
turtle.shape('turtle')

i = 20
for _ in range (10):
    for _ in range (4):
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

    

  
