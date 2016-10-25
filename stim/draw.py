import numpy as np
import pygame as pg

from expy import shared

# caluate the screen position of object
# center_x: if center_x is float, it represents the x-offset(-1~1 scale) from object center to screen center,
#            if int, it represents the x-offset(pixel) from object center to screen upper-left.
# center_y: similar with center_x
# w: if w is float, it represents the width scale on screen,
#     if int, it represents the width in pixel.
# h: similar with w
def getPos(center_x=shared.winWidth//2,center_y=shared.winHeight//2,w=0,h=0):
    if type(center_x) is float:
        center_x, center_y = (0.5+center_x/2)*shared.winWidth, (0.5+center_y/2)*shared.winHeight
    if type(w) is float:
        w, h = w*shared.winWidth, h*shared.winHeight
    return int(center_x-w/2),int(center_y-h/2)

'''Basic draw class'''
# a central fixation
# 屏幕中央显示一个红点
def drawFix(size): 
    x,y = getPos(w=size,h=size)
    shared.pg.draw.circle(shared.win, (128,0,0), (x,y), size)
    # shared.pg.draw.line(win, fixColor, (shared.winWidth / 2 - length/2, shared.winHeight / 2) , (shared.winWidth / 2 + length/2, shared.winHeight / 2), width=1)
    # shared.pg.draw.line(win, fixColor, (shared.winWidth / 2, shared.winHeight / 2 - length/2) , (shared.winWidth / 2, shared.winHeight / 2 + length/2) , width=1)

# draw word at screen center
# 将text的内容生成并放入缓存 ，只能显示一行
def drawWord(text,x=0.0, y=0.0):
    target = shared.font['sFont'].render(text, True, shared.fontColor)
    x,y = getPos(x,y,w=target.get_width(), h=target.get_height())
    shared.win.blit(target, (x, y))

def drawWordWithLine(text,linePos):
    target = shared.font['sFont'].render(text, True, shared.fontColor)
    x,y = getPos(w=target.get_width(), h=target.get_height())
    shared.win.blit(target, (x,y))

    y = shared.winHeight / 2 + target.get_height() / 2 + 5
    w = shared.winWidth
    if linePos == 0:
        linePosStart = [(w - target.get_width())/2, y]
        linePosEnd = [(w + target.get_width())/2, y]
    if linePos == 1:
        linePosStart = [(w - target.get_width())/2, y]
        linePosEnd = [w / 2, y]
    elif linePos == 2:
        linePosStart = [w / 2, y]
        linePosEnd = [(w + target.get_width())/2, y]
    shared.pg.draw.line(shared.win, shared.fontColor, linePosStart, linePosEnd, 2)

# draw sentences in more than one line
# 将text的内容生成并放入缓存，text可分行显示（由‘\n’分行）
def drawText(text, font, pos='center'):
    lines = text.split('\n')
    maxLen = max([len(l) for l in lines])*shared.font['nSize']
    lineN = len(lines)
        
    for ind,l in enumerate(lines):
        target = font.render(l, True, shared.fontColor)
        if pos=='center':
            x,y = getPos(w=maxLen, h=(ind*2-lineN)*target.get_height())
            shared.win.blit(target, (x, y))
        elif pos == 'LU':
            x,y = getPos(-0.9, -0.9, 0, 0)
            shared.win.blit(target, (x, y+ind*target.get_height()))
        elif pos == 'RU':
            x,y = getPos(0.9, -0.9, 0, 0)
            shared.win.blit(target, (x-maxLen, y+ind*target.get_height()))
        elif pos == 'LD':
            x,y = getPos(-0.9, 0.9, 0, 0)
            shared.win.blit(target, (x, y-(lineN-ind)*target.get_height()))
        elif pos == 'RD':
            x,y = getPos(0.9, 0.9, 0, 0)
            shared.win.blit(target, (x-maxLen, y-(lineN-ind)*target.get_height()))

# draw a square
# 屏幕中央显示一个方块
def drawRect(w, h, x=0.0, y=0.0, fill=True, color=(255,255,255), width=1):
    x,y = getPos(w=w, h=h)
    #colour, (x, y), size, thickness
    if fill:
        width = 0
    shared.pg.draw.rect(shared.win, color, (x, y, size,size), width)

# draw circle
def drawCircle(r, x=0.0, y=0.0, fill=True, color=(255,255,255), width=1):
    x,y = getPos(w=r*2, h=r*2)
    if fill:
        width = 0
    shared.pg.draw.circle(shared.win, color, x, y, size, width)

# draw picture
def drawPic(path, w=0, h=0, x=0.0, y=0.0):
    im = shared.pg.image.load(path).convert()
    if w>0 and h>0:
        im = shared.pg.transform.scale(im, (w,h))
    else:
        w,h = im.get_rect().size
    x,y = getPos(x,y,w,h)
    shared.win.blit(im, (x,y))

# draw line
def drawLine(points, color=(255,255,255), width=1):
    shared.pg.draw.lines(shared.win, False, points, color, width)