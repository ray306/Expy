# coding:utf-8
##### package test #####
import sys
# sys.path.append('../../')
sys.path = ['../../']+sys.path
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

# Get user input until "ENTER" pressed, then give it to a variable
something = getInput('enter something:')

# Show something until "RETURN" pressed
alert('You just entered "%s".\nPlease press RETURN to continue.' %something)

# Show the instruction of experiment
instruction(['This is the first page of instruction>', 'second page>', 'last page\nPress SPACE to quit the instruction'])

# Suspend the experiment and ask participant to rest, until "SPACE" pressed
restTime()

# Show something during a limited period, and continue
alertAndGo('Show something for 3s', 3)

# Show something during a limited period, and quit the program
alertAndQuit('Show something for 3s, and quit')