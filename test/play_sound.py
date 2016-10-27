# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start(sample_rate = 11025) # Initiate the experiment environment

sound = loadSound('data/demo.WAV') # Load the wav file
playSound(sound) # Play the wav file
show(3000) # Pause (show a screen during 3000ms)

sound = loadManySound('data',['demo','demo','demo']) # Load many wav files and concat them
playSound(sound)