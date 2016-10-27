# coding:utf-8
import os
import pygame as pg
import ctypes

'environment varible'
path = os.path.dirname(os.path.abspath(__file__)) + '/'

winWidth, winHeight = pg.display.set_mode((0,0)).get_size() 
# from win32api import GetSystemMetrics
# winWidth = GetSystemMetrics(0)
# winHeight = GetSystemMetrics(1)
font = dict()
win = None
backgroundColor = None
fontColor = None

'experiment varible'
subj = ''
startBlockID = 1

setting = dict()
timing = dict()


# init
pg.init()
Objdll = ctypes.windll.LoadLibrary(path+"inpoutx64.dll")