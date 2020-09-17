import turtle
import numpy as np
turtle.shape('turtle')
turtle.speed(0)
def strmm(n):
    
    fi=0
    dh=0
    k=1
   
    dl=0
    dfi=np.pi/180
    for i in range(n):
        fi+=dfi
        dl=k*dfi*np.sqrt(1+fi**2)
        turtle.forward(dl)
        turtle.right(dfi*180/np.pi)
strmm(10000)        
    