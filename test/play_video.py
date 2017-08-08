# coding:utf-8
##### package test #####
import sys
sys.path = ['../../']+sys.path
################

from expy import *  # Import the needed functions
start(fullscreen=False)  # Initiate the experiment environment

video = loadVideo('data/demo.mpg')
playVideo(video)
