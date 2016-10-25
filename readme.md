===========
# Overview

Expy is an easy-but-powerful psychology experiment builder. It's designed for psycholinguistic experiment, but also be suitable for other visual or auditory experiments.

===========

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

---
# API
# basic page
textSlide 在一个新页面上显示text的内容

# advanced page
tip 显示一个实验提示tip，然后等待被试按键确认
alertAndQuit 显示一个实验提示（出错警告或实验结束提示），x秒后自动退出程序
alertAndGo 显示一个实验提示，一段时间后自动消失并继续程序

# more advanced page
getInput 获取输入
introduction 实验介绍阶段
rest 实验暂停 

# response
waitForResp 等待被试按键，超过设定时间自动结束,容许的按键可有多个
waitForEvent 等待被试按键,容许的按键只能有一个

# IO
readSetting 读取配置文件
readStimuli 读取csv数据文件，得到实验刺激
readDir 读取一个文件夹下的文件列表
saveResult 生成csv