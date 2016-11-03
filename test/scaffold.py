# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start() # Initiate the experiment environment

something = getInput('enter something:') # Get user input until "ENTER", then give it to a varible

instruction(['page1>','page2>','page3\npage3']) # Show the information of experiment

tip('Show something until press SPACE or RETURN') # Show something until "SPACE" or "RETURN"

restTime() # Suspend the experiment and ask participant to rest, until "SPACE" or "RETURN"

alertAndGo('Show something for 3000ms',3000) # Show something during a given time, and continue

alertAndQuit('Show something for 3000ms, and quit')# Show something during a given time, and quit the program

