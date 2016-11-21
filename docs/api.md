## Initialization
- **start(setting_file='setting.txt', fullscreen=True, winsize=(800, 600), mouse_visible=False, normal_font_size=20, stim_font_size=None, distance=60, diag=23, angel=2.5, font_color=(255, 255, 255), background_color=(128, 128, 128), sample_rate=44100, bits=16, channel=2, port='COM1')**

```
Initialize the experiment.
Note: todo.

Parameters
----------
setting_file: str (default: 'setting.txt')
    The filepath of setting
fullscreen: True(default), or False 
    Whether the window is fullscreen
winsize: (width,height) (default:(800, 600)) 
    The size of window
mouse_visible: True, or False(default)
    Set the mouse pointer visibility
normal_font_size: int (default:20) 
    The size of normal/['normalFont'] text 
stim_font_size: int, or None(default) 
    The size of ['stimFont'] text 
distance: int (default:60) 
    Distance from eyes to screen (cm)
diag: int (default:23) 
    The length of the screen diagonal (inch) 
angel: int (default:2.5) 
    Visual angel of single char (degree)
font_color: tuple RGB (default:(255, 255, 255)) 
    The color of text
background_color: tuple RGB (default:(128, 128, 128)) 
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
- **getPos(x=shared.win_width // 2, y=shared.win_height // 2, w=0, h=0, benchmark='center')**

```
Caluate the screen position of object

