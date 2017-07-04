# coding:utf-8
##### package test #####
import sys
# sys.path.append('../../')
sys.path = ['../../']+sys.path
################

from expy import *  # Import the needed functions
start(sample_rate=44100)  # Initiate the experiment environment

'''General usage'''
sound = loadSound('data/demo.WAV')  # Load the wav file
playSound(sound)  # Play the wav file
''''''
show(0.5)  # Pause (Keep displaying in 0.5s)

# Load many wav files and concat them
sound = loadManySound('data', ['ba','da','ba','da'], 'wav')
playSound(sound, blocking=False)
show(0.5)

# sound = makeSound(data)
# playSound(sound)
# show(1)

sound = makeBeep(440, 0.5)
playSound(sound)

sound = makeNoise(1)
playSound(sound)

