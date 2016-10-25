# Cookbook
---

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
