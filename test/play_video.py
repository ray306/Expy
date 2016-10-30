# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start() # Initiate the experiment environment

video = loadVideo('data/demo.mpg')
playVideo(video, pauseKey={})