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

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
angle = 0

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)
    
    
def Flowers(petals):
    for i in range (petals):
        angle1 = 90
        angle = angle1 * 1.5 #angle1 + angle1 / 2
        arc(bob, 100, angle1)
        bob.lt(angle)
      

Flowers(16)
