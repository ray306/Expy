# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

'''General usage'''
# Draw a picture on the canvas center
drawPic('data/demo.jpg')
show(3000)  # Display current canvas
''''''

# Draw a zoomed picture on the canvas center
drawPic('data/demo.jpg', w=400, h=300)
show(3000)  # Display current canvas

# # Draw a zoomed picture on the canvas center
# drawPic('data/demo.jpg', w=300, h=400, rotate=90)
# show(3000)  # Display current canvas

# Draw a zoomed picture on the canvas, and move it
drawPic('data/demo.jpg', w=400, h=300, x=0.5, y=0.5)
show(3000)  # Display current canvas

# Draw a zoomed picture on the canvas, and move it
drawPic('data/demo.jpg', w=400, h=300, x=0.5, y=0.5, anchor_x='left',anchor_y='center')
show(3000)  # Display current canvas
