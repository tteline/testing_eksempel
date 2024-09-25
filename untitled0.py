# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:11:29 2024

@author: Teline
"""

import turtle
t = turtle.Turtle()
t.left(45)

ant = 5
#int(input("hvor mange diamanter? "))
lengd = 100

for i in range (ant):
    lengd += 30
    t.penup()
    t.left(135)
    t.forward(20)
    t.right(135)
    t.pendown()
    for i in range (4):
        t.forward(lengd)
        t.right(90)


turtle.done()