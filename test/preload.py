# coding:utf-8
##### package test #####
import sys
sys.path = ['../']+sys.path
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

drawText('Hello', show_now=False)  # Draw text on the canvas
s1 = getScreen()  # Get current canvas, then clean the canvas

drawText('world', show_now=False)  # Draw text on the canvas
s2 = getScreen(clean_screen=False)  # Get current canvas, and keep it

drawText('........', show_now=False)  # Draw text on the canvas
s3 = getScreen()  # Get current canvas, then clean the canvas

show(3, backup=s1)  # Display backup canvas
show(3, backup=s2)  # Display backup canvas
show(3, backup=s3)  # Display backup canvas
