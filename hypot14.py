import turtle
import numpy as np
turtle.shape('turtle')

def strmm(n):
    for i in range(n):
        turtle.forward(150)
        turtle.right(180-180/n)
strmm(11)
