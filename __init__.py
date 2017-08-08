# coding:utf-8
import io

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

os = shared.os
np = shared.np
time = shared.time
key_ = shared.key_
mouse_ = shared.mouse_


def start(setting_file='setting.txt', fullscreen=True, winsize=(800, 600), mouse_visible=False, normal_font_size=20, stim_font_size=None, distance=60, diag=23, angel=2.5, font_color=C_white, background_color=C_gray, sample_rate=44100, port='', vsync=True):
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
    font_color: tuple RGBA (default:C_white) 
        The color of text
    background_color: tuple RGBA (default:C_gray) 
        The color of background
    sample_rate: int (default:44100) 
        Sample rate of sound mixer
    port: str, or hex number (default:'') 
        Port name used to send trigger.
        Use str on serial port, and hex on parallel port 
    vsync: True(default), or False
        Vertical retrace synchronisation

    Returns
    -------
    None
    '''

    'Parameters'
    func_var = locals().copy()
    shared.setting = readSetting(setting_file)
    for k, v in shared.setting.items():
        # if k in ['fullscreen', 'font_color', 'winsize', 'mouse_visible', 'background_color', 'distance', 'diag', 'angel',
        #          'sample_rate', 'port'] or k[-10:] == '_font_size':
        #     func_var[k] = eval('%s' % v)
        # else:
        #     func_var[k] = eval('%s' % v)
        try:
            func_var[k] = eval('%s' % v)
        except:
            func_var[k] = eval('"%s"' % v)

    shared.setting = func_var

    'Color'
    shared.font_color = shared.setting['font_color']
    shared.background_color = tuple(
        i / 255 for i in shared.setting['background_color'])

    'Window'
    # Initate the window
    if shared.setting['fullscreen'] == True:
        shared.win = shared.pyglet.window.Window(fullscreen=True, vsync=vsync)
        shared.win_width = shared.win.width
        shared.win_height = shared.win.height
    else:
        shared.win_width = shared.setting['winsize'][0]
        shared.win_height = shared.setting['winsize'][1]
        shared.win = shared.pyglet.window.Window(
            width=shared.win_width, height=shared.win_height, vsync=vsync)
    shared.pyglet.gl.glClearColor(*shared.background_color)

    shared.win.dispatch_events()
    shared.win.clear()  # Reset screen color
    shared.win.switch_to()

    'Mouse pointer visibility'
    # Set the pointer visibility
    if not mouse_visible:
        shared.win.set_exclusive_mouse(True)
        shared.win.set_mouse_platform_visible(False)

    'Joystick'
    # Initate the joystick
    try:
        joysticks = shared.pyglet.input.get_joysticks()[0]
        joystick.open()
    except:
        pass

    'Sound (OpenAL)'
    # def sound_stream():
    #     shared.stream = shared.pa.open(format=shared.pyaudio.paInt16,
    #                         channels=2, rate=shared.setting['sample_rate'],
    #                         input=True, output=True)
    #     while 1:
    # shared.sound_process = Process(target=sound_stream, args=(shared.q,))
    # shared.sound_process.start()
    # if shared.has_openal:
    #     pass
    # device = shared.alc.alcOpenDevice(None)
    # context = shared.alc.alcCreateContext(device, None)
    # shared.alc.alcMakeContextCurrent(context)

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
            shared.pyglet.font.add_file(shared.path + f)

    'Port (only serial port needs port name pre-define)'
    try:
        if shared.setting['port'] != '':
            shared.ser.port = shared.setting['port']  # set the port
            shared.ser.open()
    except:
        print('Could not open serial port')

    # shared.watchdog.start()
    # print('Watchdog started')

    @shared.win.event
    def on_mouse_press(x, y, button, modifiers):
        for event in shared.allowed_mouse_clicks:
            if x in event.x and y in event.y and button == event.button:
                e = {'type': 'mouse_press',
                     'button': button,
                     'pos': (x, y),
                     'time': time.time()}
                shared.events.append(e)
                return

        shared.figure_released = False

    @shared.win.event
    def on_key_press(k, modifiers):
        'decision'
        if k == key_.ESCAPE:
            shared.ser.close()
            shared.pa.terminate()
            shared.win.close()
            shared.pyglet.app.exit()
        elif k == key_.F12 and not shared.suspending:
            shared.suspending = True
            start_tp_raw = shared.start_tp
            suspend_time = suspend()
            shared.suspending = False
            shared.start_tp = start_tp_raw + suspend_time
        if len(shared.allowed_keys) == 0:  # if allowed_keys is None
            e = {'type': 'key_press',
                 'key': k,
                 'time': time.time()}
            shared.events.append(e)
        elif k in shared.allowed_keys:  # if k is in the allowed Keyname(s)
            e = {'type': 'key_press',
                 'key': shared.allowed_keys_mapping[k],
                 'time': time.time()}
            shared.events.append(e)

        shared.figure_released = False

    @shared.win.event
    def on_key_release(k, modifiers):
        shared.end_tp = time.time()
        shared.figure_released = True

    @shared.win.event
    def on_mouse_release(x, y, button, modifiers):
        shared.end_tp = time.time()
        shared.figure_released = True

    # @shared.win.event
    # def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    #     pass

    @shared.win.event
    def on_close():
        shared.ser.close()
        shared.pa.terminate()
        shared.win.close()
        shared.pyglet.app.exit()
