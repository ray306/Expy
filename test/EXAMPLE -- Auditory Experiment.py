# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start() # Initiate the experiment environment

introduction(setting('introduction2'))
# tip('Are you ready?')

def trial(stim):
    sound = loadSound('data/'+stim+'.WAV') # Load the wav file
    playSound(sound) # Play the wav file

    textSlide('Please press F for "ba", or press J for "da"')
    key = waitForEvent({K_f:'ba',K_j:'da'}) # Waiting for pressing 'F' or 'J'

    if key==stim:
        alertAndGo('Correct!',1000) # Display something in 1s
    else:
        alertAndGo('Wrong!',1000)

    show(500) # Pause (show a screen during 500ms)

alertAndGo('The experiment will start after 3s.') # Display something in 3s(default)
for stim in ['ba','da','da','ba']:
    trial(stim) # Call the trial function with different parameters

alertAndQuit('Done!') # Display something in 3s(default), and quit the program