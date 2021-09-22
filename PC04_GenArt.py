#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:34:40 2021

@author: katiehaley
"""

import random, turtle
turtle.colormode(255)
#startcode

panel = turtle.Screen()
w = 750
h = 750
panel.setup(width=w, height=h)

#define two diferent turtles
clouds = turtle.Turtle() #the turtle that will make the clouds
flower1 = turtle.Turtle() #the turtle that will make the flowers

clouds.speed(10) # draw at the fastest speed

turtle.bgcolor(135,206,250) #light blue
turtle.up()

clouds.penup()
clouds.color(255, 255, 255) #white

for k in range(4):#nested for loop creating four different clouds w/ four circles in each
    clouds.goto(random.randint(-350,350), random.randint(100,350)) #random spots in sky within those x and y values
    for i in range(4): #actually making the circles that form the clouds
        #drawing clouds
        clouds.pendown()
        clouds.fillcolor(255, 255, 255)
        clouds.begin_fill()
        clouds.circle(60)
        clouds.end_fill()
        clouds.penup()
        clouds.setheading(random.randint(-45,45)) #make cloud shape
        clouds.forward(10)
    
myListCoordinates = [(-300,-350),(-100,-350),(0,-350), (150,-350),(255,-350)]
 #the spot where stem should start drawing
flower1.width(10) #for stems

flower1.penup()
flower1.left(90) #have to turn the pen left 90 to make it face upwards

for s in range(4): #drawing stems in random spots
    flower1.color("green")
    flower1.goto(random.choice(myListCoordinates)) #to make random spots for the stems
    flower1.pendown()
    flower1.forward(300)
    flower1.penup()

inc = 50 # angle increment between shapes in pattern
numIt = int(360/inc) # the number of iterations to make a complete circle. 
innerCirc = 25 # radius of inner circle
radius = 15 # radius of circles drawn in pattern

myListFlowerCoordinates = [(-320,-50),(-120,-50),(-20,-50), (130,-50),(235,-50)] 
#where flowers will start drawing
turtle.width(5)
colors = ["yellow", "pink", "purple", "salmon", "darkorchid4", "thistle"]
#set the colors the turtle will pick from to draw flowers 

for k in range(4): #nested for loop that will draw the flowers in different spots
    flower1.penup()
    flower1.goto(random.choice(myListFlowerCoordinates)) #to make random spots for flowers 
    flower1.pencolor(random.choice(colors)) #flowers will be random colors each time
    for iteration in range(numIt): #drawing a singal flower
        # for loop creates a ring of overlapping circles--a spirograph!
        flower1.pendown()
        flower1.circle(radius)
        flower1.forward(innerCirc)
        flower1.right(inc)
    
turtle.done()