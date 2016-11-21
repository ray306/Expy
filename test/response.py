# coding:utf-8
import sys
sys.path.append('../../')

from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

drawText('请按下键盘上的任意键')  # Draw text on the canvas and display it
key, rt = waitForResponse()  # Waiting for pressing and get the pressed key.
alertAndGo('您刚刚按下了%d，用时：%dms' % (key, rt))  # Display the keypress

'Key limited by "allowed_keys". Please look into "Key mapping" for some detail'
drawText('除了键盘上的K或J，别的按键都不会起作用')  # Draw text on the canvas and display it
key, rt = waitForResponse([K_k, K_j])  # Waiting for pressing 'K' or 'J', and get the pressed key's id.
alertAndGo('您刚刚按下了%s，用时：%dms' % (key, rt))  # Display the keypress

drawText('除了键盘上的K或J，别的按键都不会起作用')  # Draw text on the canvas and display it
key, rt = waitForResponse({K_k: 'K', K_j: 'J'})  # Waiting for pressing 'K' or 'J', and get the pressed key's name.
alertAndGo('您刚刚按下了%d，用时：%dms' % (key, rt))  # Display the keypress

drawText('除了键盘上的K，别的按键都不会起作用')  # Draw text on the canvas and display it
key, rt = waitForResponse(K_k)  # Waiting for pressing 'K', and get the pressed key's id.
alertAndGo('您刚刚按下了%d，用时：%dms' % (key, rt))  # Display the keypress

'Time limited by "out_time"'
drawText('请在1秒内按下键盘上的K或J')  # Draw text on the canvas and display it
key, rt = waitForResponse({K_k: 'K', K_j: 'J'}, out_time=1000)  # Waiting for pressing 'K' or 'J' in 1000ms.
alertAndGo('您刚刚按下了%s，用时：%dms' % (key, rt))  # Display the keypress

'Get only key(without RT) by falsing the "has_RT"'
drawText('请按下键盘上的K或J')  # Draw text on the canvas and display it
key = waitForResponse({K_k: 'K', K_j: 'J'}, has_RT=False)  # Waiting for pressing 'K' or 'J', no RT returned.
alertAndGo('您刚刚按下了' + key)  # Display the keypress
