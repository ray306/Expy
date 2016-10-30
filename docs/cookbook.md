# Cookbook
---
## *Experiment Initiation*
```python
from expy import * # Import the needed functions
start() # Initiate the experiment environment
```

## *Experiment Structure*
A standard experiment contains 3 levels:

- Run(Session)
- Block
- Trial
  So we suggest that your code should have hierarchical structure, as the example below：
```python
from expy import *
start()

def trial(stim):
    draw(stim)
    show(1000)

def block(trialList):
    for stim in trialList:
        trial(stim)
        
def run():
    for trialList in blockList:
        block(trialList)

run()
```

## *Response*
```python
'With response time'
drawText('请按下键盘上的K或J') # Draw text on the canvas
show() # Display current canvas
'''General usage'''
key,rt = waitForResponse({K_k:'K',K_j:'J'}) # Waiting for pressing 'K' or 'J', and get the pressed key.
''''''
alertAndGo('您刚刚按下了'+key+'，用时：'+str(rt)) # Print the keypress

drawText('请在1秒内按下键盘上的K或J') # Draw text on the canvas
show() # Display current canvas
key,rt = waitForResponse({K_k:'K',K_j:'J'}, outTime=1000) # Waiting for pressing 'K' or 'J' in 1000ms, and get the pressed key.

alertAndGo('您刚刚按下了'+key+'，用时：'+str(rt)) # Print the keypress


'Only key'
drawText('请按下键盘上的任意键') # Draw text on the canvas
show() # Display current canvas
key = waitForEvent() # Waiting for pressing and get the pressed key.
alertAndGo('您刚刚按下了'+str(key)) # Show the keypress

# Please look into "Key mapping" for some detail
drawText('除了键盘上的K，别的按键都不会起作用') # Draw text on the canvas
show() # Display current canvas
key = waitForEvent(K_k) # Waiting for pressing "K"
clear()

drawText('请按下键盘上的K或J') # Draw text on the canvas
show() # Display current canvas
key = waitForEvent({K_k:'K',K_j:'J'}) # Waiting for pressing 'K' or 'J', and get the pressed key.
alertAndGo('您刚刚按下了'+key) # Print the keypress
```

## *Visual Experiment*
### Show text
```python
'''General usage'''
drawText('Hello world!') # Draw text on the canvas
show(3000) # Display current canvas
''''''

drawText('Hello world!', fontname='normalFont') # Draw text on the canvas, with given font(size)
show(3000) # Display current canvas

drawText('Hello! world!', x=-0.5,y=0.0) # Draw text on the canvas, with center's position
show(3000) # Display current canvas

drawText('Hello! world!', x=-0.5,y=0.0, benchmark='left_center') # Draw text on the canvas, with left center's position
show(3000) # Display current canvas

drawText('Hello\nworld\n!') # Draw multi-line text on the canvas
show(3000) # Display current canvas

textSlide('Hello\nworld\nagain!') # Display some text directly, it's functionally equals to clear+drawText+show
```
### Show picture
```python
drawPic('demo.jpg') # Draw a picture on the canvas center
show(3000) # Display current canvas

drawPic('demo.jpg', w=400, h=300) # Draw a zoomed picture on the canvas center
show(3000) # Display current canvas

drawPic('demo.jpg', w=400, h=300, x=0.5, y=0.5) # Draw a zoomed picture on the canvas, and move it
show(3000) # Display current canvas

drawPic('data/demo.jpg', w=400, h=300, x=0.5, y=0.5, benchmark='upper_center') # Draw a zoomed picture on the canvas, and move it
show(3000) # Display current canvas
```
### Show shape
```python
drawCircle(60, fill=False) # Draw a circle on the canvas
show(3000) # Display current canvas

drawRect(200,100) # Draw a rect on the canvas
show(3000) # Display current canvas

x,y = shared.winWidth//2, shared.winHeight//2 # calculate the screen center
drawLine([(x-100,y-100), (x,y), (x+100,y-100)]) # Draw lines on the canvas
show(3000) # Display current canvas
```

