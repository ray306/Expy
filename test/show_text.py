# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start() # Initiate the experiment environment

drawWord('Hello world!') # Draw text on the canvas
show(3000) # Display current canvas

drawWord('Hello world!', x=0.5, y=0.0)
show(3000) # Display current canvas

drawText('Hello\nworld\n!') # Draw text on the canvas
show(3000) # Display current canvas

textSlide('Hello\nworld\nagain!') # Display some text directly