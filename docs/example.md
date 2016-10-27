# Simple example
---
```python
# coding:utf-8
from expy import * # Import the needed functions
start() # Initiate the experiment environment

# An RSPV demo
for w in 'ABCDE12345':
    drawWord(w) # Draw something on the canvas(not the screen)
    show(200) # Display current canvas on the screen, and keep for 200ms
```

## *Visual Experiment*
```python
from expy import * # Import the needed functions
start() # Initiate the experiment environment

name = getInput('Please enter your name:')
introduction(setting('introduction1'))
tip(name+', Are you ready?')

def trial(word,pos):
    drawWord('+')
    show(500)

    drawWord(word,x=pos) # Draw text on the canvas
    show()
    key = waitForEvent({K_f:'Left',K_j:'Right'}) # Waiting for pressing 'F' or 'J'
    if key==word:
        alertAndGo('Correct!',1000)
    else:
        alertAndGo('Wrong!',1000)
    show(500)

alertAndGo('The experiment will start after 3s.')
stimuli = [('Left',-0.5),
            ('Right',0.5),
            ('Right',-0.5),
            ('Left',0.5),
            ('Left',-0.5),
            ('Right',-0.5)]
for word,pos in stimuli:
    trial(word,pos)

alertAndQuit('Done!')
```
## *Auditory Experiment*
```python
from expy import * # Import the needed functions
start() # Initiate the experiment environment

name = getInput('Please enter your name:')
introduction(setting('introduction2'))
tip(name+', Are you ready?')

def trial(stim):
    sound = loadSound('data/'+stim+'.WAV')
    playSound(sound)

    textSlide('Please press F for "ba", or press J for "da"')
    key = waitForEvent({K_f:'ba',K_j:'da'}) # Waiting for pressing 'F' or 'J'

    if key==stim:
        alertAndGo('Correct!',1000)
    else:
        alertAndGo('Wrong!',1000)

    show(500)

alertAndGo('The experiment will start after 3s.')
for stim in ['ba','da','da','ba']:
    trial(stim)

alertAndQuit('Done!')
```