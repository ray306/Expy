from pygame.locals import *

from expy import shared
from .stim.draw import *
from .stim.display import *
from .io import *
from .response import *

'''Advanced draw class'''
# display text right now
# 在一个新页面上显示text的内容
# 依赖drawText()
def textSlide(text, bgImage=None):
    shared.win.fill(shared.bgColor)
    drawText(text,shared.font['nFont'])
    if bgImage: drawPic(path)
    shared.pg.display.flip()

# 获取被试输入的信息
# 【参数】 preText：屏幕上预先出现的内容
# 【返回值】被试的输入
def getInput(preText):
    textSlide(preText)
    text = preText
    while 1:
        inkey = waitForEvent([])
        if inkey == K_RETURN:
            break
        elif inkey == K_BACKSPACE:
            text = text[0:-1]
        elif inkey <= 127:
            text += (chr(inkey))
        textSlide(text)
    return text[len(preText):]

# display the introduction of the experiment (press 'left' to back, 'right' to continue)
# 显示指导语introductionText，可分页面显示（introductionText列表有多长就显示几页）
# 依赖textSlide()、 waitForEvent()
def introduction(introductionText,hasPractice=False):
    intro = '\n'.join(introductionText).split('>\n')
    i = 0
    while True:
        if intro[i] == '[demo]':
            demo()
            i+=1
            continue

        if i==0:
            textSlide(intro[i]+'\n\n(按方向键“→”进入下一页)')
        elif i==len(intro)-1:
            if hasPractice:
                textSlide(intro[i]+'\n\n(按方向键“←”返回上一页，按 [回车键] 开始练习. \n如果要跳过练习，请按 [空格] )')
            else:
                textSlide(intro[i]+'\n\n(按方向键“←”返回上一页，按 [空格] 开始实验. )')
        else:
            textSlide(intro[i]+'\n\n(按方向键“←”返回上一页，按方向键“→”进入下一页)')
        
        resp = waitForEvent()
        if resp == K_LEFT and i > 0:
            i-=1
        elif  resp == K_RIGHT and i < len(intro)-1:
            i+=1
        elif  resp in [K_SPACE,K_RETURN] and i == len(intro)-1:
            return resp

# display the tip during experiment (press 'blank' to continue)
# 显示一个实验提示tip，然后等待被试按键确认
# 依赖textSlide()、 waitForEvent()、 clear()
def tip(text):
    textSlide(text)
    while 1:
        resp = waitForEvent()
        if resp in [K_SPACE,K_RETURN]:
            break
    clear()
    return resp

# display message and quit after some time
# 显示一个实验提示（出错警告或实验结束提示），2.5秒后自动退出程序
# 依赖textSlide()
def alertAndQuit(text,outTime=2500):
    textSlide(text)
    shared.pg.time.wait(outTime)
    shared.pg.quit()

# 显示一个实验提示，一段时间后自动消失并继续程序
# 依赖textSlide()
def alertAndGo(tipText, outTime):
    textSlide(tipText)
    show(outTime)

# 表示休息时间，用空格键结束（可用F12暂停，回车恢复）
# 依赖tip()
def restTime():
    shared.pg.time.wait(3000)
    while 1:
        resp = tip('现在实验暂停一会儿，您可以放松一下~\n如果休息好了请按 [空格键] 开始实验。')
        if resp == K_SPACE:
            break