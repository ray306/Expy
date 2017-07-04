# coding:utf-8
##### package test #####
import sys
# sys.path.append('../../')
sys.path = ['../../']+sys.path
################

from expy import *  # Import the needed functions

'List the filenames of a dir'
filelist = readDir('data', shuffle=True)
print(filelist)

'Get stimuli from csv or xlsx'
stim = 'data/trial_list.csv'
alldata = readStimuli(stim)
block2 = readStimuli(stim, query='block==2')

print('alldata:\n', alldata)
print('block2:\n', block2)

'Save result'
saveResult(resp=[1, 2, 3, 4], block_tag=1, columns=['resp'])
saveResult(resp=[1, 2, 3, 4], block_tag=2 columns=['resp'], stim=block2)
saveResult(resp=[(1, 0), (2, 0), (3, 0), (4, 0)], block_tag=3, columns=[
           'resp1', 'resp2'], stim=block2)
