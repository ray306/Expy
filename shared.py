# coding:utf-8
import os
import ctypes
import serial
import time
import threading
import platform

import pyglet
from pyglet import gl
import pyglet.window.key as key_
import pyglet.window.mouse as mouse_

import librosa
import pyaudio
import numpy as np
import math

'''
Some variable that will be used in many place.
'''

'environment varibles'
path = os.path.dirname(os.path.abspath(__file__)) + '/'

win_width = 0
win_height = 0

win = None
need_update = False

'event varibles'
events = []
events2 = []
states = dict()

allowed_keys = []
allowed_keys_mapping = dict()

allowed_mouse_clicks = []  # {'x':range(), 'y':range(), 'button':..}
allowed_mouse_clicks_mapping = dict()

suspending = False

pressing = None
figure_released = True

start_tp = 0
end_tp = 0

onset = time.time()
with open('log.txt','a') as f:
    f.write('###\nOnset\t%s\n' %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(onset)) ))

'port'
if platform.system() == "Windows":
    if platform.architecture()[0] == '64bit':
        port_dll = ctypes.windll.LoadLibrary(path + "inpoutx64.dll")
    else:
        port_dll = ctypes.windll.LoadLibrary(path + "inpout32.dll")
else:
    port_dll = None

ser = serial.Serial(baudrate=115200)

'threading'
check_serial_port = False
serial_port_state = ''
def serial_port_listener():
    # main_thread = threading.main_thread()
    global check_serial_port  # serial port listener
    global serial_port_state
    global start_tp
    while 1:
        time.sleep(0.0005)
        if check_serial_port:
            serial_port_state = ser.read()
            start_tp = time.time()
            check_serial_port = False
        # if not main_thread.is_alive():
        #     break
td_sp = threading.Thread(target=serial_port_listener)
td_sp.start()

net_port_state = ''
def net_port_listener():
    import socket
    HOST = '0.0.0.0'
    PORT = 36

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    global net_port_state
    while True:
        try:
            conn, addr = s.accept()
            while True:
                net_port_state = conn.recv(1024)
        except:
            continue

td_net = threading.Thread(target=net_port_listener)
td_net.start()


lock = threading.Lock()

def changeState(name, value):
    '''
    Change the value of a global state
    Parameters
    ----------
    name: anything
        The name of the target state
    value: anything
        The target value of the target state

    Return
    ---------
    None
    '''
    lock.acquire()
    try:
        states[name] = value
    finally:
        lock.release()

'experiment varibles'
subject = ''
start_block = 1

setting = dict()
timing = dict()

font = dict()
background_color = None
font_color = None

if platform.system() in ["Windows",'Linux']:
    default_font = 'simhei'
else:
    default_font = 'hei'

'sound'
pa = pyaudio.PyAudio()
# try:
#     from pyglet.media.drivers.openal import lib_openal as al
#     from pyglet.media.drivers.openal import lib_alc as alc
# except:
#     print('OpenAL not installed')
#     has_openal = False
# else:
#     has_openal = True


