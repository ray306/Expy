# coding:utf-8
##### package test #####
import sys
sys.path = ['../']+sys.path
################

from expy import *  # Import the needed functions
start(background_color=C_green)  # Initiate the experiment environment

# Draw a rect on the canvas
drawRect(200, 100, color=C_red)
show(1.5)  # Display current canvas

# Draw a circle on the canvas
drawCircle(60, fill=False)
show(1.5)  # Display current canvas

x, y = shared.win_width // 2, shared.win_height // 2  # calculate the screen center
drawPoints([(x - 100, y - 100), (x+50, y), (x + 100, y - 100)], size=5)
show(1.5)

# Draw lines on the canvas
drawLines([(x - 100, y - 100), (x+50, y), (x + 100, y - 100)])
show(1.5)  # Display current canvas
