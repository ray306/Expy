# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

# Draw a circle on the canvas
drawCircle(60, fill=False)
show(3000)  # Display current canvas

# Draw a rect on the canvas
drawRect(200, 100)
show(3000)  # Display current canvas

x, y = shared.winWidth // 2, shared.winHeight // 2  # calculate the screen center
# Draw lines on the canvas
drawLine([(x - 100, y - 100), (x, y), (x + 100, y - 100)])
show(3000)  # Display current canvas
