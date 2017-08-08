## Simple example (An RSPV demo)

```python
from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

for w in 'ABCDE12345':
    drawText(w)  # Draw something on the canvas(not the screen)
    show(0.2)  # Display current canvas on the screen, and keep for 0.2s
```

---

## *Visual Experiment*

```python
from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

def trial(word, pos):
    drawText(word, x=pos)  # Draw text on the canvas and display it

    key, rt = waitForResponse({key_.F: 'Left', key_.J: 'Right'}) # Waiting for pressing 'F' or 'J'
    if key == word:
        alertAndGo('Correct!', 1)  # Display something in 1s
    else:
        alertAndGo('Wrong!', 1)

    show(0.5)  # Pause (Keep displaying in 0.5s)


stimuli = [('Left', -0.5), ('Right', 0.5), ('Right', -0.5),
           ('Left', 0.5), ('Left', -0.5), ('Right', -0.5)]

for word, pos in stimuli:
    trial(word, pos)  # Call the trial function with different parameters

alertAndQuit('Done!')  # Display something in 3s(default), and quit the program

```

## *Auditory Experiment*

```python
from expy import *  # Import the needed functions
start()  # Initiate the experiment environment

def trial(stim):
    sound = loadSound('data/' + stim + '.WAV')  # Load the wav file
    playSound(sound)  # Play the wav file

    textSlide('Please press F for "ba", or press J for "da"')  # Display something
    
    key, rt = waitForResponse({key_.F: 'ba', key_.J: 'da'}) # Waiting for pressing 'F' or 'J'

    if key == stim:
        alertAndGo('Correct!', 1)  # Display something in 1s
    else:
        alertAndGo('Wrong!', 1)

    show(0.5)  # Pause (Keep displaying in 0.5s)


instruction(shared.setting['instruction2'])
alertAndGo('The experiment will start after 3s.')  # Display something in 3s(default)

for stim in ['ba', 'da', 'da', 'ba']:
    trial(stim)  # Call the trial function with different parameters

alertAndQuit('Done!')  # Display something in 3s(default), and quit the program

```
