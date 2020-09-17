import turtle
import numpy as np
turtle.shape('turtle')
def strmm(n):
    i=0
    n=200
    for i in range(n):
        turtle.forward(2)
        turtle.right(360/n)
for j in range(3):
    strmm(200)
    turtle.right(180)
    strmm(200)
    turtle.right(60)