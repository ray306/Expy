# coding:utf-8
import sys
sys.path.append('../../')

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

drawText('请按下键盘上的任意键')  # Draw text on the canvas and display it
key,rt = waitForResponse()  # Waiting for pressing and get the pressed key
alertAndGo('您刚刚按下了%d，用时：%dms' % (key, rt))  # Display the keypress

'Key limited by "allowed_keys". Please look into "Key mapping" for some detail'
drawText('除了键盘上的K或J，别的按键都不会起作用')  # Draw text on the canvas and display it
key,rt = waitForResponse([key_.K, key_.J])  # Waiting for pressing 'K' or 'J', and get the pressed key's id.
alertAndGo('您刚刚按下了%s，用时：%dms' % (key,rt))  # Display the keypress

drawText('除了键盘上的K或J，别的按键都不会起作用')  # Draw text on the canvas and display it
key,rt = waitForResponse({key_.K: 'K', key_.J: 'J'})  # Waiting for pressing 'K' or 'J', and get the pressed key's name.
alertAndGo('您刚刚按下了%s，用时：%dms' % (key,rt))  # Display the keypress

drawText('除了键盘上的K，别的按键都不会起作用')  # Draw text on the canvas and display it
key,rt = waitForResponse(key_.K)  # Waiting for pressing 'K', and get the pressed key's id.
alertAndGo('您刚刚按下了%d，用时：%dms' % (key,rt))  # Display the keypress

'Time limited by "out_time"'
drawText('请在1秒内按下键盘上的K或J')  # Draw text on the canvas and display it
key,rt = waitForResponse({key_.K: 'K', key_.J: 'J'}, out_time=1000)  # Waiting for pressing 'K' or 'J' in 1000ms.
if type(rt)==int:
    alertAndGo('您刚刚按下了%s，用时：%dms' % (key,rt))  # Display the keypress
else:
    alertAndGo('超时')

'Get only key without RT) by falsing the "has_RT"'
drawText('请按下键盘上的K或J')  # Draw text on the canvas and display it
key = waitForResponse({key_.K: 'K', key_.J: 'J'}, has_RT=False)  # Waiting for pressing 'K' or 'J', no RT returned.
alertAndGo('您刚刚按下了' + key) # Display the keypress



# import win32api
# import win32con
# from threading import Thread

# from multiprocessing import Process, Queue

# import time

# # def press():
# #     import win32api
# #     import win32con
# #     import time
# #     now = time.time()
# #     while 1:
# #         if time.time()-now>1:
# #             win32api.keybd_event(49,0,0,0)
# #             win32api.keybd_event(49,0,win32con.KEYEVENTF_KEYUP,0) 
# #             now = time.time()
# #         time.sleep(0.001)

# # t = Process(target=press)
# # t.start()

# drawText('请按下键盘上的K或J')
# show()
# while 1:
#     shared.win.dispatch_events()
    
#     for e in shared.events:
#         print(e['time'])
#         shared.events = []
#     time.sleep(0.001)


