# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################


from expy import * # Import the needed functions
start() # Initiate the experiment environment

'''General usage'''
drawText('Hello world!') # Draw text on the canvas
show(3000) # Display current canvas
''''''


drawText('Hello world!', fontname='normalFont') # Draw text on the canvas, with given font(size)
show(3000) # Display current canvas

drawText('Hello! world!', x=-0.5,y=0.0) # Draw text on the canvas, with center's position
show(3000) # Display current canvas

drawText('Hello! world!', x=-0.5,y=0.0, benchmark='left_center') # Draw text on the canvas, with left center's position
show(3000) # Display current canvas

drawText('Hello\nworld\n!') # Draw multi-line text on the canvas
show(3000) # Display current canvas

textSlide('Hello\nworld\nagain!') # Display some text directly, it's functionally equals to clear+drawText+show, 