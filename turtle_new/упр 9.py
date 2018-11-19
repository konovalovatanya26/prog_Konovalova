import turtle
turtle.shape('turtle')


Number = 3
Length = 50
x = 0
y = 0
k = 3

for _ in range (11):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(k):
       turtal.forward(Length)
       turtal.left(360/Number)
     Number += 1
     Length += 20
     x -= 10
     y -= 7
     k +=1
    
    
    

    
