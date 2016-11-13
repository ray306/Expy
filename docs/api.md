## Initialization
- **start(settingfile='setting.txt', fullscreen=True, winsize=(800, 600), mouseVisible=False, normalFontSize=20, stimFontSize=None, distance=60, diag=23, angel=2.5, fontColor=(255, 255, 255), backgroundColor=(128, 128, 128), sample_rate=44100, bits=16, channel=2, port='COM1')**

```
Initialize the experiment.
Note: todo.

Parameters
----------
settingfile: str (default: 'setting.txt')
    The filepath of setting
fullscreen: True(default), or False 
    Whether the window is fullscreen
winsize: (width,height) (default:(800, 600)) 
    The size of window
mouseVisible: True, or False(default)
    Set the mouse pointer visibility
normalFontSize: int (default:20) 
    The size of normal/['normalFont'] text 
stimFontSize: int, or None(default) 
    The size of ['stimFont'] text 
distance: int (default:60) 
    Distance from eyes to screen (cm)
diag: int (default:23) 
    The length of the screen diagonal (inch) 
angel: int (default:2.5) 
    Visual angel of single char (degree)
fontColor: tuple RGB (default:(255, 255, 255)) 
    The color of text
backgroundColor: tuple RGB (default:(128, 128, 128)) 
    The color of background
sample_rate: int (default:44100) 
    Sample rate of sound mixer
bits: int (default:16) 
    Bits of sound mixer
channel: int (default:2) 
    Channel amount of sound mixer
port: str, or hex number (default:'COM1') 
    Port name used to send trigger.
    Use str on serial port, and hex on parallel port 

Returns
-------
None
```

