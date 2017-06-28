# coding:utf-8
##### package test #####
import sys
# sys.path.append('../../')
sys.path = ['../../']+sys.path
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

noise_level = environmentNoise(0.5)  # Detect the noise level of environment

'Without file'
textSlide('Recording: ')
sound = recordSound(noise_level, rec_length_min=2000, sound_length_max=4000)
textSlide('Playing: ')
playSound(sound)

'With file'
textSlide('Recording to file: ')
recordSound(noise_level, rec_length_min=2000, sound_length_max=4000, 
                                    path='data/record.WAV')
record = loadSound('data/record.WAV')
textSlide('Playing from file: ')
playSound(record)

