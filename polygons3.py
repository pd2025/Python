"""
Created on Thu Apr  2 10:59:03 2020

@author: Indu
"""

import math
import turtle

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    """Draws n line segments.
     angle = degrees between line segments (interior angle)
    t = turtle (bob, in this case)
    n = # of line segments
    length = length of each line segment
   
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        

def any_polygon(t, n, length):
    """this function is like polyline, except you don't
    have to enter the angle. It calculates the angle by
    dividing 360 by the number of sides, or line segments)."""
    for i in range(n):
        angle = 360 / n
        d = length * (0.1 * math.sqrt(2 * length))
        t.rt(angle * 1.5)
        t.fd(d)
        t.rt(angle * 1.5)
        t.fd(length)

any_polygon(bob, 6, 100)
        