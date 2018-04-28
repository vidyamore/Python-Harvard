
# coding: utf-8

# In[1]:

# Spiral
# 
#Draws an Archimedian spiral starting at the origin.
# From the book:
# Think Python: An Introduction to Software Design by Allen B. Downey
#http://www.greenteapress.com/thinkpython/code/spiral.py
# This code has been changed from the above source 
#
# modified by: Vidya More
# July 15 , 2017
#
# An Archimedean Spiral is a curve defined by a polar equation
# of the form r = θa

import math
import turtle
def draw_spiral(t, n, length=5, a=0.1, b=0.0002):
    """Draws an Archimedian spiral starting at the origin.

    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)

    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta

def make_turtle(color, size, shape):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.shape(shape)
    t.speed(0)
    return t

# create the  bob
bob = make_turtle("blue",3, "turtle")

# Draws an Archimedian spiral starting at the origin.
draw_spiral(bob, n=500)

turtle.mainloop()
turtle.done()

wait_for_user()


# In[ ]:



