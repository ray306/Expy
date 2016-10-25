from expy import shared
from .draw import *

# clear the screen
# 清空屏幕上的显示
def clear():
    shared.win.fill(shared.bgColor)
    shared.pg.display.flip()

# 将buffer中的内容输出到屏幕，keep the display for a period
# 【参数】 outTime: 停留的时间，cleanScreen: 最后是否清空屏幕
# 依赖clear()
def show(outTime=False,cleanScreen=True):
    shared.pg.display.flip()
    if outTime:
        waitForResponse({}, outTime)
        if cleanScreen:
            clear()