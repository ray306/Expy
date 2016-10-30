# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start(sample_rate = 44100) # Initiate the experiment environment

'''General usage'''
sound = loadSound('data/demo.wav') # Load the wav file
playSound(sound) # Play the wav file
''''''

show(1000) # Pause (show a screen during 3000ms)

sound = loadManySound('data',['ba','da'],'wav') # Load many wav files and concat them
playSound(sound)