# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

RATE = 44100
min_duration = 1 * RATE
max_duration = 2 * RATE
sample_duration = 0.5
noise_level = environment_noise(sample_duration)

'Without file'
textSlide('Recording：')
sample_width, sound = recordSound(noise_level, min_duration, max_duration)

textSlide('Playing：')
playSound(sound)

'With file'
textSlide('Recording to file：')
recordSound_tofile('data', 'record', noise_level, min_duration, max_duration)

record = loadSound('data/record.WAV')
textSlide('Playing from file：')
playSound(record)
