# Simple example
---
```python
# coding:utf-8
from expy import * # Import the needed functions
start() # Initiate the experiment environment

# An RSPV demo
for w in 'ABCDE12345':
    drawText(w) # Draw something on the canvas(not the screen)
    show(200) # Display current canvas on the screen, and keep for 200ms
```

## *Visual Experiment*
```python
from expy import * # Import the needed functions
start() # Initiate the experiment environment

# name = getInput('Please enter your name:')
tip('In this example, you need to respond to the words "left" with the F key , and respond to the words "right" with the J key. ') # Display something until pressing 'SPACE' or 'ENTER'

def trial(word,pos):
    drawText(word,x=pos) # Draw text on the canvas
    show() # Display current canvas

    key = waitForEvent({K_f:'Left',K_j:'Right'}) # Waiting for pressing 'F' or 'J'
    if key==word:
        alertAndGo('Correct!',1000) # Display something in 1s
    else:
        alertAndGo('Wrong!',1000)

    show(500) # Pause (show a screen during 500ms)

alertAndGo('The experiment will start after 3s.') # Display something in 3s(default)

stimuli = [('Left',-0.5),
            ('Right',0.5),
            ('Right',-0.5),
            ('Left',0.5),
            ('Left',-0.5),
            ('Right',-0.5)]
for word,pos in stimuli:
    trial(word,pos) # Call the trial function with different parameters

alertAndQuit('Done!') # Display something in 3s(default), and quit the program
```
## *Auditory Experiment*
```python
from expy import * # Import the needed functions
start() # Initiate the experiment environment

# name = getInput('Please enter your name:')
tip('In this example, you need to press key to select the word you heard.') # Display something until pressing 'SPACE' or 'ENTER'

def trial(stim):
    sound = loadSound('data/'+stim+'.WAV') # Load the wav file
    playSound(sound) # Play the wav file

    textSlide('Please press F for "ba", or press J for "da"')
    key = waitForEvent({K_f:'ba',K_j:'da'}) # Waiting for pressing 'F' or 'J'

    if key==stim:
        alertAndGo('Correct!',1000) # Display something in 1s
    else:
        alertAndGo('Wrong!',1000)

    show(500) # Pause (show a screen during 500ms)

alertAndGo('The experiment will start after 3s.') # Display something in 3s(default)
for stim in ['ba','da','da','ba']:
    trial(stim) # Call the trial function with different parameters

alertAndQuit('Done!') # Display something in 3s(default), and quit the program
```