# coding:utf-8
import sys
# sys.path.append('../../')
sys.path = ['../../']+sys.path

from expy import *  # Import the needed functions
start(mouse_visible=True)  # Initiate the experiment environment

# drawText('请按下键盘上的任意键')  # Draw text on the canvas and display it
# pressAndChange(allowed_keys={key_.K: 'K', key_.J: 'J'}, out_time=5)
# while 1:
#     # t = shared.pressing
#     # print(t)
#     show(0.01)

drawText('请按下键盘上的任意键')  # Draw text on the canvas and display it
key,rt = waitForResponse()  # Waiting for pressing and get the pressed key
alertAndGo('您刚刚按下了%d，用时: %fs' % (key, rt))  # Display the keypress

'Key limited by "allowed_keys". Please look into "Key mapping" for some detail'
drawText('除了键盘上的K或J，别的按键都不会起作用')  # Draw text on the canvas and display it
key,rt = waitForResponse([key_.K, key_.J])  # Waiting for pressing 'K' or 'J', and get the pressed key's id.
alertAndGo('您刚刚按下了%s，用时: %fs' % (key,rt))  # Display the keypress

drawText('除了键盘上的K或J，别的按键都不会起作用')  # Draw text on the canvas and display it
key,rt = waitForResponse({key_.K: 'K', key_.J: 'J'})  # Waiting for pressing 'K' or 'J', and get the pressed key's name.
alertAndGo('您刚刚按下了%s，用时: %fs' % (key,rt))  # Display the keypress

drawText('除了键盘上的K，别的按键都不会起作用')  # Draw text on the canvas and display it
key,rt = waitForResponse(key_.K)  # Waiting for pressing 'K', and get the pressed key's id.
alertAndGo('您刚刚按下了%d，用时: %fs' % (key,rt))  # Display the keypress

'Time limited by "out_time"'
drawText('请在1秒内按下键盘上的K或J')  # Draw text on the canvas and display it
key,rt = waitForResponse({key_.K: 'K', key_.J: 'J'}, out_time=1)  # Waiting for pressing 'K' or 'J' in 1s.
if type(rt)==int:
    alertAndGo('您刚刚按下了%s，用时: %fs' % (key,rt))  # Display the keypress
else:
    alertAndGo('超时')

'Get only key without RT) by falsing the "has_RT"'
drawText('请按下键盘上的K或J')  # Draw text on the canvas and display it
key = waitForResponse({key_.K: 'K', key_.J: 'J'}, has_RT=False)  # Waiting for pressing 'K' or 'J', no RT returned.
alertAndGo('您刚刚按下了' + key) # Display the keypress

drawText('请按下键盘上的K或J，并过一会再松开')  # Draw text on the canvas and display it
key, (RT, pressed_time) = waitForResponse([key_.K, key_.J], action_while_pressing=(print,0))
alertAndGo('您刚刚按下了%d，按键前用时: %fs，按键用时%fs' % (key, RT, pressed_time))  # Display the keypress

drawText('请用鼠标左键点击方块',y=-0.5)  # Draw text on the canvas and display it
drawRect(w =0.1, h=0.1, color=C_white) # Draw a button
(button, (x, y)), rt = waitForResponse(allowed_clicks=ClickRange((-0.1,0.1),(-0.1,0.1),mouse_.LEFT))  # Waiting for mouse click and get the click
alertAndGo('您刚刚在（X=%d，Y=%d）处按下了%d，用时: %fs' % (x, y, button, rt))  # Display the event