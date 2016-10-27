# coding:utf-8
import sys
sys.path.append('../../')

from expy import * # Import the needed functions
start() # Initiate the experiment environment

'Please look into "Key mapping" for some detail'

'Only key'
drawWord('请按下键盘上的任意键') # Draw text on the canvas
show() # Display current canvas
key = waitForEvent() # Waiting for pressing and get the pressed key.
alertAndGo('您刚刚按下了'+str(key)) # Show the keypress

# Please look into "Key mapping" for some detail
drawWord('除了键盘上的K，别的按键都不会起作用') # Draw text on the canvas
show() # Display current canvas
key = waitForEvent(K_k) # Waiting for pressing "K"
clear()

drawWord('请按下键盘上的K或J') # Draw text on the canvas
show() # Display current canvas
key = waitForEvent({K_k:'K',K_j:'J'}) # Waiting for pressing 'K' or 'J', and get the pressed key.
alertAndGo('您刚刚按下了'+key) # Print the keypress


'With response time'
drawWord('请按下键盘上的K或J') # Draw text on the canvas
show() # Display current canvas
key,rt = waitForResponse({K_k:'K',K_j:'J'}) # Waiting for pressing 'K' or 'J', and get the pressed key.
alertAndGo('您刚刚按下了'+key+'，用时：'+str(rt)) # Print the keypress

drawWord('请在1秒内按下键盘上的K或J') # Draw text on the canvas
show() # Display current canvas
key,rt = waitForResponse({K_k:'K',K_j:'J'}, outTime=1000) # Waiting for pressing 'K' or 'J' in 1000ms, and get the pressed key.

alertAndGo('您刚刚按下了'+key+'，用时：'+str(rt)) # Print the keypress


