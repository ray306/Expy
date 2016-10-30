from pygame.locals import *
import time
from expy import shared

'''Response class'''
# make an allowable key list, and a key mapping
def setKeyMapping(allowedKeys):
    keys = allowedKeys
    mapping = allowedKeys
    if type(allowedKeys)==dict: # eg. allowedKeys = {K_f: 'T', K_j: 'F'}
        keys = list(allowedKeys.keys())
    elif type(allowedKeys)==list: # eg. allowedKeys = [K_f, K_j]
        mapping = {k:k for k in allowedKeys}
    elif type(allowedKeys)==int: # eg. allowedKeys = K_ENTER
        keys = [allowedKeys]
        mapping = {allowedKeys:allowedKeys}
    return keys,mapping

def suspend():
    backup = shared.pg.display.get_surface().convert()
    
    shared.win.fill(shared.backgroundColor)
    target = shared.font['normalFont'].render('[程序暂停/Paused]', True, shared.fontColor)
    shared.win.blit(target, 
        ((shared.winWidth-target.get_width())/2, (shared.winHeight-target.get_height())/2))
    shared.pg.display.flip()

    waitForEvent()
    shared.win.blit(backup,(0,0))
    shared.pg.display.flip()

# hold on until a event coming, if the respKeys hasn't set, return the key (usually be used as 'next' button)
# 等待被试按键
# 【参数】 allowedKeys：容许的按键
# 【返回值】1.如果设置了一个respKey，返回True
# 【返回值】2.如果没有设置respKey，或有多个respKey，则返回实际按键的编号）
# 【返回值】3.如果按下ESC，则直接退出程序
def waitForEvent(allowedKeys=None):
    # make an allowable key list, and a key mapping
    keys,mapping = setKeyMapping(allowedKeys)

    shared.pg.event.clear()
    while True:
        for e in shared.pg.event.get():
            # get the pressed key
            k = 0
            if e.type == KEYDOWN:
                k = e.key
            elif e.type == JOYBUTTONDOWN:
                k = e.button
            else:
                continue
            # decision
            if k == 27:
                shared.pg.quit()
            elif k == K_F12:
                suspend()
            elif not keys: # if the allowedKeys hasn't set
                return k
            elif k in keys:
                if len(keys)>1: 
                    return mapping[k]
                else: 
                    return True
            
        time.sleep(0.001)

# waiting for a response during a limited period and recording it
# 等待被试按键，超过设定时间自动结束
# 【参数】 respKeys：容许的按键（可有多个）； outTime：超过这个时间就不再等待，进入下一步
# 【返回值】按键，反应时 （没有按键会返回None,None）
def waitForResponse(allowedKeys=None, outTime=0):
    startT = shared.pg.time.get_ticks()
    endT = outTime+startT

    # make an allowable key list, and a key mapping
    keys,mapping = setKeyMapping(allowedKeys)

    shared.pg.event.clear()
    while True:
        if outTime>0 and shared.pg.time.get_ticks() >= endT:
            return 'None', 'None'
        for e in shared.pg.event.get():
            # get the pressed key
            k = 0
            if e.type == KEYDOWN:
                k = e.key
            elif e.type == JOYBUTTONDOWN:
                k = e.button
            elif e.type == MOUSEBUTTONDOWN:
                k = e.button
            # elif e.type == MOUSEMOTION:
            #     k = e.pos
            else:
                continue
            # decision
            if k == 27:
                shared.pg.quit()
            elif k == K_F12:
                suspend()
            elif not keys: # if the allowedKeys hasn't set
                return k, shared.pg.time.get_ticks() - startT
            elif k in keys:
                if len(keys)>1: 
                    return mapping[k], shared.pg.time.get_ticks() - startT
                else: 
                    return True, shared.pg.time.get_ticks() - startT

        time.sleep(0.001)

# def waitForResp(respKeys, outTime):
#     shared.pg.event.clear()
#     startT = shared.pg.time.get_ticks()
#     endT = outTime+startT
#     while True:
#         if shared.pg.time.get_ticks() >= endT:
#             return 'None', 'None'
#         for e in shared.pg.event.get():
#             if e.type == KEYDOWN and e.key in respKeys.keys():
#                 respT = shared.pg.time.get_ticks() - startT
#                 return respKeys[e.key], respT
#             elif e.type == KEYDOWN and e.key == 27:
#                 shared.pg.quit()
#         time.sleep(0.001)