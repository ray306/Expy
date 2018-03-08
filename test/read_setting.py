# coding:utf-8
##### package test #####
import sys
sys.path = ['../']+sys.path
################

from expy import *  # Import the needed functions

start()  # Calling start() will do the readSetting() implicitly
# readSetting() # Or you can directly load setting from "setting.txt"

'Using "shared.setting" dictionary to get the pre-defined value'
print(shared.setting['background_color'])  # Print the setting of 'background_color' part
print(shared.setting['timing_set'])  # Print the setting of 'timing_set' part

'Calling "timing" function to get a certain time value'
print(timing('ITI'))  # Print 'ITI' value (we specify 500 for it in "setting.txt")
# Print 'fix' value (we specify 800~1400 range for it in "setting.txt")
print(timing('fix'))
# Print 'fix' value (we specify 800~1400 range for it in "setting.txt")
print(timing('fix'))
