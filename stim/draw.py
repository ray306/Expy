import numpy as np
import pygame as pg

from expy import shared
from expy.colors import *


def getPos(x=shared.winWidth // 2, y=shared.winHeight // 2, w=0, h=0, benchmark='center'):
    '''
    Caluate the screen position of object

    Parameters
    ----------
    x: float or int (default: shared.winWidth // 2)
        If x is float, it represents the x-offset(-1~1 scale) from the object benchmark to the screen center,
        if int, it represents the x-offset(pixel) from the object benchmark to the screen upperleft.
    y: float or int (default: shared.winHeight // 2)
        Similar with x
    w: float or int (default: 0)
        If w is float, it represents the width scale on screen,
        if int, it represents the width in pixel.
    h: float or int (default: 0)
        Similar with x
    benchmark: 'center'(default), 
               'upper_left', 'upper_right', 'lower_left', 'lower_right', 
               'upper_center', 'left_center', 'lower_center', 'right_center'
        The position benchmark on this object to the given x and the given y. 

    Returns
    -------
    (x,y): (int,int)
        The position of the object's upperleft corner

    '''
    if type(x) is float:
        x, y = (0.5 + x / 2) * \
            shared.winWidth, (0.5 + y / 2) * shared.winHeight
    if w < 1:
        w, h = w * shared.winWidth, h * shared.winHeight

    if benchmark == 'center':
        return int(x - w / 2), int(y - h / 2)
    elif benchmark == 'upper_left':
        return int(x), int(y)
    elif benchmark == 'upper_right':
        return int(x - w), int(y)
    elif benchmark == 'lower_left':
        return int(x), int(y - h)
    elif benchmark == 'lower_right':
        return int(x - w), int(y - h)
    elif benchmark == 'upper_center':
        return int(x - w / 2), int(y)
    elif benchmark == 'left_center':
        return int(x), int(y - h / 2)
    elif benchmark == 'lower_center':
        return int(x - w / 2), int(y - h)
    elif benchmark == 'right_center':
        return int(x - w), int(y - h / 2)
    raise ValueError('Unsupported position benchmark')


# def drawText(text, fontname='stimFont', x=0.0, y=0.0, benchmark='center', display=True):
#     '''
#     Draw text on the canvas. The text will show as multiple lines splited by the '\n'. 

#     Parameters
#     ----------
#     todo

#     Returns
#     -------
#     None
#     '''
#     FONT = shared.font[fontname]

#     if not '\n' in text:
#         target = FONT.render(text, True, shared.fontColor)
#         x, y = getPos(x, y, w=target.get_width(),
#                       h=target.get_height(), benchmark=benchmark)
#         shared.win.blit(target, (x, y))

#     else:
#         lines = text.split('\n')

#         targets = [FONT.render(l, True, shared.fontColor) for l in lines]
#         maxWidth = max([t.get_width() for t in targets])
#         for ind, target in enumerate(targets):
#             y_offset = (len(lines) - 1 - ind * 2) * (target.get_height() / shared.winHeight)
#             pos_x, pos_y = getPos(x, y - y_offset, w=maxWidth, h=0, benchmark=benchmark)
#             shared.win.blit(target, (pos_x, pos_y))

#     if display:
#         shared.pg.display.flip()

def drawText(text, font='simhei', size=25, color=C_white, x=0.0, y=0.0, benchmark='center', display=True):
    '''
    Draw text with complex format on the canvas. The text will show as multiple lines splited by the '\n'. 

    Parameters
    ----------
    todo

    Returns
    -------
    None
    '''
    'assign value'
    if (type(size) is str) and (size in shared.font):
        size = shared.font[size]
    elif (type(size) is int) and (size > 0):
        pass
    else:
        raise ValueError(str(size) + ' cannot be regarded as a font size')

    if font in shared.font:
        FONT = shared.font[font]
    else:
        raise ValueError(font + ' cannot be regarded as a font')

    'draw'
    if not '\n' in text:
        target, (left, top, w, h) = FONT.render(text, fgcolor=color, size=(size, size))
        pos_x, pos_y = getPos(x, y, w, h, benchmark=benchmark)
        shared.win.blit(target, (pos_x, pos_y))
    else:
        lines = text.split('\n')
        rendered = [FONT.render(l, fgcolor=color, size=(size, size)) for l in lines]
        maxWidth = max([w for target, (left, top, w, h) in rendered])

        for ind, (target, (left, top, w, h)) in enumerate(rendered):
            y_offset = (len(lines) - 1 - ind * 2) * (h / shared.winHeight)
            pos_x, pos_y = getPos(x, y - y_offset, w=maxWidth, h=0, benchmark=benchmark)
            shared.win.blit(target, (pos_x, pos_y))

    if display:
        shared.pg.display.flip()


def drawRect(w, h, x=0.0, y=0.0, fill=True, color=C_white, width=1, benchmark='center', display=True):
    '''
    Draw rectangle on the canvas.

    Parameters
    ----------
    todo

    Returns
    -------
    None
    '''
    x, y = getPos(x, y, w=w, h=h, benchmark=benchmark)
    #colour, (x, y), size, thickness
    if fill:
        width = 0
    shared.pg.draw.rect(shared.win, color, (x, y, w, h), width)

    if display:
        shared.pg.display.flip()


def drawCircle(r, x=0.0, y=0.0, fill=True, color=C_white, width=1, benchmark='center', display=True):
    '''
    Draw circle on the canvas.

    Parameters
    ----------
    todo

    Returns
    -------
    None
    '''
    x, y = getPos(x, y, w=0, h=0, benchmark=benchmark)
    if fill:
        width = 0
    shared.pg.draw.circle(shared.win, color, (x, y), r, width)

    if display:
        shared.pg.display.flip()


def drawLine(points, color=C_white, width=1, display=True):
    '''
    Draw line(s) on the canvas.

    Parameters
    ----------
    todo

    Returns
    -------
    None
    '''
    shared.pg.draw.lines(shared.win, color, False, points, width)

    if display:
        shared.pg.display.flip()


def drawPic(path, w=0, h=0, x=0.0, y=0.0, rotate=0, benchmark='center', display=True):
    '''
    Draw picture on the canvas.

    Parameters
    ----------
    todo

    Returns
    -------
    None
    '''
    im = shared.pg.image.load(path).convert()
    if rotate != 0:
        im = shared.pg.transform.rotate(im, rotate)
    if w > 0 and h > 0:
        im = shared.pg.transform.scale(im, (w, h))
    else:
        w, h = im.get_rect().size
    x, y = getPos(x, y, w, h, benchmark=benchmark)
    shared.win.blit(im, (x, y))

    if display:
        shared.pg.display.flip()
