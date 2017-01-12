# from pygame.locals import *
import pyglet.window.key as key_

from expy import shared
from .colors import *
from .stim.draw import *

def setKeyMapping(allowed_keys):
    '''
    Make a list and a mapping of allowable key(s)
    
    Parameters
    ----------
    allowed_keys：None(default), Keyname, list, or dict
        The allowed key(s).
        You can leave nothing, 
                a Keyname (eg. key_.F), 
                a list of Keyname (eg. [key_.F,key_.J]), 
                or a dict of Keyname (eg. [key_.F:'F',key_.J:'J']) here.
        You could look into the Keyname you want in http://expy.readthedocs.io/en/latest/keymap/

    Returns
    -------
    keys: list
        A list of the allowed Keyname(s)
    mapping: dict
        A dictionary of the allowed Keyname(s) and their correspending value
    '''
    keys = allowed_keys
    mapping = allowed_keys

    if type(allowed_keys) == dict:  # eg. allowed_keys = {key_.F: 'T', key_.J: 'F'}
        keys = list(allowed_keys.keys())
    elif type(allowed_keys) == list:  # eg. allowed_keys = [key_.F, key_.J]
        mapping = {k: k for k in allowed_keys}
    elif type(allowed_keys) == int:  # eg. allowed_keys = key_.ENTER
        keys = [allowed_keys]
        mapping = {allowed_keys: allowed_keys}

    return keys, mapping


def suspend():
    '''
    Suspend the program and display "[程序暂停中/Pause]"

    Parameters
    ----------

    Returns
    -------
    past time: int
        The millisecond count since the function starts.
    '''
    onset = shared.time.time()
    screenshot = shared.pyglet.image.get_buffer_manager().get_color_buffer().get_image_data()
    shared.win.clear()

    drawText('[程序暂停中/Pause]')

    waitForResponse(key_.F12, suspending=True)

    screenshot.blit(0,0,0)
    shared.win.flip()

    return shared.time.time() - onset

def waitForResponse(allowed_keys=[], out_time=0, has_RT=True, suspending=False):
    '''
    Waiting for a allowed keypress event during a limited period
    (Press F12 would suspend the procedure and press ESC would end the program)

    Parameters
    ----------
    allowed_keys：None(default), Keyname, list, or dict
        The allowed key(s).
        You can leave nothing, 
                a Keyname (eg. key_.F), 
                a list of Keyname (eg. [key_.F,key_.J]), 
                or a dict of Keyname (eg. [key_.F:'F',key_.J:'J']) here.
        You could look into the Keyname you want in http://expy.readthedocs.io/en/latest/keymap/
    out_time：int(>0), 0(default)
        The time limit of current function. While the past time exceeds the limitation, the function terminates.
    has_RT：True(default), False
        Return a past time or not
    suspending: True, False(default)
        Label the suspend state. If true, the F12 wouldn't suspend the program.

    Returns
    -------
    KEY: None, int, or defined value
        1. If allowed_keys is None, return the id of any pressed key
        2. If allowed_keys is a List (eg. [key_.F,key_.J]), return the id of allowed pressed key
        3. If allowed_keys is a Dict (eg. [key_.F:'F',key_.J:'J']), return the value of allowed pressed key
        4. Return None if the time is out and no allowed keypress
    (Only if has_RT is True) past_time: int
        The millisecond count since the function starts.
    '''
    def wait(start_tp, out_time):
        while True:
            shared.win.dispatch_events()

            past_time = shared.time.time() - start_tp
            if out_time > 0 and past_time >= out_time:
                return 'None', 'None'

            for e in shared.events:
                if e['type']=='key_press':
                    return e['key'], int((e['time']- start_tp)*1000)
                # elif e['type'] in other_events:
                #     return e['type'], int((e['time']- start_tp)*1000)
                # mouse_press

            shared.time.sleep(0.001)

    now = shared.time.time()
    if not shared.start_tp:
        shared.start_tp = now
        
    shared.events = []
    shared.allowed_keys, shared.allowed_keys_mapping = setKeyMapping(allowed_keys)  # Mapping allowable key(s)
    
    ev, past_time = wait(shared.start_tp, out_time/1000)

    shared.events = []
    shared.start_tp = None
    if has_RT:
        return ev, past_time
    else:
        return ev
