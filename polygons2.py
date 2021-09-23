# -*- coding: utf-8 -*-
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
        d = math.sqt(2 * length)
        t.fd(length)
        t.lt(angle * 2)
        t.fd(d)
        

def any_polygon(t, n, length):
    """this function is like polyline, except you don't
    have to enter the angle. It calculates the angle by
    dividing 360 by the number of sides, or line segments)."""
    for i in range(n / 2):
        angle = 360 / n
        d = math.sqt(2 * length)
        t.fd(length)
        t.lt(angle / 2 + angle)
        t.fd(d)
        t.rt(angle / 2 + angle)
any_polygon(bob, 4, 100)
        