from expy import shared
from expy.colors import *
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
    # shared.win.fill(shared.background_color)
    # shared.pg.display.flip()
    shared.win.clear()
    shared.win.flip()
    shared.win.clear()
    shared.win.flip()


def show(out_time=False, clean_screen=True, backup=None):
    '''
    Display current canvas buffer, and keep the display during a limited period.

    Parameters
    ----------
    out_time: num(>0), False(default)
        The time limit of current function. (unit: second) 
    clean_screen: True(default), False
        Whether clear the screen after get the screen or not. 
    backup: None, or a screen backup
        Give a prepared screen to display

    Returns
    -------
    None
    '''
    if backup:
        shared.need_update = True
        backup.blit(0,0,0)
        # shared.win.blit(backup, (0, 0))
    if shared.need_update:
        shared.win.flip()
        shared.need_update = False

    # shared.pg.display.flip()
    if out_time:
        waitForResponse(shared.key_.ENTER, out_time)
        if clean_screen:
            clear()

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

    # backup = shared.pg.display.get_surface().convert()
    backup = shared.pyglet.image.get_buffer_manager().get_color_buffer().get_image_data()
    if clean_screen:
        clear()
    return backup
