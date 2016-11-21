# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

noise_level = environmentNoise(0.5)  # Detect the noise level of environment

'Without file'
textSlide('Recording：')
sample_width, sound = recordSound(noise_level, recording_min=2, sounding_max=0.7)
textSlide('Playing：')
playSound(sound)

'With file'
textSlide('Recording to file：')
recordSoundTofile('record', noise_level=noise_level, recording_min=2, sounding_max=0.7)

record = loadSound('data/record.WAV')
textSlide('Playing from file：')
playSound(record)
