import numpy as np
import pygame as pg

from expy import shared

# caluate the screen position of object
# x: if x is float, it represents the x-offset(-1~1 scale) from the object benchmark to the screen center,
#            if int, it represents the x-offset(pixel) from the object benchmark to the screen upperleft.
# y: similar with x
# w: if w is float, it represents the width scale on screen,
#     if int, it represents the width in pixel.
# h: similar with w
# return position of the object's upperleft corner


def getPos(x=shared.winWidth // 2, y=shared.winHeight // 2, w=0, h=0, benchmark='center'):
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

'''Basic draw class'''
# draw text
# 将text的内容生成并放入缓存，text可分行显示（由‘\n’分行）


def drawText(text, fontname='stimFont', x=0.0, y=0.0, benchmark='center', display=True):
    if not '\n' in text:
        target = shared.font[fontname].render(text, True, shared.fontColor)
        x, y = getPos(x, y, w=target.get_width(),
                      h=target.get_height(), benchmark=benchmark)
        shared.win.blit(target, (x, y))

    else:
        lines = text.split('\n')
        lineN = len(lines)

        font = shared.font[fontname]
        targets = [font.render(l, True, shared.fontColor) for l in lines]
        maxLen = max([t.get_width() for t in targets])
        for ind, target in enumerate(targets):
            y_offset = (lineN - 1 - ind * 2) * \
                (target.get_height() / shared.winHeight)
            pos_x, pos_y = getPos(x, y - y_offset, w=maxLen,
                                  h=0, benchmark=benchmark)
            shared.win.blit(target, (pos_x, pos_y))
    if display:
        shared.pg.display.flip()

# draw text with complex format


def drawFormattedText(text, fontname='stimFont', size=15, x=0.0, y=0.0, benchmark='center', display=True):
    FONT = shared.font['ft']
    FONT.underline = True

    x, y = getPos(x, y, w=size * len(text), h=size, benchmark=benchmark)
    FONT.render_to(shared.win, (x, y), text, size=(size, size))

    if display:
        shared.pg.display.flip()

# draw a square
# 屏幕中央显示一个方块


def drawRect(w, h, x=0.0, y=0.0, fill=True, color=(255, 255, 255), width=1, benchmark='center', display=True):
    x, y = getPos(x, y, w=w, h=h, benchmark=benchmark)
    #colour, (x, y), size, thickness
    if fill:
        width = 0
    shared.pg.draw.rect(shared.win, color, (x, y, w, h), width)

    if display:
        shared.pg.display.flip()

# draw circle


def drawCircle(r, x=0.0, y=0.0, fill=True, color=(255, 255, 255), width=1, benchmark='center', display=True):
    x, y = getPos(x, y, w=0, h=0, benchmark=benchmark)
    if fill:
        width = 0
    shared.pg.draw.circle(shared.win, color, (x, y), r, width)

    if display:
        shared.pg.display.flip()

# draw line


def drawLine(points, color=(255, 255, 255), width=1):
    shared.pg.draw.lines(shared.win, color, False, points, width)

    if display:
        shared.pg.display.flip()

# draw picture


def drawPic(path, w=0, h=0, x=0.0, y=0.0, rotate=0, benchmark='center', display=True):
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
