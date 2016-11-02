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

The simplest way to install Expy is through the Python Package Index (PyPI). This will ensure that all required dependencies are fulfilled. This can be achieved by executing the following command:

```
pip install expy
```
or:
```
sudo pip install expy
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
    drawText(w) # Draw something on the canvas(not the screen)
    show(200) # Display current canvas on the screen, and keep for 200ms
```