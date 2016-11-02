# coding:utf-8
import io
import os
from pygame.locals import *
from pygame import freetype
import numpy as np

from . import shared
from .io import *
from .response import *
from .stim.draw import *
from .stim.display import *
from .stim.sound import *
from .stim.video import *
from .recorder import *
from .scaffold import *
from .extend import *


# 启动pygame环境，设置好一些参数
# 【参数】fullscreen：是否全屏显示
#               normalFontSize: 一般显示内容的字体字号
#               normalFont: 一般显示内容的字体字号
#               distance = 40：distance from eyes to screen (cm)
#               diag = 14.3：the length of the screen diagonal (inch)
#               angel = 1.5：visual angel of single char (degree)
# 【返回值】pg：pygame对象，win：显示屏对象，font：字体对象
def start(settingfile='setting.txt', fullscreen=True, winsize=(800,600),mouseVisible=False, normalFontSize = 20, stimFontSize = None, distance=60, diag = 23, angel = 2.5, fontColor = (255,255,255), backgroundColor = (128, 128, 128), sample_rate = 44100, bits = 16, channel=2, port='COM1'):
    'Parameters'
    func_var = locals().copy()
    shared.setting = readSetting(settingfile)

    for k,v in shared.setting.items():
        if k in ['fullscreen','fontColor','winsize','mouseVisible','backgroundColor','distance','diag','angel',
              'sample_rate','bit','channel','port'] or k[-8:] == 'FontSize':
            func_var[k] = eval('%s' %v[0])
        else:
            func_var[k] = eval('%s' %v)

    shared.setting = func_var

    'Color'
    shared.fontColor = shared.setting['fontColor']
    shared.backgroundColor = shared.setting['backgroundColor']

    'Mouse pointer visibility'
    # Set the pointer visibility
    shared.pg.mouse.set_visible(shared.setting['mouseVisible'])
    shared.pg.mixer.quit()

    'Sound mixer'
    # Initate the mixer
    shared.pg.mixer.init(shared.setting['sample_rate'], -shared.setting['bits'], shared.setting['channel'])
    
    'Window'
    # Initate the window
    if shared.setting['fullscreen'] == True:
        shared.win = shared.pg.display.set_mode((shared.winWidth,shared.winHeight), FULLSCREEN| HWSURFACE|DOUBLEBUF)
    else:
        shared.win = shared.pg.display.set_mode(shared.setting['winsize'], HWSURFACE | DOUBLEBUF)
        shared.winWidth = shared.setting['winsize'][0]
        shared.winHeight = shared.setting['winsize'][1]
    clear() # Reset screen color

    'Joystick'
    # Initate the joystick
    try:
        joystick = shared.pg.joystick.Joystick(0)
        joystick.init()
    except:
        pass

    'Font'
    # Get the font size attribute of normal text, stimulus, or others
    for k,v in shared.setting.items():
         if 'FontSize' == k[-8:]:
            shared.font[k] = v

    if shared.setting['stimFontSize'] == None:
        shared.font['stimFontSize'] =  int((shared.winWidth**2 + shared.winHeight**2) **0.5/(shared.setting['diag']*2.54 / (shared.setting['distance'] * np.tan(shared.setting['angel']/4*np.pi/180) * 2))) # pixelSize/(pixels in diagonal) = realLength/(real length in diagonal)
    
    for k,v in shared.font.copy().items():
         shared.font[k[:-4]] = shared.pg.font.Font(shared.path+"simhei.ttf", shared.font[k])

    shared.font['ft'] = freetype.Font(shared.path+"simhei.ttf")

    'Port (only serial port needs port name pre-define)'
    shared.ser.port = shared.setting['port'] # set the port
    try:
        shared.ser.open()
    except:
        print('Could not open serial port')

    