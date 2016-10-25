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
def start(durations=[], fullscreen=True, normalFontSize = 20, stimFontSize = None, distance=60, diag = 23, angel = 2.5, fontColor = (255,255,255), bgColor = (128, 128, 128)):
    # Set the pointer visibility
    shared.pg.mouse.set_visible(False)

    # Initate the window
    if fullscreen == True:
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

    shared.fontColor = fontColor
    shared.bgColor = bgColor

    # 计算一般显示内容的字体字号
    shared.font['nSize'] = normalFontSize
    shared.font['nFont'] = shared.pg.font.Font(shared.path+"simhei.ttf", normalFontSize)

    # 计算刺激材料的字体字号
    if stimFontSize == None:
        shared.font['sSize'] =  int((shared.winWidth**2 + shared.winHeight**2) **0.5/(diag*2.54 / (distance * np.tan(angel/4*np.pi/180) * 2))) # pixelSize/(pixels in diagonal) = realLength/(real length in diagonal)
    else:
        shared.font['sSize'] =  stimFontSize
    shared.font['sFont'] = shared.pg.font.Font(shared.path+"simhei.ttf", shared.font['sSize'])

    # Set duration of each phase
    for dur in durations:
        k,v = dur.replace(' ','').split(':')
        if '-' in v:
            limit = v.split('-')
            shared.duration[k] = [int(limit[0]),int(limit[1])]
        else:
            shared.duration[k] = int(v)




    

