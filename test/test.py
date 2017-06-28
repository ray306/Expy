# coding:utf-8
##### package test #####
import sys
# sys.path.append('../../')
sys.path = ['../../']+sys.path
################

from expy import *  # Import the needed functions
start(sample_rate=44100)  # Initiate the experiment environment

# sounds = []
# for i in range(500,1000):
#     sounds.append(makeBeep(i, 0.05))

# original = 250
# def func(a):
#     global original
#     playSound(sounds[original])
    
#     original+=1

# while 1:
#     waitForResponse({key_.LEFT: 0, key_.RIGHT: 1}, action_while_pressing=(func,None))
#     key,rt = waitForResponse({key_.LEFT: 0, key_.RIGHT: 1}, out_time=10) 
#     # if key == 0:
#     #     original += 10
#     # elif key == 1:
#     #     original -= 10
#     # playSound(sounds[original])
