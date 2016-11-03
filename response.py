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
    onset = shared.pg.time.get_ticks()

    backup = shared.pg.display.get_surface().convert()
    
    shared.win.fill(shared.backgroundColor)
    target = shared.font['normalFont'].render('[程序暂停中/Pause]', True, shared.fontColor)
    shared.win.blit(target, 
        ((shared.winWidth-target.get_width())/2, (shared.winHeight-target.get_height())/2))
    shared.pg.display.flip()

    waitForResponse(K_F12, suspending=True)

    shared.win.blit(backup,(0,0))
    shared.pg.display.flip()

    return shared.pg.time.get_ticks()-onset

# waiting for a response during a limited period and recording it
# 等待被试按键，超过设定时间自动结束
# 【参数】 allowedKeys：容许的按键（可有多个）
# 【参数】 outTime：超过这个时间就不再等待，进入下一步
# 【参数】 hasRT：
# 【返回值】按键&反应时 （hasRT is True）, 按键 （hasRT is False）
# 【返回值】1.如果设置了一个respKey，返回True
# 【返回值】2.如果没有设置respKey，或有多个respKey，则返回实际按键的编号）
# 【返回值】3.如果按下ESC，则直接退出程序
# 【返回值】4.如果没有按键会返回None
# 【Note】Press F12 could suspend the procedure
def waitForResponse(allowedKeys=None, outTime=0, hasRT=True, suspending=False):
    def wait(keys,mapping,startT,outTime):
        while True:
            pastTime = shared.pg.time.get_ticks() - startT
            if outTime>0 and pastTime >= outTime:
                return 'None', 'None'
            for e in shared.pg.event.get():
                'get the pressed key'
                # k = 0
                if e.type == KEYDOWN:
                    k = e.key
                elif e.type == JOYBUTTONDOWN:
                    k = e.button
                elif e.type == MOUSEBUTTONDOWN: # e.type == MOUSEMOTION, k = e.pos
                    k = e.button
                else:
                    continue

                'decision'
                if k == 27:
                    shared.pg.quit()
                elif k == K_F12 and not suspending:
                    suspendTime = suspend()
                    startT += suspendTime
                elif not keys:
                    return k, pastTime
                elif k in keys: # if the allowedKeys hasn't set
                    return mapping[k], pastTime

            time.sleep(0.001)

    startT = shared.pg.time.get_ticks()
    shared.pg.event.clear()
    keys,mapping = setKeyMapping(allowedKeys) # make an allowable key list, and a key mapping

    KEY,pastTime = wait(keys,mapping,startT,outTime)
    if hasRT:
        return KEY,pastTime
    else:
        return KEY