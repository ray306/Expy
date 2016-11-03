# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

instruction(shared.setting['instruction2'])
# tip('Are you ready?')


def trial(stim):
    sound = loadSound('data/' + stim + '.WAV')  # Load the wav file
    playSound(sound)  # Play the wav file

    textSlide('Please press F for "ba", or press J for "da"')
    # Waiting for pressing 'F' or 'J'
    key, rt = waitForResponse({K_f: 'ba', K_j: 'da'})

    if key == stim:
        alertAndGo('Correct!', 1000)  # Display something in 1s
    else:
        alertAndGo('Wrong!', 1000)

    show(500)  # Pause (show a screen during 500ms)

# Display something in 3s(default)
alertAndGo('The experiment will start after 3s.')
for stim in ['ba', 'da', 'da', 'ba']:
    trial(stim)  # Call the trial function with different parameters

alertAndQuit('Done!')  # Display something in 3s(default), and quit the program
