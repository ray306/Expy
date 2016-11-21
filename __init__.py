# coding:utf-8
import io
import os
from pygame.locals import *
from pygame import freetype
import numpy as np
import pandas as pd
import random
import time

from . import shared
from .colors import *
from .io import *
from .response import *
from .stim.draw import *
from .stim.display import *
from .stim.sound import *
from .stim.video import *
from .recorder import *
from .scaffold import *
from .extend import *

def start(setting_file='setting.txt', fullscreen=True, winsize=(800, 600), mouse_visible=False, normal_font_size=20, stim_font_size=None, distance=60, diag=23, angel=2.5, font_color=(255, 255, 255), background_color=(128, 128, 128), sample_rate=44100, bits=16, channel=2, port='COM1'):
    '''
    Initialize the experiment.
    Note: todo.

    Parameters
    ----------
    setting_file: str (default: 'setting.txt')
        The filepath of setting
    fullscreen: True(default), or False 
        Whether the window is fullscreen
    winsize: (width,height) (default:(800, 600)) 
        The size of window
    mouse_visible: True, or False(default)
        Set the mouse pointer visibility
    normal_font_size: int (default:20) 
        The size of the text in normal font 
    stim_font_size: int, or None(default) 
        The size of the text in stimulus font  
    distance: int (default:60) 
        Distance from eyes to screen (cm)
    diag: int (default:23) 
        The length of the screen diagonal (inch) 
    angel: int (default:2.5) 
        Visual angel of single char (degree)
    font_color: tuple RGB (default:(255, 255, 255)) 
        The color of text
    background_color: tuple RGB (default:(128, 128, 128)) 
        The color of background
    sample_rate: int (default:44100) 
        Sample rate of sound mixer
    bits: int (default:16) 
        Bits of sound mixer
    channel: int (default:2) 
        Channel amount of sound mixer
    port: str, or hex number (default:'COM1') 
        Port name used to send trigger.
        Use str on serial port, and hex on parallel port 

    Returns
    -------
    None
    '''
    
    'Parameters'
    func_var = locals().copy()
    try:
        shared.setting = readSetting(setting_file)
    except:
        print('"setting.txt" does not exist.')

    for k, v in shared.setting.items():
        if k in ['fullscreen', 'font_color', 'winsize', 'mouse_visible', 'background_color', 'distance', 'diag', 'angel',
                 'sample_rate', 'bit', 'channel', 'port'] or k[-10:] == '_font_size':
            func_var[k] = eval('%s' % v[0])
        else:
            func_var[k] = eval('%s' % v)

    shared.setting = func_var

    'Color'
    shared.font_color = shared.setting['font_color']
    shared.background_color = shared.setting['background_color']

    'Mouse pointer visibility'
    # Set the pointer visibility
    shared.pg.mouse.set_visible(shared.setting['mouse_visible'])
    shared.pg.mixer.quit()

    'Sound mixer'
    # Initate the mixer
    shared.pg.mixer.init(shared.setting[
                         'sample_rate'], -shared.setting['bits'], shared.setting['channel'])

    'Window'
    # Initate the window
    if shared.setting['fullscreen'] == True:
        shared.win = shared.pg.display.set_mode(
            (shared.win_width, shared.win_height), FULLSCREEN | HWSURFACE | DOUBLEBUF)
    else:
        shared.win = shared.pg.display.set_mode(
            shared.setting['winsize'], HWSURFACE | DOUBLEBUF)
        shared.win_width = shared.setting['winsize'][0]
        shared.win_height = shared.setting['winsize'][1]
    clear()  # Reset screen color

    'Joystick'
    # Initate the joystick
    try:
        joystick = shared.pg.joystick.Joystick(0)
        joystick.init()
    except:
        pass

    'Font'
    # Get the font size attribute of normal text, stimulus, or others
    for k, v in shared.setting.items():
        if '_font_size' == k[-10:]:
            shared.font[k] = v

    if shared.setting['stim_font_size'] == None:
        shared.font['stim_font_size'] = int((shared.win_width**2 + shared.win_height**2) ** 0.5 / (shared.setting['diag'] * 2.54 / (shared.setting[
                                          'distance'] * np.tan(shared.setting['angel'] / 4 * np.pi / 180) * 2)))  # pixelSize/(pixels in diagonal) = realLength/(real length in diagonal)
    # Find out all the .ttf files and load them.
    for f in os.listdir(shared.path):
        if f[-4:] == '.ttf':
            shared.font[f[:-4]] = freetype.Font(shared.path + f)

    # for k, v in shared.font.copy().items():
    #     shared.font[
    #         k[:-4]] = shared.pg.font.Font(shared.path + "simhei.ttf", shared.font[k])

    'Port (only serial port needs port name pre-define)'
    try:
        shared.ser.port = shared.setting['port']  # set the port
        shared.ser.open()
    except:
        print('Could not open serial port')
