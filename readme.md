Document: http://expy.readthedocs.io/en/latest/

===========
# Overview

Expy is an easy-but-powerful psychology experiment builder. It's designed for psycholinguistic experiment, but also be suitable for other visual or auditory experiments.

---
# Native example

```python
# coding:utf-8
from expy import * # Import the needed functions
start() # Initiate the experiment environment

# An RSPV demo
for w in '这是一个简单的例子':
    drawWord(w) # Draw something on the canvas(not the screen)
    show(200) # Show the content of current canvas on the screen, and keep for 200ms
```
---
# API overview

- Initiation (Environment Setting)
- Stimulus
    - Text
    - Shape
    - Picture
    - Sound
    - Video
- Response
- IO (Read & Record)
    - Read
    - Save
- Other Scaffolds
    - show
    - clear
    - getInput
    - introdution
    - restTime
    - tip
    - alertAndGo
    - alertAndQuit


---
# Cookbook
## *Experiment Structure*
A standard experiment contains 3 levels:
- Run(Session)
- Block
- Trial
So we suggest that your code should have hierarchical structure, as the example below：
```python
def trial(stim):
    drawWord(stim)
    show(1000)
def block(trialList):
    for stim in trialList:
        trial(stim)
def run():
    for trialList in blockList:
        block(trialList)

run()
```
## *Visual Experiment*
todo
## *Auditory Experiment*
todo
