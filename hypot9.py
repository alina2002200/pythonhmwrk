import turtle
import numpy as np
turtle.shape('turtle')
def strmm(n):
    R, a = 0, 0
    
    for i in range(3,n):
        R += 10
        a = 2*R*np.sin(np.pi/i)
        turtle.pendown()
        for j in range(i):
            turtle.forward(a)
            turtle.right(360/i)	
        turtle.penup()
        turtle.left(180-90*(i-2)/i)
        turtle.forward(10)
        turtle.right(180-90*(i-1)/(i+1))
strmm(10)