import turtle
import numpy as np
turtle.shape('turtle')
turtle.speed(0)
def strmm(n, k):
    n = 200
    for i in range(n):
        turtle.forward(k)
        turtle.right(360/n)
def stlmm(n, k):
    n = 200
    for i in range(n):
        turtle.forward(k)
        turtle.left(360/n)
k = 2
turtle.right(90)
for j in range(10):
    strmm(200, k)
    stlmm(200, k)
    k += 0.1