# Cookbook
---
- Experiment Initiation
- Experiment Structure
- Visual
    - Show text
    - Show picture
    - Show shape
- Video
- Auditory
    - Play sound
    - Sound Recording
- Response
- Scaffold functions
- Get external parameters
- Read or write file
- Send trigger
- Preload screen

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
  So we suggest that your code should have hierarchical structure, as the example below: 
```python
from expy import *
start()

def trial(stim):
    draw(stim)
    show(1)

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
start()  # Initiate the experiment environment

'''General usage'''
# Draw text on the canvas
drawText('Hello world!')
show(2)  # Display current canvas
''''''

# Draw text on the canvas
w, h = drawText('Hello world!', show_now=False)
drawRect(w, h, color=C_red, fill=False, show_now=False)
show(2)  # Display current canvas

# Draw text on the canvas, with left center's position
drawText('Hello! world!', anchor_x='left', anchor_y='bottom')
show(2)  # Display current canvas

# Draw text on the canvas, with given fontsize
drawText('Hello world!', size=50)
show(2)  # Display current canvas

# Draw text on the canvas, with given font color
drawText('Hello world!', color=C_red)
show(2)  # Display current canvas

# # Draw text on the canvas, with given angle
# drawText('Hello world!', rotation=45)
# show(2)  # Display current canvas

# Draw text on the canvas, with center's position
drawText('Hello! world!', x=-0.5, y=0.0)
show(2)  # Display current canvas

drawText('Hello\nworld\n!')  # Draw multi-line text on the canvas
show(2)  # Display current canvas

# Display text on a new slide, it's functionally equals to clear+drawText+show,
textSlide('Hello\nworld\nagain!')

```

### Show picture

```python
start()  # Initiate the experiment environment

'''General usage'''
# Draw a picture on the canvas center
drawPic('data/demo.jpg')
show(3)  # Display current canvas
''''''

# Draw a zoomed picture on the canvas center
drawPic('data/demo.jpg', w=400, h=300)
show(3)  # Display current canvas

# Draw a zoomed picture on the canvas center
drawPic('data/demo.jpg', w=300, h=400, rotate=90)
show(3)  # Display current canvas

# Draw a zoomed picture on the canvas, and move it
drawPic('data/demo.jpg', w=400, h=300, x=0.5, y=0.5)
show(3)  # Display current canvas

# Draw a zoomed picture on the canvas, and move it
drawPic('data/demo.jpg', w=400, h=300, x=0.5, y=0.5, anchor_x='right',anchor_y='center')
show(3)  # Display current canvas

```

### Show shape

```python
start(background_color=C_green)  # Initiate the experiment environment

# Draw a rect on the canvas
drawRect(200, 100, color=C_red)
show(1.5)  # Display current canvas

# Draw a circle on the canvas
drawCircle(60, fill=False)
show(1.5)  # Display current canvas

x, y = shared.win_width // 2, shared.win_height // 2  # calculate the screen center
drawPoints([(x - 100, y - 100), (x+50, y), (x + 100, y - 100)], size=5)
show(1.5)

# Draw lines on the canvas
drawLines([(x - 100, y - 100), (x+50, y), (x + 100, y - 100)])
show(1.5)  # Display current canvas

```

## *Video*

```python
start(fullscreen=False)  # Initiate the experiment environment

video = loadVideo('data/demo.mpg')
playVideo(video)

```

## *Auditory*
### Play sound

```python
start(sample_rate=44100)  # Initiate the experiment environment

'''General usage'''
sound = loadSound('data/demo.WAV')  # Load the wav file
playSound(sound)  # Play the wav file
''''''

# Load many wav files and concat them
sound = loadManySound('data', ['ba','da','ba','da'], 'wav')
playSound(sound)

# Play multiple soundtrack at the same time
sound = loadManySound('data', ['demo','demo','demo','demo'], 'wav')
playSound(sound, busy=False)  # Play the wav file
sound = loadManySound('data', ['ba','da','ba','da'], 'wav')
playSound(sound, busy=False)
show(5)

# sound = makeSound(data)
# playSound(sound)
# show(1)

sound = makeBeep(440, 0.5)
playSound(sound)

sound = makeNoise(3)
playSound(sound)

sound = loadSound('data/demo.WAV')  # Load the wav file
sound = changeOnTracks(sound,changeVolume,[0.1,1]) # Change the volume of different tracks 
playSound(sound)  # Play the wav file
show(0.5)  # Pause (Keep displaying in 0.5s)

# s = makeBeep(440, 15)
s = loadManySound('data', ['ba','da','ba','da'], 'wav')
index = playAlterableSound(s,effect=changePitch)
print('The change is', index)




```

