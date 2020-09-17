import turtle
turtle.shape('turtle')
turtle.speed()
def strmm(n, k):
    for i in range(n):
        turtle.pendown()
        for j in range(4):
            turtle.forward(k)
            turtle.right(90)
        turtle.penup()
        turtle.left(135)
        turtle.forward(5*2**0.5)
        turtle.right(135)
        k+=10
#    return(n, k)


strmm(10, 20)
