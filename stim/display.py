from expy import shared
from .draw import *
from expy.response import *

def clear():
    '''
    Clear the screen

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    shared.win.fill(shared.backgroundColor)
    shared.pg.display.flip()

def show(outTime=False, cleanScreen=True, backup=None):
    '''
    Display current canvas buffer, and keep the display during a limited period.

    Parameters
    ----------
    outTime: int(>0), False(default)
        The time limit of current function. 
    cleanScreen: True(default), False
        Whether clear the screen after get the screen or not. 
    backup: None, or a screen backup
        Give a prepared screen to display

    Returns
    -------
    None
    '''
    if backup:
        shared.win.blit(backup, (0, 0))
    shared.pg.display.flip()
    if outTime:
        waitForResponse({}, outTime)
        if cleanScreen:
            clear()

def getScreen(cleanScreen=True):
    '''
    Get a backup of current canvas

    Parameters
    ----------
    cleanScreen: True(default), False
        Whether clear the screen after get the screen or not. 

    Returns
    -------
    None
    '''
    backup = shared.pg.display.get_surface().convert()
    if cleanScreen:
        clear()
    return backup
