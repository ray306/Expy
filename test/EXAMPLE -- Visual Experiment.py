# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start() # Initiate the experiment environment

# name = getInput('Please enter your name:')
introduction(setting('introduction1'))

def trial(word,pos):
    drawWord('+')
    show(500)

    drawWord(word,x=pos) # Draw text on the canvas
    show()
    key = waitForEvent({K_f:'Left',K_j:'Right'}) # Waiting for pressing 'F' or 'J'
    if key==word:
        alertAndGo('Correct!',1000)
    else:
        alertAndGo('Wrong!',1000)
    show(500)

alertAndGo('The experiment will start after 3s.')
stimuli = [('Left',-0.5),
            ('Right',0.5),
            ('Right',-0.5),
            ('Left',0.5),
            ('Left',-0.5),
            ('Right',-0.5)]
for word,pos in stimuli:
    trial(word,pos)

alertAndQuit('Done!')