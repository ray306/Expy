# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions

start()  # Calling start() will do the readSetting() implicitly
# readSetting() # Or you can directly load setting from "setting.txt"

'Using "shared.setting" dictionary to get the pre-defined value'
print(shared.setting['backgroundColor']) # Print the setting of 'backgroundColor' part 
print(shared.setting['timingSet']) # Print the setting of 'timingSet' part 

'Calling "timing" function to get a certain time value'
print(timing('ITI')) # Print 'ITI' value (we specify 500 for it in "setting.txt")
print(timing('fix')) # Print 'fix' value (we specify 800~1400 range for it in "setting.txt")
print(timing('fix')) # Print 'fix' value (we specify 800~1400 range for it in "setting.txt")


