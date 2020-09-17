import turtle
import numpy as np
turtle.shape('turtle')
turtle.speed(0)
def strmm(N):
    n = 200
    k = 2
    l = 0.3
    turtle.right(90)
    for j in range(N):
        for i in range(n//2):
            turtle.forward(k)
            turtle.right(360/n)
        for i in range(n//2):
            turtle.forward(l)
            turtle.right(360/n)
strmm(10)