### *Sound Recording*

```python
start()  # Initiate the experiment environment

noise_level = environmentNoise(0.5)  # Detect the noise level of environment

'Without file'
textSlide('Recording: ')
sound = recordSound(noise_level, rec_length_min=2, sound_length_max=4)
textSlide('Playing: ')
playSound(sound)

'With file'
textSlide('Recording to file: ')
recordSound(noise_level, rec_length_min=2, sound_length_max=4, 
                                    path='data/record.WAV')
record = loadSound('data/record.WAV')
textSlide('Playing from file: ')
playSound(record)


```

## *Response*

```python
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
key,rt = waitForResponse(key_.NUM_ENTER)  # Waiting for pressing 'K', and get the pressed key's id.
alertAndGo('您刚刚按下了%d，用时: %fs' % (key,rt))  # Display the keypress

'Time limited by "out_time"'
drawText('请在1秒内按下键盘上的K或J')  # Draw text on the canvas and display it
key,rt = waitForResponse({key_.K: 'K', key_.J: 'J'}, out_time=1)  # Waiting for pressing 'K' or 'J' in 1s.
if type(rt)==float:
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
```

## *Scaffold functions*

```python
start()  # Initiate the experiment environment

# Get user input until "ENTER" pressed, then give it to a variable
something = getInput('enter something:')

# Show something until "RETURN" pressed
alert('You just entered "%s".\nPlease press RETURN to continue.' %something)

# Show the instruction of experiment
instruction(['This is the first page of instruction>', 'second page>', 'last page\nPress SPACE to quit the instruction'])

# Suspend the experiment and ask participant to rest, until "SPACE" pressed
restTime()

# Show something during a limited period, and continue
alertAndGo('Show something for 3s', 3)

# Show something during a limited period, and quit the program
alertAndQuit('Show something for 3s, and quit')
```

## *Get external parameters*

```python

start()  # Calling start() will do the readSetting() implicitly
# readSetting() # Or you can directly load setting from "setting.txt"

'Using "shared.setting" dictionary to get the pre-defined value'
print(shared.setting['background_color'])  # Print the setting of 'background_color' part
print(shared.setting['timing_set'])  # Print the setting of 'timing_set' part

'Calling "timing" function to get a certain time value'
print(timing('ITI'))  # Print 'ITI' value (we specify 500 for it in "setting.txt")
# Print 'fix' value (we specify 800~1400 range for it in "setting.txt")
print(timing('fix'))

```

## *Read or Write*

```python

'List the filenames of a dir'
filelist = readDir('data', shuffle=True)
print(filelist)

'Get stimuli from csv or xlsx'
stim = 'data/trial_list.csv'
alldata = readStimuli(stim)
block2 = readStimuli(stim, query='block==2')

print('alldata:\n', alldata)
print('block2:\n', block2)

'Save result'
saveResult(resp=[1, 2, 3, 4], block_tag=1, columns=['resp'])
saveResult(resp=[1, 2, 3, 4], block_tag=2 columns=['resp'], stim=block2)
saveResult(resp=[(1, 0), (2, 0), (3, 0), (4, 0)], block_tag=3, columns=[
           'resp1', 'resp2'], stim=block2)

```

## *Send trigger*

```python
# ser.write(n.to_bytes((n.bit_length()+7)//8, 'big')) # send a binary code

```

## *Preload screen*

```python
start()  # Initiate the experiment environment

drawText('Hello', show_now=False)  # Draw text on the canvas
s1 = getScreen()  # Get current canvas, then clean the canvas

drawText('world', show_now=False)  # Draw text on the canvas
s2 = getScreen(clean_screen=False)  # Get current canvas, and keep it

drawText('........', show_now=False)  # Draw text on the canvas
s3 = getScreen()  # Get current canvas, then clean the canvas

show(3, backup=s1)  # Display backup canvas
show(3, backup=s2)  # Display backup canvas
show(3, backup=s3)  # Display backup canvas

```
