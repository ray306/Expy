# coding:utf-8
##### package test #####
import sys
# sys.path.append('../../')
sys.path = ['../../']+sys.path
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

def trial(word, pos):
    drawText(word, x=pos)  # Draw text on the canvas and display it

    key, rt = waitForResponse({key_.F: 'Left', key_.J: 'Right'}) # Waiting for pressing 'F' or 'J'
    if key == word:
        alertAndGo('Correct!', 1000)  # Display something in 1s
    else:
        alertAndGo('Wrong!', 1000)

    show(500)  # Pause (Keep displaying in 500ms)


instruction(shared.setting['instruction1'])
alertAndGo('The experiment will start after 3s.') # Display something in 3s(default)

stimuli = [('Left', -0.5), ('Right', 0.5), ('Right', -0.5),
           ('Left', 0.5), ('Left', -0.5), ('Right', -0.5)]

for word, pos in stimuli:
    trial(word, pos)  # Call the trial function with different parameters

alertAndQuit('Done!')  # Display something in 3s(default), and quit the program
