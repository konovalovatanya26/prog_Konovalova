import turtle
turtle.shape('turtle')

N=100
L=5


def circle(N,L):
    for step in range(N):
        turtle.forward(L)
        turtle.left(360/N)
    for step in range(N):
        turtle.forward(L)
        turtle.right(360/N)

for x in range(10):
    circle(N,L)
    N=N+10
    
