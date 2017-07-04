# coding:utf-8
import pyglet.window.key as key_

from expy import shared
from .colors import *
from .stim.draw import *

def setKeyMapping(allowed_keys):
    '''
    Make a list and a mapping of allowable key(s)
    
    Parameters
    ----------
    allowed_keys: None(default), Keyname, list, or dict
        The allowed key(s).
        You can leave nothing, 
                a Keyname (eg. key_.F), 
                a list of Keyname (eg. [key_.F,key_.J]), 
                or a dict of Keyname (eg. {key_.F:'F',key_.J:'J'}) here.
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

class ClickRange():
    def __init__(self, x, y, button):
        def toPixelRange(a, b, ref):
            if type(a) is float:
                a, b = (0.5 + a / 2) * ref, (0.5 + b / 2) * ref
                return range(int(a),int(b))
            elif type(a) is int:
                return range(a,b)
            else:
                raise Exception('Unsupported coordinate.')

        self.x = toPixelRange(x[0],x[1], shared.win_width)
        self.y = toPixelRange(y[0],y[1], shared.win_height)

        self.button = button

def setClickMapping(allowed_clicks):
    '''
    Make a list and a mapping of allowable mouse click(s)
    
    Parameters
    ----------
    allowed_clicks: None(default), ClickRange object, list, or dict
        The allowed mouse click event(s).
        You can leave nothing, 
                a ClickRange object (eg. C1), 
                a list of ClickRange object (eg. [C1, C2]), 
                or a dict of ClickRange object (eg. {C1:'F',C2:'J'}) here.

    Returns
    -------
    keys: list
        A list of the allowed mouse click(s)
    mapping: dict
        A dictionary of the allowed mouse click(s) and their correspending value
    '''
    keys = allowed_clicks
    mapping = allowed_clicks

    if type(allowed_clicks) == dict:  # eg. allowed_clicks = {key_.F: 'T', key_.J: 'F'}
        keys = list(allowed_clicks.keys())
    elif type(allowed_clicks) == list:  # eg. allowed_clicks = [key_.F, key_.J]
        mapping = {k: k for k in allowed_clicks}
    elif type(allowed_clicks) == ClickRange:  # eg. allowed_clicks = key_.ENTER
        keys = [allowed_clicks]
        mapping = {allowed_clicks: allowed_clicks}

    return keys, mapping


def suspend():
    '''
    Suspend the program and display "[程序暂停中/Pause]"

    Parameters
    ----------

    Returns
    -------
    past time: int
        The second count since the function starts.
    '''
    onset = shared.time.time()
    screenshot = shared.pyglet.image.get_buffer_manager().get_color_buffer().get_image_data()
    shared.win.clear()

    drawText('[程序暂停中/Pause]')

    waitForResponse(key_.F12, suspending=True)

    screenshot.blit(0,0,0)
    shared.win.flip()

    return shared.time.time() - onset

def wait(out_time):
    while True:
        shared.win.dispatch_events()
        past_time = shared.time.time() - shared.start_tp

        if out_time > 0 and past_time >= out_time:
            return 'None', 'None'
        for e in shared.events:
            if e['type']=='key_press':
                if (not shared.suspending) and e['key'] == key_.F12:
                    shared.events = []
                    break
                return e['key'], e['time']- shared.start_tp
            elif e['type']=='mouse_press':
                return (e['button'], e['pos']), e['time']- shared.start_tp
        shared.time.sleep(0.001)

def whilePressing(job, *param):
    while not shared.figure_released:
        shared.win.dispatch_events()
        job(*param)
    return shared.end_tp - shared.start_tp

def waitForResponse(allowed_keys=[], out_time=0, has_RT=True, allowed_clicks=[], action_while_pressing=None ,suspending=False):
    '''
    Waiting for a allowed keypress event during a limited period
    (Press F12 would suspend the procedure and press ESC would end the program)

    Parameters
    ----------
    allowed_keys: None(default), Keyname, list, or dict
        The allowed key(s).
        You can leave nothing, 
                a Keyname (eg. key_.F), 
                a list of Keyname (eg. [key_.F,key_.J]), 
                or a dict of Keyname (eg. [key_.F:'F',key_.J:'J']) here.
        You could look into the Keyname you want in http://expy.readthedocs.io/en/latest/keymap/
    out_time: num(>0), 0(default)
        The time limit of current function. While the past time exceeds the limitation, the function terminates.
    has_RT: True(default), False
        Return a past time or not
    allowed_clicks: None(default), ClickRange object, list, or dict
        The allowed mouse click event(s).
        You can leave nothing, 
                a ClickRange object (eg. C1), 
                a list of ClickRange object (eg. [C1, C2]), 
                or a dict of ClickRange object (eg. {C1:'F',C2:'J'}) here.
    action_while_pressing: None(default), tuple
        If None, the pressing will be ingored.
        Otherwise, the tuple will be unpacked. 
            The first element is the function, and the rest are(is) the paramenter(s) of the function.

    suspending: True, False(default)
        Label the suspend state. If true, the F12 wouldn't suspend the program.

    Returns
    -------
    KEY: None, int, or defined value
        1. If allowed_keys is None, return the id of any pressed key
        2. If allowed_keys is a List (eg. [key_.F,key_.J]), return the id of allowed pressed key
        3. If allowed_keys is a Dict (eg. [key_.F:'F',key_.J:'J']), return the value of allowed pressed key
        4. Return None if the time is out and no allowed keypress
    (Only if has_RT is True)
        (Only if action_while_pressing is None) RT: int
            The second count since the function starts.
        (Only if action_while_pressing is tuple) RT: (int, int)
            The second count until pressed, and the second count while pressing.
    '''


    now = shared.time.time()
    if not shared.start_tp:
        shared.start_tp = now
        
    shared.events = []
    shared.allowed_keys, shared.allowed_keys_mapping = setKeyMapping(allowed_keys)  # Mapping allowable key(s)
    shared.allowed_mouse_clicks, shared.allowed_mouse_clicks_mapping = setClickMapping(allowed_clicks)

    ev, RT = wait(out_time)

    if type(action_while_pressing) is tuple:
        job, *param = action_while_pressing
        duration = whilePressing(job, *param)
        RT = (RT, duration - RT) # waited_time & pressed_time

    shared.events = []
    shared.start_tp = None
    if has_RT:
        return ev, RT
    else:
        return ev


def pressAndChange(allowed_keys=[], out_time=0):
    '''
    todo
    '''

    now = shared.time.time()
    shared.start_tp = now
        
    shared.events = []
    shared.allowed_keys, shared.allowed_keys_mapping = setKeyMapping(allowed_keys)  # Mapping allowable key(s)

    while True:
        shared.win.dispatch_events()
        past_time = shared.time.time() - shared.start_tp

        if out_time > 0 and past_time >= out_time:
            shared.events = []
            shared.start_tp = None
            return

        for e in shared.events:
            if e['type']=='key_press':
                shared.pressing = e['key']

        if shared.figure_released:
            shared.pressing = None

        shared.time.sleep(0.001)

    # td = shared.threading.Thread(target=wait, args=(out_time,))
    # td.start()
