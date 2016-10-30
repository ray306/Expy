import numpy as np
from expy import *

'"Extend.py" is a play for any kind of plugin function'

def session(stim_list, blockFunc):
    for blockID in range(shared.startBlockID,shared.blockCount+1):
        blockData = readStimuli(stim_list, blockID=('block',blockID))
        blockFunc(blockID, blockData)
        if blockID < shared.blockCount:
            restTime()  
        break