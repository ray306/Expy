# coding:utf-8
from expy import *
np = shared.np

'"Extend.py" is a play for any kind of plugin function'

def normalProcedure(trial_func, trial_list='trial_list.csv',  practice_list=None, practice_func=None, onset_block=1, instruction_setting='instruction'):
    '''
    General framework of experiment procedure.

    Parameters
    ----------
    trial_func: method name
        Name of trial method
    trial_list: str (default: 'trial_list.csv')
        Name of trial list
    practice_list: str, or None (default)
        Name of practice trial list
    onset_block: int (default: 1)
        Number of onset block
    instruction_setting: str (default: 'instruction'), or None
        Name of instruction in the setting file

    Returns
    -------
    None
    '''

    # Preload file of stimuli and then process it
    pre_load_file = readStimuli(trial_list, return_list=False)
    if 'block' in pre_load_file.columns:
        shared.blockCount = pre_load_file.block.iloc[-1]
        single_block=False
    else:
        shared.blockCount = 1
        single_block=True

    # Experiment start
    getSubjectID(shared.setting['subject_name_query'])
    instruction(shared.setting[instruction_setting])

    # Practice stage
    if practice_list:
        if not practice_func:
            practice_func = trial_func
        stimuli = readStimuli(practice_list)
        for data in stimuli:
            practice_func(data)

    # Regular stage
    def block(blockID):
        if single_block:
            stimuli = readStimuli(trial_list)
        else:
            stimuli = readStimuli(trial_list, query='block==%s' %blockID)                

        alertAndGo(shared.setting['block_start'])
        
        result = [trial_func(data) for data in stimuli]

        saveResult(result, blockID, columns=['respKey','RT'], stim=stimuli)

        if blockID < shared.blockCount:
            restTime()  

    for blockID in range(onset_block, shared.blockCount+1):
        block(blockID)

    # Experiment end
    alertAndQuit(shared.setting['experiment_end'])
