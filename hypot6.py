import turtle
turtle.shape('turtle')
def strmm(n, k):
    for i in range(n):
        turtle.pendown()
        turtle.forward(k)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(k)
        turtle.left(180+360/n)
    return(n)
strmm(12, 50)        