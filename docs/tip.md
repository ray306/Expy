### Timing
---
#### How to suspend the experiment
We often meet the need of keeping showing the text, the shape, etc., but the experiment program will jump the next command once the last command executed, which means there's no interval between `drawText("Please look at the stimuli")` and `drawText("Please press the keyboard")`. 
So, how could we insert an 1s' interval between two `drawText` operations?

We will insert the command `show(1)` between two commands.
The method `show` will keep running and blocking the experiment procedure for a given duration which depends on the parameter "out_time".

##### About the unit of time measurement
All the numbers should given based on second. 

##### About "shared.start_tp"
Normally, the method (e.g. `show` and `waitForResponse`) with the parameter "out_time" will keep running for the duration of "out_time". Thus the onset of "out_time" is the onset of those commands. 
But we sometimes want the "out_time" to refer to longer time -- the onset should be refered to another timepoint. In that case, you should setted the "shared.start_tp = time.time()" before those commands, the "out_time" would mean the duration between "shared.start_tp = time.time()" and those commands.

##### The default value of timing onset
If not assigned, the default value of timing onset, which means the value of "shared.start_tp", will be the ending time of last `win.flip()`.

### Object position
---
#### Coordinate
We designed two types of coordinate:
- **Pixel coordinate**: The coordinate bases on pixel number (`int`) while you give the method integral number.
    - The position index (x=0, y=0) means the lower-left corner of current window. 
    - The range of x: [0, the width of window]
    - The range of y: [0, the height of window]
- **Ratio coordinate**: The coordinate bases on the ratio (`float`) of current window size while you give the method decimal fraction.
    - The position index (x=0.0, y=0.0) means the center of current window.
    - The range of x: [-1.0, 1.0]
    - The range of y: [-1.0, 1.0]

#### Supported position's anchors
The default anchor of an object is its lower-left corner. If you want another anchor, you could change the parameters "anchor_x" and "anchor_y":

- anchor_x: str (default:'center')
    The position anchor on this object to the given x.
    Options: 'center', 'left', or 'right'.
- anchor_y: str (default:'center')
    The position anchor on this object to the given y.
    Options: 'center', 'top', or 'bottom'.

### Display tricks
---
#### Font
`Simhei` is the default font under Windows and Linux, and 'Hei' is the default font under MacOSX. But if you put a "ttf" font file under expy package's path, then you can use the font by its font name (not the filename).
e.g. 
> drawText(text, font='Source Han Sans SC Normal')

#### Supported colornames
C_black, C_white, C_red, C_lime, C_blue, C_yellow, C_aqua, C_fuchsia, C_silver, C_gray, C_maroon, C_olive, C_green, C_purple, C_teal, C_navy

#### Draw things on previous screen / new screen
In default, the `drawXXX()` command will draw thing on a new screen, but you can also draw a thing on previous screen by a parameter setting `show_on=False`.
e.g. 
> w, h = drawText('Hello world!', show_now=False)
> drawRect(w, h, color=C_red, fill=False, show_now=False)
> show(3)

### Keyboard
---
#### Keyboard controller
You could press **F12** to suspend/resume the program;
You could press **ESC** to quit the program;
You could press **WIN** to return to the desktop and leave the program running

#### Response
todo
list, dictionary, max wating time
whilePressing


### Sound
---
#### Play sound while keeping the experiment procedure going
Setting the parameter `busy=False` in `playSound()` can start a new thread for sound playing, and so the experiment procedure won't be stopped by `playSound()`.
And in this case, `playSound()` will return a number refers to the playing track. You can stop the sound by the command `shared.states[playing_track_id] = False`

### IO
---
#### Read whole/partial stimuli list
You can get whole stimuli list by `readStimuli(path)`;
You can get part of the list by `readStimuli(path, query=XXX)`. `XXX` should be a string discribing the filter (https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.query.html). For example, `query='block==2'` means the rows with `2` at the `block` attribute will be selected.

#### Write the result
##### The format of result
List of numbers or strings, or list of list/tuples.
e.g.
`['A','B','C','D']`
or
`[('A', 1), ('B', 0), ('C', 1), ('D', 0)] `

##### Append to existing result file
If `block_tag` was undefined in `saveResult()` and the result file was existed, the new result will be added to existing result file.

##### Attach the stimuli list to the result
By giving the stimuli list (List or DataFrame) to the parameter `stim`, `saveResult()` will store the stimuli list as well.
e.g.
> stimuli_list = pd.Dataframe(['A','B','C','D'])
> saveResult(resp=[(1, 0), (2, 0), (3, 0), (4, 0)], columns=['resp1', 'resp2'], stim=stimuli_list)

##### Subject name in result file
If the `shared.subject` has been assigned a value or the command `getSubjectID()` was executed before `saveResult()`, the assigned value/input will be part of the result filename.

#### Send trigger
todo

#### Log the events in experiment
todo


### Scaffolds
---
todo

### Others
---
#### Outside control of programm
todo

#### About "extend.py"
A internal space for your DIY methods.

