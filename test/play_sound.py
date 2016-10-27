# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start(sample_rate = 11025) # Initiate the experiment environment

sound = loadSound('data/demo.WAV')
playSound(sound)
show(3000)

sound = loadManySound('data',['demo','demo','demo'])
playSound(sound)