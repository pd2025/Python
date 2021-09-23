# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:02:31 2020

@author: Indu
"""


import turtle
import math

bob = turtle.Turtle()

def square(t, length):
    for i in range (4):
        t.fd(length)
        t.lt(90)

#square(bob, 1)

def polygon(t, length, n):
    for i in range (int(n)):
        t.fd(length)
        t.lt(360/n)

        
polygon(bob, 6, 100)

def circle(t, r):
    for i in range(50):
        dist = 2 * math.pi * r
        t.fd(dist / 50)
        t.lt(360/50)
        
#circle (bob, 25)

def circle2(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon (t, length, n)
        
#circle2(bob, 50)

def circle3(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference/3) + 3
    length = circumference / n
    polygon (t, length, n)
       
#circle3 (bob, 70)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc (bob, 10, 90)