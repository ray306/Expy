# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

# Get user input until "ENTER" pressed, then give it to a variable
something = getInput('enter something:')

# Show the instruction of experiment
instruction(['page1>', 'page2>', 'page3\npage3'])

# Show something until "SPACE" or "RETURN" pressed
tip('Show something until press SPACE or RETURN')

# Suspend the experiment and ask participant to rest, until "SPACE" or "RETURN" pressed
restTime()  

# Show something during a limited period, and continue
alertAndGo('Show something for 3000ms', 3000)

# Show something during a limited period, and quit the program
alertAndQuit('Show something for 3000ms, and quit')
