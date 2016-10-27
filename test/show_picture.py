# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start() # Initiate the experiment environment

drawPic('data/demo.jpg') # Draw a picture on the canvas center
show(3000) # Display current canvas

drawPic('data/demo.jpg', w=400, h=300) # Draw a zoomed picture on the canvas center
show(3000) # Display current canvas

drawPic('data/demo.jpg', w=400, h=300, x=0.5, y=0.5) # Draw a zoomed picture on the canvas, and move it
show(3000) # Display current canvas