# coding:utf-8
import io
import os
from pygame.locals import *
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
def start(settingfile='setting.txt', fullscreen=True, normalFontSize = 20, stimFontSize = None, distance=60, diag = 23, angel = 2.5, fontColor = (255,255,255), backgroundColor = (128, 128, 128), sample_rate = 44100, bits = 16, channel=2):
    func_var = locals().copy()
    
    readSetting(settingfile)
    for k in ['fullscreen','fontColor','backgroundColor','distance','diag','angel',
              'normalFontSize','stimFontSize','sample_rate','bit','channel']:
        if setting(k):
            func_var[k] = eval('%s' %setting(k)[0])

    # Set the pointer visibility
    shared.pg.mouse.set_visible(False)
    shared.pg.mixer.quit()

    # Initate the mixer
    shared.pg.mixer.init(func_var['sample_rate'], -func_var['bits'], func_var['channel'])
    
    # Initate the window
    if func_var['fullscreen'] == True:
        shared.win = shared.pg.display.set_mode((shared.winWidth,shared.winHeight), FULLSCREEN| HWSURFACE|DOUBLEBUF)
    else:
        shared.win = shared.pg.display.set_mode((800,600), HWSURFACE | DOUBLEBUF)
        shared.winWidth = 800
        shared.winHeight = 600

    # Initate the joystick
    try:
        joystick = shared.pg.joystick.Joystick(0)
        joystick.init()
    except:
        pass

    shared.fontColor = func_var['fontColor']
    shared.backgroundColor = func_var['backgroundColor']

    # Get the font attribute of normal text
    shared.font['nSize'] = func_var['normalFontSize']
    shared.font['nFont'] = shared.pg.font.Font(shared.path+"simhei.ttf", shared.font['nSize'])

    # Get the font attribute of stimulus text
    if func_var['stimFontSize'] == None:
        shared.font['sSize'] =  int((shared.winWidth**2 + shared.winHeight**2) **0.5/(func_var['diag']*2.54 / (func_var['distance'] * np.tan(func_var['angel']/4*np.pi/180) * 2))) # pixelSize/(pixels in diagonal) = realLength/(real length in diagonal)
    else:
        shared.font['sSize'] =  func_var['stimFontSize']
        
    shared.font['sFont'] = shared.pg.font.Font(shared.path+"simhei.ttf", shared.font['sSize'])

    clear()