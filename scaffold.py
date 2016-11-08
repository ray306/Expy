import numpy as np
from pygame.locals import *

from expy import shared
from .colors import *
from .stim.draw import *
from .stim.display import *
from .io import *
from .response import *


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

def textSlide(text, font='simhei', size='normalFontSize', bgImage=None):
    '''
    Display a new text slide right now.

    Parameters
    ----------
    text：str
        The text on the screen.
    font: str (default:'simhei')
        The fontname of the text.
    size: str (default:'normalFontSize')
        The fontsize of the text.
    bgImage: str, or None(default)
        The path of background picture.
        
    Return
    ---------
    None
    '''
    shared.win.fill(shared.backgroundColor)
    if bgImage:
        drawPic(path)    
    drawText(text, font=font, size=size)
    

def getInput(preText):
    '''
    Get user input until "ENTER" pressed, then give it to a variable

    Parameters
    ----------
    preText：str
        The text that will be displayed before user's input.

    Return
    ---------
    input_text: str
        The content of user's input.
    '''
    textSlide(preText)
    text = preText
    while 1:
        inkey = waitForResponse(hasRT=False)
        if inkey == K_RETURN:
            break
        elif inkey == K_BACKSPACE:
            text = text[0:-1]
        elif inkey <= 127:
            text += (chr(inkey))
        textSlide(text)
    input_text = text[len(preText):]
    clear()
    return input_text

def instruction(instructionText, hasPractice=False):
    '''
    Show the instruction of experiment
    (press 'left' to back, 'right' to continue)

    Parameters
    ----------
    instructionText：list of str
        The text that will be displayed as instruction.

    Return
    ---------
    resp: Keyname/int
        The last pressed key name.
    '''
    intro = '\n'.join(instructionText).split('>\n')
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

        resp = waitForResponse(hasRT=False)
        if resp == K_LEFT and i > 0:
            i -= 1
        elif resp == K_RIGHT and i < len(intro) - 1:
            i += 1
        elif resp in [K_SPACE, K_RETURN] and i == len(intro) - 1:
            clear()
            return resp

def tip(text, allowedKeys=[K_SPACE, K_RETURN], outTime=0):
    '''
    Display a new text slide right now, and keep the screen until user's response.

    Parameters
    ----------
    text：str
        The text on the screen.
    allowedKeys: Keyname, or list of Keyname (default:[K_SPACE, K_RETURN])
        The allowed user's response.
    outTime: int(>0) or 0(default)
        The display time limitation of this function.
        
    Return
    ---------
    resp: Keyname/int
        The last pressed key name.
    '''
    textSlide(text)
    resp = waitForResponse(allowedKeys, outTime, hasRT=False)
    clear()
    return resp

def alertAndGo(text, outTime=3000):
    '''
    Display a new text slide right now, 
    and keep the screen in a given period of time, or until user pressed SPACE or K_RETURN

    Parameters
    ----------
    text：str
        The text on the screen.
    outTime: int(>0) or 0(default)
        The display time limitation of this function.
        
    Return
    ---------
    None
    '''
    tip(text, outTime=outTime)

def alertAndQuit(text, outTime=3000):
    '''
    Display a new text slide right now, 
    and keep the screen in a given period of time, or until user pressed SPACE or K_RETURN,
    then quit the program.

    Parameters
    ----------
    text：str
        The text on the screen.
    outTime: int(>0) or 0(default)
        The display time limitation of this function.
        
    Return
    ---------
    None
    '''
    alertAndGo(text, outTime)
    shared.pg.quit()

def restTime(text='现在实验暂停一会儿，您可以放松一下\n如果休息好了请按 [空格键] 开始实验。'):
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
    shared.pg.time.wait(3000)
    tip(text, K_SPACE)
