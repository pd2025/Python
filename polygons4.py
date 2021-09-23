# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:31:51 2020

@author: Indu
"""
import turtle
import math

bob = turtle.Turtle

def polygon_test(t, n, length):
    angle = 360 / n
    d = 2 * length * 2 * length
    t.fd(length)
    t.lt(angle * 3)
    t.fd(d)
    
polygon_test(bob, 8, 100)