Parameters
----------
x: float or int (default: shared.win_width // 2)
    If x is float, it represents the x-offset(-1~1 scale) from the object benchmark to the screen center,
    if int, it represents the x-offset(pixel) from the object benchmark to the screen upperleft.
y: float or int (default: shared.win_height // 2)
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
- **drawText(text, font='simhei', size='stim_font_size', color=C_white, rotation=0, x=0.0, y=0.0, benchmark='center', display=True)**

```
Draw text on the canvas. The text will show as multiple lines splited by the '\n'. 

Parameters
----------
text: str
    The content of text.
font: str (default:'simhei')
    The font name of text.
size:int, or str (default:'stim_font_size')
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
- **playSound(wav=None, blocking=True)**

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
- **show(out_time=False, clean_screen=True, backup=None)**

```
Display current canvas buffer, and keep the display during a limited period.

Parameters
----------
out_time: int(>0), False(default)
    The time limit of current function. 
clean_screen: True(default), False
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
- **getScreen(clean_screen=True)**

```
Get a backup of current canvas

Parameters
----------
clean_screen: True(default), False
    Whether clear the screen after get the screen or not. 

Returns
-------
None
```

---
## Response
### *Keyboard & Mouse & Joystick*
-    **waitForResponse(allowed_keys=None, out_time=0, has_RT=True, suspending=False)**

```
Waiting for a allowed keypress event during a limited period
(Press F12 would suspend the procedure and press ESC would end the program)

Parameters
----------
allowed_keys：None(default), Keyname, list, or dict
   The allowed key(s).
   You can leave nothing, 
           a Keyname (eg. K_f), 
           a list of Keyname (eg. [K_f,K_j]), 
           or a dict of Keyname (eg. [K_f:'F',K_j:'J']) here.
   You could look into the Keyname you want in http://expy.readthedocs.io/en/latest/keymap/
out_time：int(>0), 0(default)
   The time limit of current function. While the past time exceeds the limitation, the function terminates.
has_RT：True(default), False
   Return a past time or not
suspending: True, False(default)
   Label the suspend state. If true, the F12 wouldn't suspend the program.

Returns
-------
KEY: None, int, or defined value
1. If allowed_keys is None, return the id of any pressed key
2. If allowed_keys is a List (eg. [K_f,K_j]), return the id of allowed pressed key
3. If allowed_keys is a Dict (eg. [K_f:'F',K_j:'J']), return the value of allowed pressed key
4. Return None if the time is out and no allowed keypress
(Only if has_RT is True) pastTime: int
    The millisecond count since the function starts.
```

### *Sound Recorder*
- **environment_noise(sampling_time)**

```
Record the sound in a certain duration as the environment noise, and calcuate its power.

Parameters
----------
todo

Returns
-------
todo
```
- **recordSound(noise_level, recording_min=0, recording_max=0, sounding_max=0, trim_side='left', feedback=False, chunk=512)**

```
Record sound from the microphone and return the data as an array of signed shorts.

Parameters
----------
todo

Returns
-------
todo
```
- **recordSoundTofile(path, filename, noise_level, recording_min=0, recording_max=0, sounding_max=0, trim_side='left', feedback=False, chunk=512)**

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
If the 'timing_set' is in the file, create a "timing" in the dict to put the timing parameter.


Parameters
----------
filepath：str (default:'setting.txt')
    The path of the setting file.

Returns
-------
setting: dict
    todo.
```
- **readStimuli(filepath, query=None, sheetname=0, return_list=True)**

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
return_list: True(default), False
    If return_list is True, then return a list of rows instead of whole table

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
- **saveResult(block_id, resp, columns=['respKey', 'RT'], stim=None, stim_columns=None)**

```
Save experiment result to a file named {subject_id}_{block_id}_result.csv.
If stim is not None, the stimuli data would attach to the response result.


Parameters
----------
block_id：int
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
-   **textSlide(text, font='simhei', size='normal_font_size', background_image=None)**

```
Display a new text slide right now.

Parameters
----------
text：str
    The text on the screen.
font: str (default:'simhei')
    The fontname of the text.
size: str (default:'normal_font_size')
    The fontsize of the text.
background_image: str, or None(default)
    The path of background picture.
    
Return
---------
None
```
-   **getInput(pre_text)**

```
Get user input until "ENTER" pressed, then give it to a variable


Parameters
----------
pre_text：str
    The text that will be displayed before user's input.

Return
---------
input_text: str
    The content of user's input.
```
-   **instruction(instruction_text, has_practice=False)**

```
Show the instruction of experiment
(press 'left' to back, 'right' to continue)


Parameters
----------
instruction_text：list of str
    The text that will be displayed as instruction.

Return
---------
resp: Keyname/int
    The last pressed key name.
```
-   **alert(text, allowed_keys=[K_RETURN], out_time=0)**

```
Display a new text slide right now, and keep the screen until user's response.


Parameters
----------
text：str
    The text on the screen.
allowed_keys: Keyname, or list of Keyname (default:[K_RETURN])
    The allowed user's response.
out_time: int(>0) or 0(default)
    The display time limitation of this function.

Return
---------
resp: Keyname/int
    The last pressed key name.
```
-   **alertAndGo(text, out_time=3000)**

```
Display a new text slide right now, 
and keep the screen in a given period of time, or until user pressed SPACE or K_RETURN


Parameters
----------
text：str
    The text on the screen.
out_time: int(>0) or 0(default)
    The display time limitation of this function.

Return
---------
None
```
-   **alertAndQuit(text, out_time=3000)**

```
Display a new text slide right now, 
and keep the screen in a given period of time, or until user pressed SPACE or K_RETURN,
then quit the program.


Parameters
----------
text：str
    The text on the screen.
out_time: int(>0) or 0(default)
    The display time limitation of this function.

Return
---------
None
```

-   **restTime(text=rest_text)**

```
Suspend the experiment and ask participant to rest:
1. Display a blank screen in 3s,
2. Display a new text slide which tells user to rest, 
3. keep the screen until user pressed SPACE.

rest_text = '实验暂停，您可以休息一会\n\
如果休息结束请按 [空格] 继续实验。\n\
Now you could have a rest,\n \
please press [SPACE] key when you decide to continue.\n'


Parameters
----------
text：str
    The text on the screen.

Return
---------
None
```

```