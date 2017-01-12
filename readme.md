# Overview

[![PyPI Version][pypi-v-image]][pypi-v-link]

[pypi-v-image]: https://img.shields.io/pypi/v/expy.png
[pypi-v-link]: https://pypi.python.org/pypi/expy

Expy is an easy-yet-powerful experiment framework builder for psychology. It's aimed at setting up an experiment without struggling with the manual production of stimuli, data loading and storing, or the other time-consuming works, by using various module functions.
Expy is designed for psycholinguistic experiments, but it's also suitable for any other experiments.

**Advantanges**:

- Various stimuli modules (not need for preparation of massive stimuli pictures).
- Various procedure-controlling modules (instruction, alert, rest-stage, etc.)
- Convenient for stimuli loading and responses recording.
- Getting participants' response data (from keyboard, mouse, or joystick) by one function.
- Sending triggers easily.
- Easy pause or exit from the program.

**Disadvantages**:

- Not good at drawing complex shape (e.g.,grating) as stimuli (however, you could draw them as loaded pictures).
- Not good at video playing.

---
## Documentation
See http://expy.readthedocs.io/en/latest/ for introduction, tutorials, and reference manual.

---
# Installation instructions

Expy has been tested on Python3.5 64bit.
(Current it might be unfit for older versions like Python2.7. But since Python2 will become obsolete in the years to come, why not drop it anyaway and take Python3 instead?)

The simplest way to install Expy is through the Python Package Index (PyPI), which ensures that all required dependencies are established. This can be achieved by executing the following command:

```
pip install expy
```
or:
```
sudo pip install expy
```

The command of getting update:
```
pip install --upgrade expy
```
or:
```
sudo pip install --upgrade expy
```

###*Required Dependencies*

- numpy
- pandas
- scipy
- pygame
- pyaudio
- wave
- pyserial

---
# Simple example (An RSPV demo)

```python
# coding:utf-8
from expy import * # Import the needed functions
start() # Initiate the experiment environment

for w in 'ABCDE12345':
    drawText(w) # Draw something on the canvas
    show(200) # Keep displaying in 200ms
```

---
## Cookbook
### *Experiment Initiation*
```python
from expy import * # Import the needed functions
start() # Initiate the experiment environment
```

### *Experiment Structure*
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

### *Visual Experiment*
```python
from expy import * # Import the needed functions
start() # Initiate the experiment environment

def trial(word, pos):
    drawText(word, x=pos)  # Draw text on the canvas and display it

    key, rt = waitForResponse({key_.F: 'Left', key_.J: 'Right'}) # Waiting for pressing 'F' or 'J'
    if key == word:
        alertAndGo('Correct!', 1000)  # Display something in 1s
    else:
        alertAndGo('Wrong!', 1000)

    show(500)  # Pause (Keep displaying in 500ms)

alert('In this example, you need to respond to the words "left" with the F key , and respond to the words "right" with the J key') # Display something until pressing 'SPACE' or 'ENTER'
alertAndGo('The experiment will start after 3s.') # Display something in 3s(default)

stimuli = [('Left', -0.5), ('Right', 0.5), ('Right', -0.5),
           ('Left', 0.5), ('Left', -0.5), ('Right', -0.5)]

for word, pos in stimuli:
    trial(word, pos)  # Call the trial function with different parameters

alertAndQuit('Done!')  # Display something in 3s(default), and quit the program
```

### *Auditory Experiment*
```python
from expy import * # Import the needed functions
start() # Initiate the experiment environment

def trial(stim):
    sound = loadSound('data/' + stim + '.WAV')  # Load the wav file
    playSound(sound)  # Play the wav file

    textSlide('Please press F for "ba", or press J for "da"')  # Display something
    
    key, rt = waitForResponse({key_.F: 'ba', key_.J: 'da'}) # Waiting for pressing 'F' or 'J'

    if key == stim:
        alertAndGo('Correct!', 1000)  # Display something in 1s
    else:
        alertAndGo('Wrong!', 1000)

    show(500)  # Pause (Keep displaying in 500ms)

alert('In this example, you need to press key to select the word you heard.') # Display something until pressing 'SPACE' or 'ENTER'
alertAndGo('The experiment will start after 3s.')  # Display something in 3s(default)

for stim in ['ba', 'da', 'da', 'ba']:
    trial(stim)  # Call the trial function with different parameters

alertAndQuit('Done!')  # Display something in 3s(default), and quit the program
```
