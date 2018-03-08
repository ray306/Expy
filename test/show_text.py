# coding:utf-8
##### package test #####
import sys
sys.path = ['../']+sys.path
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

'''General usage'''
# Draw text on the canvas
drawText('Hello world!')
show(2)  # Display current canvas
''''''

# Draw text on the canvas
w, h = drawText('Hello world!', show_now=False)
drawRect(w, h, color=C_red, fill=False, show_now=False)
show(2)  # Display current canvas

# Draw text on the canvas, with left center's position
drawText('Hello! world!', anchor_x='left', anchor_y='bottom')
show(2)  # Display current canvas

# Draw text on the canvas, with given fontsize
drawText('Hello world!', size=50)
show(2)  # Display current canvas

# Draw text on the canvas, with given font color
drawText('Hello world!', color=C_red)
show(2)  # Display current canvas

# # Draw text on the canvas, with given angle
# drawText('Hello world!', rotation=45)
# show(2)  # Display current canvas

# Draw text on the canvas, with center's position
drawText('Hello! world!', x=-0.5, y=0.0)
show(2)  # Display current canvas

drawText('Hello\nworld\n!')  # Draw multi-line text on the canvas
show(2)  # Display current canvas

# Display text on a new slide, it's functionally equals to clear+drawText+show,
textSlide('Hello\nworld\nagain!')
