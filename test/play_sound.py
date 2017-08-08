# coding:utf-8
##### package test #####
import sys
sys.path = ['../../']+sys.path
################

from expy import *  # Import the needed functions
start(sample_rate=44100)  # Initiate the experiment environment

'''General usage'''
sound = loadSound('data/demo.WAV')  # Load the wav file
playSound(sound)  # Play the wav file
''''''

# Load many wav files and concat them
sound = loadManySound('data', ['ba','da','ba','da'], 'wav')
playSound(sound)

# Play multiple soundtrack at the same time
sound = loadManySound('data', ['demo','demo','demo','demo'], 'wav')
playSound(sound, busy=False)  # Play the wav file
sound = loadManySound('data', ['ba','da','ba','da'], 'wav')
playSound(sound, busy=False)
show(5)

# sound = makeSound(data)
# playSound(sound)
# show(1)

sound = makeBeep(440, 0.5)
playSound(sound)

sound = makeNoise(3)
playSound(sound)

sound = loadSound('data/demo.WAV')  # Load the wav file
sound = changeOnTracks(sound,changeVolume,[0.1,1]) # Change the volume of different tracks 
playSound(sound)  # Play the wav file
show(0.5)  # Pause (Keep displaying in 0.5s)

# s = makeBeep(440, 15)
s = loadManySound('data', ['ba','da','ba','da'], 'wav')
index = playAlterableSound(s,effect=changePitch)
print('The change is', index)



