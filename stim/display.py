from expy import shared
from expy.colors import *
from .draw import *
from expy.response import *

def clear(debugging=True):
    '''
    Clear the screen

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''

    shared.win.clear()
    shared.win.flip()
    if debugging:
        shared.win.clear()
        shared.win.flip() 


def show(out_time=False, clean_screen=True, stop_signal=None, backup=None, debugging=True):
    '''
    Display current canvas buffer, and keep the display during a limited period.

    Parameters
    ----------
    out_time: num(>0), False(default)
        The time limit of current function. (unit: second)
    clean_screen: True(default), False
        Whether clear the screen after get the screen or not. 
    stop_signal: None (default), str
        If the stop_signal is str, this method would be blocked until a stop_signal was received from the 0.0.0.0:36
    backup: None, or a screen backup
        Give a prepared screen to display

    Returns
    -------
    None
    '''
    if backup:
        shared.need_update = True
        backup.blit(0,0,0)
    if shared.need_update:
        shared.win.flip()
        shared.need_update = False

    if out_time:
        waitForResponse(shared.key_.ENTER, out_time)
    if stop_signal!=None:
        shared.net_port_state = ''
        s = stop_signal.encode(encoding='utf_8', errors='strict')
        while True:
            if shared.net_port_state == s:
                shared.net_port_state = ''
                break
    if clean_screen:
        clear(debugging)
    else:
        shared.win.flip()

def getScreen(clean_screen=True):
    '''
    Get a backup of current canvas

    Parameters
    ----------
    clean_screen: True(default), False
        Whether clear the screen after get the screen or not. 

    Returns
    -------
    None
    '''

    backup = shared.pyglet.image.get_buffer_manager().get_color_buffer().get_image_data()
    if clean_screen:
        clear()
    return backup
