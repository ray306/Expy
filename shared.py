# coding:utf-8
import os
import pygame as pg
import ctypes
import serial

'''
Some variable that will be used in many place.
'''

'environment varible'
path = os.path.dirname(os.path.abspath(__file__)) + '/'

try:
    from win32api import GetSystemMetrics
    win_width = GetSystemMetrics(0)
    win_height = GetSystemMetrics(1)
except:
    win_width, win_height = pg.display.set_mode((0,0)).get_size()


win = None

'experiment varible'
subject = ''
start_block = 1

font = dict()
background_color = None
font_color = None

setting = dict()
timing = dict()

# init
pg.init()
port_dll = ctypes.windll.LoadLibrary(path + "inpoutx64.dll")
ser = serial.Serial(baudrate=115200)
