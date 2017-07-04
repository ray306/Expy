# coding:utf-8
from expy import *
np = shared.np

'"Extend.py" is a play for any kind of plugin function'

def session(block_count, stim_list, block_func):
    for block_id in range(shared.start_block, block_count + 1):
        block_data = readStimuli(stim_list, block_id=('block', block_id))
        block_func(block_id, block_data)
        if block_id < block_count:
            restTime()
        break
