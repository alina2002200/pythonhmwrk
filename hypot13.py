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
def stpmm(n, k):
    n = 200
    for i in range(n//2):
        turtle.forward(k)
        turtle.left(360/n)
turtle.begin_fill()   
turtle.fillcolor('yellow')

strmm(200, 5)
turtle.end_fill()

turtle.right(70)
turtle.penup()
turtle.forward(100)
turtle.pendown()

turtle.begin_fill()   
turtle.fillcolor('blue')
stlmm(200, 1)
turtle.end_fill()

turtle.left(180)
turtle.penup()
turtle.forward(100)
turtle.left(70)
turtle.left(70)
turtle.forward(100)
turtle.pendown()

turtle.begin_fill()   
turtle.fillcolor('blue')
strmm(200, 1)
turtle.end_fill()

turtle.right(180)
turtle.penup()
turtle.forward(100)

turtle.right(160)
turtle.forward(150)
turtle.pendown()
turtle.width(10)
turtle.forward(75)
turtle.penup()

turtle.backward(55)
turtle.left(270)
turtle.forward(120)
turtle.pendown()

turtle.left(90)
turtle.pencolor('red')
stpmm(200, 4)


