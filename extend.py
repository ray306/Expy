import numpy as np
from expy import *

def setting(name):
    if name in shared.setting:
        return shared.setting[name]
    else:
        return None

def timing(name):
    val = shared.timing[name]
    if type(val) == int:
        return val
    else:
        return np.random.randint(val[0],val[1])

def session(stim_list, blockFunc):
    for blockID in range(shared.startBlockID,shared.blockCount+1):
        blockData = readStimuli(stim_list, blockID=('block',blockID))
        blockFunc(blockID, blockData)
        if blockID < shared.blockCount:
            restTime()  
        break