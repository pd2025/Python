# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:58:58 2020

@author: Indu
"""


import turtle
import math

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
        
angle = 0

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t = Turtle (bob)
    r = radius (1/2 of the diameter)
    angle = angle of the arc
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)
    
def petal(t, r, angle):
    for i in range (2):
        arc (t, r, angle)
        t.lt(180-angle)
    
def Flower(t, n, r, angle):
    """ t = turtle (bob)
    n = # of petals
    r = radius
    angle = angle of the arc
    """
    for i in range (n):
        petal(t, r, angle)
        t.lt(360/n)

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()

move(bob, 100)    
Flower(bob, 20, 60.0, 60.0)
