import turtle
turtle.shape('turtle')

def proper_polygon(N,L):
    for step in range(N):
        turtle.forward(L)
        turtle.left(360/N)

N= 3
L= 10

for x in range (10):
    proper_polygon(N,L)
    turtle.penup()
    turtle.right(360/N+180*(N-2)/(2*N))
    turtle.forward(10)
    turtle.left(360/(N+1)+180*(N-2)/(2*N))
    turtle.pendown()
    N=N+1
    L=L+10
    


    
