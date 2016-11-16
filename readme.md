# Overview

[![PyPI Version][pypi-v-image]][pypi-v-link]

[pypi-v-image]: https://img.shields.io/pypi/v/expy.png
[pypi-v-link]: https://pypi.python.org/pypi/expy

Expy is an easy-but-powerful psychology experiment framework. It's aimed at building an experiment without strugglling against the manual work of stimuli or the coding logic, by using a various of module functions.
Expy is designed for psycholinguistic experiment, but also be suitable for any other experiments.

**Advantange**:

- Various of stimuli module (not need to prepare massive of stimuli pictures).
- Various of procedure-controlling module (instruction, tip, rest, etc.)
- Convenient to read stimuli from file and record response to file.
- Getting participant's response data (keyboard, mouse, joystick) by one function.
- Sending trigger easily.
- You can pause or quit the program at anytime.

**Drawback**:

- Drawing complex shape (like grating) as stimuli (but you could draw them as loaded pictures).
- Video playing.

---
## Documentation
See http://expy.readthedocs.io/en/latest/ for a complete reference manual and introductory tutorials.

---
# Installation instructions

Expy has been tested on Python3.5 64bit, and I think it might be unfit for Python2.7.
(Since Python2 will be abanboned in recent years, why not drop it away and take Python3?)

The simplest way to install Expy is through the Python Package Index (PyPI). This will ensure that all required dependencies are fulfilled. This can be achieved by executing the following command:

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

    key, rt = waitForResponse({K_f: 'Left', K_j: 'Right'}) # Waiting for pressing 'F' or 'J'
    if key == word:
        alertAndGo('Correct!', 1000)  # Display something in 1s
    else:
        alertAndGo('Wrong!', 1000)

    show(500)  # Pause (Keep displaying in 500ms)

tip('In this example, you need to respond to the words "left" with the F key , and respond to the words "right" with the J key. ') # Display something until pressing 'SPACE' or 'ENTER'
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
    
    key, rt = waitForResponse({K_f: 'ba', K_j: 'da'}) # Waiting for pressing 'F' or 'J'

    if key == stim:
        alertAndGo('Correct!', 1000)  # Display something in 1s
    else:
        alertAndGo('Wrong!', 1000)

    show(500)  # Pause (Keep displaying in 500ms)

tip('In this example, you need to press key to select the word you heard.') # Display something until pressing 'SPACE' or 'ENTER'
alertAndGo('The experiment will start after 3s.')  # Display something in 3s(default)

for stim in ['ba', 'da', 'da', 'ba']:
    trial(stim)  # Call the trial function with different parameters

alertAndQuit('Done!')  # Display something in 3s(default), and quit the program
```
