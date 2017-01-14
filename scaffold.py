import pyglet.window.key as key_
from expy import shared
from .colors import *
from .stim.draw import *
from .stim.display import *
from .io import *
from .response import *

np = shared.np


def timing(name):
    '''
    Get a value of timing parameter:
    If the setting gave a int, return it;
    If the setting gave a range, return a random int in that range.

    Parameters
    ----------
    name：str
        The name of timing parameter.
        
    Return
    ---------
    value: int
    '''
    val = shared.setting['timing'][name]
    if type(val) == int:
        return val
    else:
        return np.random.randint(val[0], val[1])

def textSlide(text, font='simhei', size='normal_font_size', background_image=None):
    '''
    Display a new text slide right now.

    Parameters
    ----------
    text：str
        The text on the screen.
    font: str (default:'simhei')
        The fontname of the text.
    size: str (default:'normal_font_size')
        The fontsize of the text.
    background_image: str, or None(default)
        The path of background picture.
        
    Return
    ---------
    None
    '''
    clear()
    if background_image:
        drawPic(path)    
    drawText(text, font=font, size=size)
    

def getInput(pre_text, out_time=0):
    '''
    Get user input until "ENTER" pressed, then give it to a variable

    Parameters
    ----------
    pre_text：str
        The text that will be displayed before user's input.
    out_time: int(>0) or 0(default)
        The time limitation of this function.

    Return
    ---------
    input_text: str
        The content of user's input.
    '''
    textSlide(pre_text)
    text = pre_text
    if not shared.start_tp:
        shared.start_tp = shared.time.time()
    while 1:
        inkey = waitForResponse(has_RT=False, out_time=out_time)
        if inkey in [key_.RETURN, 'None']:
            break
        elif inkey == key_.BACKSPACE:
            text = text[0:-1]
        elif inkey <= 127:
            text += (chr(inkey))
        textSlide(text)
    input_text = text[len(pre_text):]
    clear()
    return input_text

def instruction(instruction_text, has_practice=False):
    '''
    Show the instruction of experiment
    (press 'left' to back, 'right' to continue)

    Parameters
    ----------
    instruction_text：list of str
        The text that will be displayed as instruction.

    Return
    ---------
    resp: Keyname/int
        The last pressed key name.
    '''
    intro = '\n'.join(instruction_text).split('>\n')
    i = 0
    while True:
        if intro[i] == '[demo]':
            demo()
            i += 1
            continue

        if i == 0:
            textSlide(
                intro[i] + '\n\n\n(按“→”进入下一页)\n\n(Press "→" to the next page)')
        elif i == len(intro) - 1:
            textSlide(intro[
                      i] + '\n\n\n(按“←”返回上一页，按 [空格] 开始实验. )\n\n(Press "←" to the previous page, or Press "SPACE" to start the experiment)')
        else:
            textSlide(intro[
                      i] + '\n\n\n(按“←”返回上一页，按“→”进入下一页)\n\n(Press "←" to the previous page, or Press "→" to the next page)')

        resp = waitForResponse(has_RT=False)
        if resp == key_.LEFT and i > 0:
            i -= 1
        elif resp == key_.RIGHT and i < len(intro) - 1:
            i += 1
        elif resp in [key_.SPACE, key_.RETURN] and i == len(intro) - 1:
            clear()
            return resp

def alert(text, allowed_keys=[key_.RETURN], out_time=0):
    '''
    Display a new text slide right now, and keep the screen until user's response.

    Parameters
    ----------
    text：str
        The text on the screen.
    allowed_keys: Keyname, or list of Keyname (default:[key_.RETURN])
        The allowed user's response.
    out_time: int(>0) or 0(default)
        The display time limitation of this function.
        
    Return
    ---------
    resp: Keyname/int
        The last pressed key name.
    '''
    textSlide(text)
    resp = waitForResponse(allowed_keys, out_time, has_RT=False)
    clear()
    return resp

def alertAndGo(text, out_time=3000):
    '''
    Display a new text slide right now, 
    and keep the screen in a given period of time, or until user pressed SPACE or key_.RETURN

    Parameters
    ----------
    text：str
        The text on the screen.
    out_time: int(>0) or 0(default)
        The display time limitation of this function.
        
    Return
    ---------
    None
    '''
    alert(text, out_time=out_time)

def alertAndQuit(text, out_time=3000):
    '''
    Display a new text slide right now, 
    and keep the screen in a given period of time, or until user pressed SPACE or key_.RETURN,
    then quit the program.

    Parameters
    ----------
    text：str
        The text on the screen.
    out_time: int(>0) or 0(default)
        The display time limitation of this function.
        
    Return
    ---------
    None
    '''
    alertAndGo(text, out_time)
    shared.pa.terminate()
    shared.pyglet.app.exit()

rest_text = '实验暂停，您可以休息一会\n\
如果休息结束请按 [空格] 继续实验。\n\
Now you could have a rest,\n \
please press [SPACE] key when you decide to continue.\n'
def restTime(text=rest_text):
    '''
    Suspend the experiment and ask participant to rest:
    1. Display a blank screen in 3s,
    2. Display a new text slide which tells user to rest, 
    3. eep the screen until user pressed SPACE.

    Parameters
    ----------
    text：str
        The text on the screen.
        
    Return
    ---------
    None
    '''
    textSlide(text)
    shared.time.sleep(3)
    alert(text, key_.SPACE)
