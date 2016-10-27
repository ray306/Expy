# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start() # Initiate the experiment environment

drawWord('Hello') # Draw text on the canvas
s1 = getScreen() # Get current canvas, then clean the canvas

drawWord('world') # Draw text on the canvas
s2 = getScreen(cleanScreen=False) # Get current canvas, and keep it

drawWord('........') # Draw text on the canvas
s3 = getScreen() # Get current canvas, then clean the canvas

show(3000,backup=s1) # Display backup canvas
show(3000,backup=s2) # Display backup canvas
show(3000,backup=s3) # Display backup canvas