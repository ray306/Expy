# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

for w in 'ABCDE12345':
    drawText(w)  # Draw something on the canvas(not the screen)
    show(200)  # Display current canvas on the screen, and keep for 200ms
