# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

drawText('Hello', display=False)  # Draw text on the canvas
s1 = getScreen()  # Get current canvas, then clean the canvas

drawText('world', display=False)  # Draw text on the canvas
s2 = getScreen(clean_screen=False)  # Get current canvas, and keep it

drawText('........', display=False)  # Draw text on the canvas
s3 = getScreen()  # Get current canvas, then clean the canvas

show(3000, backup=s1)  # Display backup canvas
show(3000, backup=s2)  # Display backup canvas
show(3000, backup=s3)  # Display backup canvas