---
## Stimulus
### *Position*
- **getPos(x=shared.winWidth // 2, y=shared.winHeight // 2, w=0, h=0, benchmark='center')**

```
Caluate the screen position of object

Parameters
----------
x: float or int (default: shared.winWidth // 2)
    If x is float, it represents the x-offset(-1~1 scale) from the object benchmark to the screen center,
    if int, it represents the x-offset(pixel) from the object benchmark to the screen upperleft.
y: float or int (default: shared.winHeight // 2)
    Similar with x
w: float or int (default: 0)
    If w is float, it represents the width scale on screen,
    if int, it represents the width in pixel.
h: float or int (default: 0)
    Similar with x
benchmark: 'center'(default), 
           'upper_left', 'upper_right', 'lower_left', 'lower_right', 
           'upper_center', 'left_center', 'lower_center', 'right_center'
    The position benchmark on this object to the given x and the given y. 

Returns
-------
(x,y): (int,int)
    The position of the object's upperleft corner

```

### *Text*
- **drawText(text, font='simhei', size='stimFontSize', color=C_white, rotation=0, x=0.0, y=0.0, benchmark='center', display=True)**

```
Draw text on the canvas. The text will show as multiple lines splited by the '\n'. 

Parameters
----------
text: str
    The content of text.
font: str (default:'simhei')
    The font name of text.
size:int, or str (default:'stimFontSize')
    The font size of text, you can either use a number or a pre-defined number name.
color: RGB tuple, or pre-defined variable (default:'C_white')
    The font color of text, you can either use an RGB value or a pre-defined color name. The pre-defined colors include C_black, C_white, C_red, C_lime, C_blue, C_yellow, C_aqua, C_fuchsia, C_silver, C_gray, C_maroon, C_olive, C_green, C_purple, C_teal, C_navy.
rotation: int (default:0)
    The rotation angle of text.
x: int, or float (default:0.0)
    The x coordinate of text. If x is int, the coordinate would be pixel number to the left margin of screen; If x is float (-1~1), the coordinate would be percentage of half screen to the screen center.
y: int, or float (default:0.0)
    The y coordinate of text. If y is int, the coordinate would be pixel number to the upper margin of screen; If y is float (-1~1), the coordinate would be percentage of half screen to the screen center.
benchmark: str (default:'center')
    The position benchmark of x and y on the text area.
display: True(default), False
    If True, the function will put the canvas onto the screen. 

Returns
-------
None
```

### *Shape*
- **drawRect(w, h, x=0.0, y=0.0, fill=True, color=(255, 255, 255), width=1, benchmark='center', display=True)**

```
Draw rectangle on the canvas.

Parameters
----------
todo

Returns
-------
None
```
- **drawCircle(r, x=0.0, y=0.0, fill=True, color=(255, 255, 255), width=1, benchmark='center', display=True)**

```
Draw circle on the canvas.

Parameters
----------
todo

Returns
-------
None
```
- **drawLine(points, color=(255, 255, 255), width=1)**

```
Draw line(s) on the canvas.

Parameters
----------
todo

Returns
-------
None
```

### *Picture*
- **drawPic(path, w=0, h=0, x=0.0, y=0.0, rotate=0, benchmark='center', display=True)**

```
Draw picture on the canvas.

Parameters
----------
todo

Returns
-------
None
```

### *Sound*
- **loadSound(path)**

```
Load a wav file, and return data array
Or load a mp3/ogg file, and return None

Parameters
----------
todo

Returns
-------
value: np.array (if loaded a wav file), or None (if loaded a mp3/ogg file)
    The sound data array
```
- **loadManySound(dirpath, filenames, ext='wav')**

```
Read a list of music file, then concatnate them and return data array.
not support mp3/ogg files

Parameters
----------
todo

Returns
-------
value: np.array
    The sound data
```
- **makeSound(freq, duration)**

```
Return a data array of certain sound freq

Parameters
----------
todo

Returns
-------
wave: np.array
    The sound data array
```
- **playSound(wav=None, block=True)**

```
Play a loaded file or a data array

Parameters
----------
todo

Returns
-------
None
```

### *Video*
### *Display controller*
- **show(outTime=False, cleanScreen=True, backup=None)**

```
Display current canvas buffer, and keep the display during a limited period.

Parameters
----------
outTime: int(>0), False(default)
    The time limit of current function. 
cleanScreen: True(default), False
    Whether clear the screen after get the screen or not. 
backup: None, or a screen backup
    Give a prepared screen to display

Returns
-------
None
```
- **clear()**

```
Clear the screen

Parameters
----------
None

Returns
-------
None
```
- **getScreen(cleanScreen=True)**

```
Get a backup of current canvas

Parameters
----------
cleanScreen: True(default), False
    Whether clear the screen after get the screen or not. 

Returns
-------
None
```

---
## Response
### *Keyboard & Mouse & Joystick*
-    **waitForResponse(allowedKeys=None, outTime=0, hasRT=True, suspending=False)**

```
Waiting for a allowed keypress event during a limited period
(Press F12 would suspend the procedure and press ESC would end the program)

Parameters
----------
allowedKeys：None(default), Keyname, list, or dict
   The allowed key(s).
   You can leave nothing, 
           a Keyname (eg. K_f), 
           a list of Keyname (eg. [K_f,K_j]), 
           or a dict of Keyname (eg. [K_f:'F',K_j:'J']) here.
   You could look into the Keyname you want in http://expy.readthedocs.io/en/latest/keymap/
outTime：int(>0), 0(default)
   The time limit of current function. While the past time exceeds the limitation, the function terminates.
hasRT：True(default), False
   Return a past time or not
suspending: True, False(default)
   Label the suspend state. If true, the F12 wouldn't suspend the program.

Returns
-------
KEY: None, int, or defined value
1. If allowedKeys is None, return the id of any pressed key
2. If allowedKeys is a List (eg. [K_f,K_j]), return the id of allowed pressed key
3. If allowedKeys is a Dict (eg. [K_f:'F',K_j:'J']), return the value of allowed pressed key
4. Return None if the time is out and no allowed keypress
(Only if hasRT is True) pastTime: int
    The millisecond count since the function starts.
```

### *Sound Recorder*
- **environment_noise(samplingTime)**

```
Record the sound in a certain duration as the environment noise, and calcuate its power.

Parameters
----------
todo

Returns
-------
todo
```
- **recordSound(threshold, minRecordTime=0, maxSoundLength=60 * RATE, feedback=False)**

```
Record sound from the microphone and return the data as an array of signed shorts.

Parameters
----------
todo

Returns
-------
todo
```
- **recordSound_tofile(path, filename, threshold, min_record_duration, maxSoundLength)**

```
Record from the microphone and save the sound on disk.

Parameters
----------
todo

Returns
-------
todo
```

---
## IO
### *Read*
- **readSetting(filepath='setting.txt')**

```
Read the setting file and put the items into a dict.
If the 'timingSet' is in the file, create a "timing" in the dict to put the timing parameter.


Parameters
----------
filepath：str (default:'setting.txt')
    The path of the setting file.

Returns
-------
setting: dict
    todo.
```
- **readStimuli(filepath, query=None, sheetname=0, returnList=True)**

```
Get the stimuli from a csv/excel file

Parameters
----------
filepath：str
    The path of the data file
query: str, None(default)
    The query expression (e.g. 'block==1' or 'block>1 and cond=="A"')
sheetname: int (default:0)
    The sheet id of an excel.
returnList: True(default), False
    If returnList is True, then return a list of rows instead of whole table

Returns
-------
stimuli: list of rows(pandas.Series), or whole table (pandas.DataFrame)
    The selected stimuli data
```
- **readDir(dirpath, shuffle=True)**

```
List the files in a directory


Parameters
----------
dirpath：str
    The path of target directory
shuffle: True, False(default)
    Whether shuffle the list or not 

Return
---------
files: list
    The filename list
```

### *Save*
- **saveResult(blockID, resp, columns=['respKey', 'RT'], stim=None, stim_columns=None)**

```
Save experiment result to a file named {subjID}_{blockID}_result.csv.
If stim is not None, the stimuli data would attach to the response result.


Parameters
----------
blockID：int
    The ID of current block
resp：list
    The list of response data
columns: list
    The names of response data columns
stim: pandas.DataFrame, or list
    The data of stimuli
stim_columns: None, or list
    The names of stimuli data columns

Return
---------
None
```

### *Send trigger*
- **sendTrigger(data, mode='P')**

```
Send trigger


Parameters
----------
data: int, or str
    The trigger content
mode: 'P', or 'S'
    The port type: 'P' refers to parallel port, 'S' refers to serial port

Return
---------
None
```

---
## Other Scaffolds
-   **textSlide(text, font='simhei', size='normalFontSize', bgImage=None)**

```
Display a new text slide right now.

Parameters
----------
text：str
    The text on the screen.
font: str (default:'simhei')
    The fontname of the text.
size: str (default:'normalFontSize')
    The fontsize of the text.
bgImage: str, or None(default)
    The path of background picture.
    
Return
---------
None
```
-   **getInput(preText)**

```
Get user input until "ENTER" pressed, then give it to a variable


Parameters
----------
preText：str
    The text that will be displayed before user's input.

Return
---------
input_text: str
    The content of user's input.
```
-   **instruction(instructionText, hasPractice=False)**

```
Show the instruction of experiment
(press 'left' to back, 'right' to continue)


Parameters
----------
instructionText：list of str
    The text that will be displayed as instruction.

Return
---------
resp: Keyname/int
    The last pressed key name.
```
-   **tip(text, allowedKeys=[K_RETURN], outTime=0)**

```
Display a new text slide right now, and keep the screen until user's response.


Parameters
----------
text：str
    The text on the screen.
allowedKeys: Keyname, or list of Keyname (default:[K_RETURN])
    The allowed user's response.
outTime: int(>0) or 0(default)
    The display time limitation of this function.

Return
---------
resp: Keyname/int
    The last pressed key name.
```
-   **alertAndGo(text, outTime=3000)**

```
Display a new text slide right now, 
and keep the screen in a given period of time, or until user pressed SPACE or K_RETURN


Parameters
----------
text：str
    The text on the screen.
outTime: int(>0) or 0(default)
    The display time limitation of this function.

Return
---------
None
```
-   **alertAndQuit(text, outTime=3000)**

```
Display a new text slide right now, 
and keep the screen in a given period of time, or until user pressed SPACE or K_RETURN,
then quit the program.


Parameters
----------
text：str
    The text on the screen.
outTime: int(>0) or 0(default)
    The display time limitation of this function.

Return
---------
None
```
-   **restTime(text='现在实验暂停一会儿，您可以放松一下\n如果休息好了请按 [空格键] 开始实验。')**

```
Suspend the experiment and ask participant to rest:
1. Display a blank screen in 3s,
2. Display a new text slide which tells user to rest, 
3. keep the screen until user pressed SPACE.


Parameters
----------
text：str
    The text on the screen.

Return
---------
None
```

```