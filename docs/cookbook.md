# Cookbook
---
## *Experiment Initiation*
```python
# coding:utf-8
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
        
# run
for trialList in blockList:
    block(trialList)
```

## *Visual*
### Show text
```python
'''General usage'''
# Draw text on the canvas
drawText('Hello world!')
show(3000)  # Display current canvas
''''''

# Draw text on the canvas, with left center's position
drawText('Hello! world!', x=-0.5, y=0.0, benchmark='left_center')
show(3000)  # Display current canvas

# Draw text on the canvas, with given fontsize
drawText('Hello world!', size=40)
show(3000)  # Display current canvas

# Draw text on the canvas, with given angle
drawText('Hello world!', size=40, rotation=45)
show(3000)  # Display current canvas

# Draw text on the canvas, with center's position
drawText('Hello! world!', x=-0.5, y=0.0)
show(3000)  # Display current canvas

drawText('Hello\nworld\n!')  # Draw multi-line text on the canvas
show(3000)  # Display current canvas

# Display text on a new slide, it's functionally equals to clear+drawText+show,
textSlide('Hello\nworld\nagain!')

```
### Show picture
```python
'''General usage'''
drawPic('demo.jpg') # Draw a picture on the canvas center
show(3000) # Display current canvas
''''''

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

x,y = shared.win_width//2, shared.win_height//2 # calculate the screen center
drawLine([(x-100,y-100), (x,y), (x+100,y-100)]) # Draw lines on the canvas
show(3000) # Display current canvas
```

## *Auditory*
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
noise_level = environment_noise(0.5)  # Detect the noise level of environment

'Without file'
textSlide('Recording：')
sample_width, sound = recordSound(noise_level, recording_min=2, sounding_max=0.7)
textSlide('Playing：')
playSound(sound)

'With file'
textSlide('Recording to file：')
recordSoundTofile('record', noise_level, recording_min=2, sounding_max=0.7)

record = loadSound('data/record.WAV')
textSlide('Playing from file：')
playSound(record)
```

## *Response*
```python
drawText('请按下键盘上的任意键') # Draw text on the canvas and display it
key,rt = waitForResponse() # Waiting for pressing and get the pressed key.
alertAndGo('您刚刚按下了%d，用时：%dms'%(key,rt)) # Display the keypress

'Key limited by "allowed_keys". Please look into "Key mapping" for some detail'
drawText('除了键盘上的K或J，别的按键都不会起作用') # Draw text on the canvas and display it
key,rt = waitForResponse({K_k:'K',K_j:'J'}) # Waiting for pressing 'K' or 'J', and get the pressed key's name.
alertAndGo('您刚刚按下了%s，用时：%dms'%(key,rt)) # Display the keypress

drawText('除了键盘上的K或J，别的按键都不会起作用') # Draw text on the canvas and display it
key,rt = waitForResponse([K_k,K_j]) # Waiting for pressing 'K' or 'J', and get the pressed key's id.
alertAndGo('您刚刚按下了%d，用时：%dms'%(key,rt)) # Display the keypress

drawText('除了键盘上的K，别的按键都不会起作用') # Draw text on the canvas and display it
key,rt = waitForResponse(K_k) # Waiting for pressing 'K', and get the pressed key's id.
alertAndGo('您刚刚按下了%d，用时：%dms'%(key,rt)) # Display the keypress

'Time limited by "out_time"'
drawText('请在1秒内按下键盘上的K或J') # Draw text on the canvas and display it
key,rt = waitForResponse({K_k:'K',K_j:'J'}, out_time=1000) # Waiting for pressing 'K' or 'J' in 1000ms.
alertAndGo('您刚刚按下了%s，用时：%dms'%(key,rt)) # Display the keypress

'Get only key(without RT) by "has_RT"'
drawText('请按下键盘上的K或J') # Draw text on the canvas and display it
key = waitForResponse({K_k:'K',K_j:'J'}, has_RT=False) # Waiting for pressing 'K' or 'J', no RT returned.
alertAndGo('您刚刚按下了'+key) # Display the keypress
```

## *Scaffold functions*
```python
# Get user input until "ENTER" pressed, then give it to a variable
something = getInput('enter something:')

# Show something until "SPACE" or "RETURN" pressed
alert('You just entered "%s".\nPlease press SPACE or RETURN to continue.' %something)

# Show the instruction of experiment
instruction(['This is the first page of instruction>', 'second page>', 'last page\nPress SPACE to quit the instruction'])

# Suspend the experiment and ask participant to rest, until "SPACE" pressed
restTime()  

# Show something during a limited period, and continue
alertAndGo('Show something for 3000ms', 3000)

# Show something during a limited period, and quit the program
alertAndQuit('Show something for 3000ms, and quit')
```

## *Get external parameters*
```python
start()  # Calling start() will do the readSetting() implicitly
# readSetting() # Or you can directly load setting from "setting.txt"

'Using "shared.setting" dictionary to get the pre-defined value'
print(shared.setting['background_color']) # Print the setting of 'background_color' part 
print(shared.setting['timing_set']) # Print the setting of 'timing_set' part 

'Calling "timing" function to get a certain time value'
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
block2 = readStimuli(stim, query='block==2')

print('alldata:\n',alldata)
print('block2:\n',block2)

'Save result'
saveResult(block_id=1, resp=[1,2,3,4], columns=['resp'])
saveResult(block_id=2, resp=[1,2,3,4], columns=['resp'], stim=block2)
saveResult(block_id=3, resp=[(1,0),(2,0),(3,0),(4,0)], columns=['resp1','resp2'], stim=block2)
```

## *Send trigger*
```python
'Parallel Port'
start(port=0xC100)
sendTrigger(0,mode='P')

'Serial Port'
start(port='COM1')
sendTrigger('something',mode='S')
```

## *Preload screen*
```python
drawText('Hello',display=False) # Draw text on the canvas
s1 = getScreen() # Get current canvas, then clean the canvas

drawText('world',display=False) # Draw text on the canvas
s2 = getScreen(clean_screen=False) # Get current canvas, and keep it

drawText('........',display=False) # Draw text on the canvas
s3 = getScreen() # Get current canvas, then clean the canvas

show(3000,backup=s1) # Display backup canvas
show(3000,backup=s2) # Display backup canvas
show(3000,backup=s3) # Display backup canvas
```