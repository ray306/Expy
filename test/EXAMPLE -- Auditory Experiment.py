# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start() # Initiate the experiment environment

name = getInput('Please enter your name:')
introduction(setting('introduction2'))
tip(name+', Are you ready?')

def trial(stim):
    sound = loadSound('data/'+stim+'.WAV')
    playSound(sound)

    textSlide('Please press F for "ba", or press J for "da"')
    key = waitForEvent({K_f:'ba',K_j:'da'}) # Waiting for pressing 'F' or 'J'

    if key==stim:
        alertAndGo('Correct!',1000)
    else:
        alertAndGo('Wrong!',1000)

    show(500)

alertAndGo('The experiment will start after 3s.')
for stim in ['ba','da','da','ba']:
    trial(stim)

alertAndQuit('Done!')