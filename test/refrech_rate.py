# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

'Experimenting version'

from expy import * # Import the needed functions
start(fullscreen=False, winsize=(800,600)) # Initiate the experiment environment

'''General usage'''
drawText('Hello world!') # Draw text on the canvas
background = getScreen()

# Copy background to screen (position (0, 0) is upper left corner).
shared.win.blit(background, (0,0))
# Create Pygame clock object.  
clock = shared.pg.time.Clock()

mainloop = True
# Desired framerate in frames per second. Try out other values.              
FPS = 90
# How many seconds the "game" is played.
playtime = 0.0

while mainloop:
    # Do not go faster than this framerate.
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0 
    
    for event in shared.pg.event.get():
        # User presses QUIT-button.
        if event.type == shared.pg.QUIT:
            mainloop = False 
        elif event.type == shared.pg.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == shared.pg.K_ESCAPE:
                mainloop = False
    shared.pg.time.wait(1)
                
    # Print framerate and playtime in titlebar.
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    shared.pg.display.set_caption(text)

    #Update Pygame display.
    shared.pg.display.flip()

# import win32api

# def printInfo(device):
#     print( device.DeviceName, device.DeviceString)
#     settings = win32api.EnumDisplaySettings(device.DeviceName, 0)
#     for varName in ['Color', 'BitsPerPel', 'DisplayFrequency']:
#         print( "%s: %s"%(varName, getattr(settings, varName)))

# device = win32api.EnumDisplayDevices()
# printInfo(device)