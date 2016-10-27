# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start() # Initiate the experiment environment

drawCircle(60, fill=False) # Draw a circle on the canvas
show(3000) # Display current canvas

drawRect(200,100) # Draw a rect on the canvas
show(3000) # Display current canvas

x,y = shared.winWidth//2, shared.winHeight//2 # calculate the screen center
drawLine([(x-100,y-100), (x,y), (x+100,y-100)]) # Draw lines on the canvas
show(3000) # Display current canvas