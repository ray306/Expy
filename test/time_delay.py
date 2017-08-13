# coding:utf-8
##### package test #####
import sys
sys.path = ['../../']+sys.path
################

from expy import *  # Import the needed functions

# Zero-setting
def reset():
    sendTrigger('mh00', mode='S')
    show(0.15)

def close():
    sendTrigger('mh70', mode='S') # close signal
    shared.pa.terminate()
    shared.win.close()
    shared.ser.close()
    shared.pyglet.app.exit()

def visualCases(count):
    'draw run + flip - trigger send'
    for _ in range(count):
        reset()
        sendTrigger('mh10', mode='S') # program trigger
        drawText('Hello', display=False)
        drawCircle(30, fill=True, x=-0.9, y=-0.9, display=False)
        show(1) # physical trigger
        show(0.5)

    'flip - trigger send'
    for _ in range(count):
        reset()
        drawText('Hello', display=False)
        drawCircle(30, fill=True, x=-0.9, y=-0.9, display=False)
        sendTrigger('mh20', mode='S') # program trigger
        show(1) # physical trigger
        show(0.5)

    'trigger run + trigger send - flip'
    for _ in range(count):
        reset()
        drawText('Hello', display=False)
        drawCircle(30, fill=True, x=-0.9, y=-0.9) # physical trigger
        sendTrigger('mh30', mode='S') # program trigger
        show(1)
        show(0.5)

    'flip - trigger send'
    for _ in range(count):
        reset()
        drawText('Hello', display=False)
        drawCircle(30, fill=True, x=-0.9, y=-0.9,trigger=('mh40', 'S')) # program trigger, physical trigger
        show(1)
        show(0.5)

def auditoryCases(count):
    sound = makeBeep(440, 1)

    'playing start - trigger send'
    for _ in range(count):
        reset()
        sendTrigger('mh10', mode='S') # program trigger
        playSound(sound)
        show(0.5)

    'playing start 2 - trigger send'
    for _ in range(count):
        reset()
        playSound(sound,trigger=('mh20', 'S'))
        show(0.5)

start(port='COM5')
visualCases(2)
close()

start(port='COM5',vsync=False)
visualCases(2)
close()

start(port='COM5',sample_rate=44100)
auditoryCases(2)
close()