## *Auditory Experiment*
### Play sound
```python
'''General usage'''
sound = loadSound('data/demo.wav') # Load the wav file
playSound(sound) # Play the wav file
''''''

show(1000) # Pause (show a screen during 3000ms)

sound = loadManySound('data',['ba','da'],'wav') # Load many wav files and concat them
playSound(sound)
```
### *Sound Recording*
```python
RATE = 44100
min_duration = 1*RATE
max_duration = 2*RATE
sample_duration=0.5
noise_level = environment_noise(sample_duration)

'Without file'
textSlide('Recording：')
sample_width,sound = recordSound(noise_level,min_duration,max_duration)

textSlide('Playing：')
playSound(sound)

'With file'
textSlide('Recording to file：')
recordSound_tofile('data','record',noise_level,min_duration,max_duration)

record = loadSound('data/record.WAV')
textSlide('Playing from file：')
playSound(record)
```

## *Scaffold functions*
```python
something = getInput('enter something:') # Get user input until "ENTER", then give it to a varible
introduction(['page1>','page2>','page3\npage3']) # Show the information of experiment
tip('Show something until press SPACE or RETURN') # Show something until "SPACE" or "RETURN"
restTime() # Suspend the experiment and ask participant to rest, until "SPACE" or "RETURN"
alertAndGo('Show something for 3000 ms',3000) # Show something during a given time, and continue
alertAndQuit('Show something for 3s, and quit')# Show something during a given time, and quit the program
```

## *Get external parameters*
```python
start()  # Calling start() will do the readSetting() implicitly
# readSetting() # Or you can directly load setting from "setting.txt"

print(shared.setting['timingSet']) # Print the text of 'timingSet' part 

print(timing('ITI')) # Print 'ITI' value (we specify 500 for it in "setting.txt")
print(timing('fix')) # Print 'fix' value (we specify 800~1400 range for it in "setting.txt")
print(timing('fix')) # Print 'fix' value (we specify 800~1400 range for it in "setting.txt")
```

## *Read or Write*
```python
'List the filenames of a dir'
filelist = readDir('data',shuffle=True)
print(filelist)

'Get stimuli from csv or xlsx'
stim = 'data/trial_list.csv'
alldata = readStimuli(stim)
block2 = readStimuli(stim, blockID=('block',2))

print('alldata:\n',alldata)
print('block2:\n',block2)

'Save result'
saveResult(blockID=1, resp=[1,2,3,4], columns=['resp'])
saveResult(blockID=2, resp=[1,2,3,4], columns=['resp'], stim=block2)
saveResult(blockID=3, resp=[(1,0),(2,0),(3,0),(4,0)], columns=['resp1','resp2'], stim=block2)
```

## *Send trigger*
```python
'Parallel Port'
shared.Objdll.Out32(0xC100,0) # 0xC100 is the port, 0 is the data

'Serial Port'
import serial
ser = serial.Serial()
ser.baudrate= 115200
ser.port = 'COM1' # set the port
ser.open()

ser.write(b'something') # send a string directly

tg = 'something'
ser.write(bytes(tg,encoding='utf8')) # send a string which might change

n=int('0b00010001',2)
ser.write(n.to_bytes((n.bit_length()+7)//8, 'big')) # send a binary code
```

## *Preload screen*
```python
drawText('Hello') # Draw text on the canvas
s1 = getScreen() # Get current canvas, then clean the canvas

drawText('world') # Draw text on the canvas
s2 = getScreen(cleanScreen=False) # Get current canvas, and keep it

drawText('........') # Draw text on the canvas
s3 = getScreen() # Get current canvas, then clean the canvas

show(3000,backup=s1) # Display backup canvas
show(3000,backup=s2) # Display backup canvas
show(3000,backup=s3) # Display backup canvas
```