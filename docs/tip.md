#### How to suspend the experiment
We often meet the need of keeping showing the text, the shape, etc., but the experiment program will jump the next command once the last command executed, which means there's no interval between `drawText("Please look at the stimuli")` and `drawText("Please press the keyboard")`. 
So, how could we insert an 1s' interval between two `drawText` operations?

We will insert the command `show(1)` between two commands.
The method `show` will keep running and blocking the experiment procedure for a given duration which depends on the parameter "out_time".

##### About the unit of time measurement
All the numbers should given based on second. 

##### About "shared.start_tp"
Normally, the commands with the parameter "out_time" will keep running for the duration of "out_time". Thus the onset of "out_time" is the onset of those commands. 
But we sometimes want the "out_time" to refer to longer time -- the onset need to be flexible. In that case, you should setted the "shared.start_tp = time.time()" before those commands, the "out_time" would mean the duration between "shared.start_tp = time.time()" and those commands.


---
#### Position
We designed two types of coordinate:
- **Pixel coordinate**: The coordinate bases on pixel number while you give the method integral number.
    - The position index (x=0, y=0) means the lower-left corner of current window. 
    - The range of x: [0, the width of window]
    - The range of y: [0, the height of window]
- **Ratio coordinate**: The coordinate bases on the ratio of current window size while you give the method decimal fraction.
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

---
#### Keyboard controller
You could press **F12** to suspend/resume the program;
You could press **ESC** to quit the program;
You could press **WIN** to return to the desktop and leave the program running

---
#### Font
`Simhei` is the default font under Windows and Linux, and 'Hei' is the default font under MacOSX. But if you put a "ttf" font file under expy package's path, then you can use the font by its font name (not the filename).
e.g. `drawText(text, font='Source Han Sans SC Normal')`

---
#### Supported colornames
C_black, C_white, C_red, C_lime, C_blue, C_yellow, C_aqua, C_fuchsia, C_silver, C_gray, C_maroon, C_olive, C_green, C_purple, C_teal, C_navy

---
The "playing_track" and "blocking" in the media functions
*todo*

---
#### About "extend.py"
A internal space for your DIY methods.

