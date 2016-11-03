from pygame.locals import *
import time
from expy import shared


def setKeyMapping(allowedKeys):
    '''
    Make a list and a mapping of allowable key(s)
    
    Parameters
    ----------
    allowedKeys：None(default), Keyname, list, or dict
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
    keys = allowedKeys
    mapping = allowedKeys

    if type(allowedKeys) == dict:  # eg. allowedKeys = {K_f: 'T', K_j: 'F'}
        keys = list(allowedKeys.keys())
    elif type(allowedKeys) == list:  # eg. allowedKeys = [K_f, K_j]
        mapping = {k: k for k in allowedKeys}
    elif type(allowedKeys) == int:  # eg. allowedKeys = K_ENTER
        keys = [allowedKeys]
        mapping = {allowedKeys: allowedKeys}

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
    shared.win.fill(shared.backgroundColor)

    target = shared.font['normalFont'].render(
        '[程序暂停中/Pause]', True, shared.fontColor)
    shared.win.blit(target,
                    ((shared.winWidth - target.get_width()) / 2, (shared.winHeight - target.get_height()) / 2))
    shared.pg.display.flip()

    waitForResponse(K_F12, suspending=True)

    shared.win.blit(backup, (0, 0))
    shared.pg.display.flip()

    return shared.pg.time.get_ticks() - onset


def waitForResponse(allowedKeys=None, outTime=0, hasRT=True, suspending=False):
    '''
    Waiting for a allowed keypress event during a limited period
    (Press F12 would suspend the procedure and press ESC would end the program)

    Parameters
    ----------
    allowedKeys：None(default), Keyname, list, or dict
        The allowed key(s).
        You can leave nothing, 
                a Keyname (eg. K_f), 
                a list of Keyname (eg. [K_f,K_j]), 
                or a dict of Keyname (eg. [K_f:'F',K_j:'J']) here.
        You could look into the Keyname you want in http://expy.readthedocs.io/en/latest/keymap/
    outTime：int(>0), 0(default)
        The time limit of current function. While the past time exceeds the limitation, the function terminates.
    hasRT：True(default), False
        Return a past time or not
    suspending: True, False(default)
        Label the suspend state. If true, the F12 wouldn't suspend the program.

    Returns
    -------
    KEY: None, int, or defined value
        1. If allowedKeys is None, return the id of any pressed key
        2. If allowedKeys is a List (eg. [K_f,K_j]), return the id of allowed pressed key
        3. If allowedKeys is a Dict (eg. [K_f:'F',K_j:'J']), return the value of allowed pressed key
        4. Return None if the time is out and no allowed keypress
    (Only if hasRT is True) pastTime: int
        The millisecond count since the function starts.
    '''
    def wait(keys, mapping, startT, outTime):
        while True:
            pastTime = shared.pg.time.get_ticks() - startT
            if outTime > 0 and pastTime >= outTime:
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
                    suspendTime = suspend()
                    startT += suspendTime
                elif not keys:  # if allowedKeys is None
                    return k, pastTime
                elif k in keys:  # if k is in the allowed Keyname(s)
                    return mapping[k], pastTime

            time.sleep(0.001)

    startT = shared.pg.time.get_ticks()
    shared.pg.event.clear()

    keys, mapping = setKeyMapping(allowedKeys)  # Mapping allowable key(s)
    KEY, pastTime = wait(keys, mapping, startT, outTime)
    if hasRT:
        return KEY, pastTime
    else:
        return KEY
