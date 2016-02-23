#########################
# Written by: Ralf Frix #
# Date: February 4,2016 #
#########################
import pylab
import sys
import numpy as np

class Shapes:
    #Shapes constructor
    def __init__(self):
        pass

    #Draws a vertical line
    def drawALine(self):
        for i in range(20): 
            print "*",
        print 
        
    #Draws a rectangle
    def drawARectangle(self):
        for i in range(5):
            for j in range(20):
                print "*",
            print             

    #Draws a square            
    def drawASquare(self):
        for i in range(5):
            for j in range(0,20,4):
                print "*",
            print             

    #Draws a right triangle    
    def drawARightTriangle(self):
        for i in range(5):
            for j in range(i+1):
                print "*",
            print     
            
            
shapes = Shapes()
shapes.drawALine()
print "\n"
shapes.drawARectangle()
print "\n"
shapes.drawASquare()
print "\n"
shapes.drawARightTriangle()

x = np.linspace(0, 20, 1000)  # 100 evenly-spaced values from 0 to 50
y = np.sin(x)

pylab.plot(x, y)

