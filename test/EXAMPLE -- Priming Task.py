# coding:utf-8
##### package test #####
import sys
sys.path = ['../']+sys.path
################

from expy import *
start()

def trial(data):
    drawText('+')
    show(0.15)

    drawText(data['prime'])
    show(0.15)

    clear()
    show(0.25)

    drawText(data['target'])
    k,rt = waitForResponse({key_.F:'nonword', key_.J:'word'})

    clear()
    show(1)

    return k,rt

normalProcedure(trial_func=trial,
                trial_list='trial_list2.csv',
                instruction_setting='instruction3')

# def block(blockID):
#     stimuli = readStimuli('trial_list.csv', query='block==%s' %(blockID))
    
#     alertAndGo('实验将在3秒后开始')

#     result = []
#     for t in stimuli:
#         result.append(trial(t))

#     saveResult(result, stim=stimuli)

#     if blockID<2:
#         restTime()

# getSubjectID('请输入实验序号：')

# instruction(shared.setting['instruction3'])

# for blockID in range(2):
#     block(blockID+1)

# alertAndQuit('实验结束~ 谢谢参与我们的实验!')