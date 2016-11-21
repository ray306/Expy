from pygame.locals import *
import time

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
                a Keyname (eg. K_f), 
                a list of Keyname (eg. [K_f,K_j]), 
                or a dict of Keyname (eg. [K_f:'F',K_j:'J']) here.
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

    if type(allowed_keys) == dict:  # eg. allowed_keys = {K_f: 'T', K_j: 'F'}
        keys = list(allowed_keys.keys())
    elif type(allowed_keys) == list:  # eg. allowed_keys = [K_f, K_j]
        mapping = {k: k for k in allowed_keys}
    elif type(allowed_keys) == int:  # eg. allowed_keys = K_ENTER
        keys = [allowed_keys]
        mapping = {allowed_keys: allowed_keys}

    return keys, mapping


def suspend():
    '''
    Suspend the program and display "[程序暂停中/Pause]"

    Returns
    -------
    past time: int
        The millisecond count since the function starts.
    '''
    onset = shared.pg.time.get_ticks()

    backup = shared.pg.display.get_surface().convert()
    shared.win.fill(shared.background_color)

    drawText('[程序暂停中/Pause]')

    # target, (left, top, w, h) = shared.font['simhei'].render(
    #     '[程序暂停中/Pause]', fgcolor=C_white, size=(25, 25))
    # shared.win.blit(target, ((shared.win_width - w) / 2, (shared.win_height - h) / 2))
    # shared.pg.display.flip()

    # target = shared.font['normalFont'].render(
    #     '[程序暂停中/Pause]', True, shared.font_color)
    # shared.win.blit(target,
    #                 ((shared.win_width - target.get_width()) / 2, (shared.win_height - target.get_height()) / 2))
    # shared.pg.display.flip()

    waitForResponse(K_F12, suspending=True)

    shared.win.blit(backup, (0, 0))
    shared.pg.display.flip()

    return shared.pg.time.get_ticks() - onset


def waitForResponse(allowed_keys=None, out_time=0, has_RT=True, suspending=False):
    '''
    Waiting for a allowed keypress event during a limited period
    (Press F12 would suspend the procedure and press ESC would end the program)

    Parameters
    ----------
    allowed_keys：None(default), Keyname, list, or dict
        The allowed key(s).
        You can leave nothing, 
                a Keyname (eg. K_f), 
                a list of Keyname (eg. [K_f,K_j]), 
                or a dict of Keyname (eg. [K_f:'F',K_j:'J']) here.
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
        2. If allowed_keys is a List (eg. [K_f,K_j]), return the id of allowed pressed key
        3. If allowed_keys is a Dict (eg. [K_f:'F',K_j:'J']), return the value of allowed pressed key
        4. Return None if the time is out and no allowed keypress
    (Only if has_RT is True) past_time: int
        The millisecond count since the function starts.
    '''
    def wait(keys, mapping, start_tp, out_time):
        while True:
            past_time = shared.pg.time.get_ticks() - start_tp
            if out_time > 0 and past_time >= out_time:
                return 'None', 'None'

            for e in shared.pg.event.get():

                'get the pressed key'
                if e.type == KEYDOWN:
                    k = e.key
                elif e.type == JOYBUTTONDOWN:
                    k = e.button
                elif e.type == MOUSEBUTTONDOWN:  # e.type == MOUSEMOTION, k = e.pos
                    k = e.button
                else:
                    continue

                'decision'
                if k == 27:
                    shared.pg.quit()
                elif k == K_F12 and not suspending:
                    suspend_time = suspend()
                    start_tp += suspend_time
                elif not keys:  # if allowed_keys is None
                    return k, past_time
                elif k in keys:  # if k is in the allowed Keyname(s)
                    return mapping[k], past_time

            time.sleep(0.001)

    start_tp = shared.pg.time.get_ticks()
    shared.pg.event.clear()

    keys, mapping = setKeyMapping(allowed_keys)  # Mapping allowable key(s)
    KEY, past_time = wait(keys, mapping, start_tp, out_time)
    if has_RT:
        return KEY, past_time
    else:
        return KEY
