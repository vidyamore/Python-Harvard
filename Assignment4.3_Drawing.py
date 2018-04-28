
# coding: utf-8

# In[ ]:

# Creative drawing 
# 
# Make a creative drawing with the Python turtle library.
#
# This code has been changed from the below source
# From the book:
# Think Python: An Introduction to Software Design by Allen B. Downey
# http://www.greenteapress.com/thinkpython/code/flower.py
# and
# http://deborahrfowler.com/PythonResources/PythonTurtleExamples/TurtleSunflowers.py
# 
# modified by: Vidya More
# July 15 , 2017

import math
import turtle
def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """    
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def drawPetal(t, length, angle ):
    """Draws a single petals wihout arc.

    t: Turtle
    length: length of the edge of petal
    angle: angle (degrees) between 2 edges of petal
    """
    for i in range(6):
        t.fd(length)
        t.lt(180-angle)
        t.fd(length)
        t.lt(angle)
        t.fd(length)
        t.lt(180-angle)
        t.fd(length)
        t.lt(angle)
        t.rt(180-angle)

def make_turtle(color,fillcolor, size, shape):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(color,fillcolor)
    t.pensize(size)
    t.shape(shape)
    t.speed(0)
    return t

wn = turtle.Screen()
wn.bgcolor("brown")

bob = make_turtle("white", "blue",8, "circle")

# draw a sequence of three flowers, as shown in the book.
bob.begin_fill()
drawPetal(bob,150,120)
bob.end_fill()

tess = make_turtle("yellow", "red",8, "circle")
tess.begin_fill()
flower(tess, 12, 80.0, 120.0)
tess.begin_fill()

alex = make_turtle("red", "yellow",8, "circle")
alex.begin_fill()
flower(alex, 12, 140.0, 30.0)
alex.begin_fill()


turtle.mainloop()
turtle.done()
die(bob)

