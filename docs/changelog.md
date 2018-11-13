# Todo
- auto check the working port
- two screen or online report : flask server html ajax
- Format text draw method
- abstract every methods in the beginning - to speed up the startup 

# 0.9.13.9
- Fixed an important issue that sleeping interval in `waitForResponse()` is 0.1s so that the result could be strongly biased!

# 0.9.13.8
- Added method `button()`
- Fixed an issue in `ClickRange()`

# 0.9.13.7
- Now the parameter `w`,`h`,`x`,`y` in `getPos()` can be set as int or float indepently.
- Set the default text 'Please enter the subject ID:' for `getSubjectID()`

# 0.9.13.6
- Fixed an issue that `clean_screen=False` doesn't work in `show()`

# 0.9.13.5
- Fixed an issue of `saveResult()`
- Fixed an issue that the program won't actually stop after pressing "ESC"
- Now `log()` supports the multiple parameters

# 0.9.13.4
- Fixed an issue of `stop_signal`
- Fixed an issue of `log()`
- Fixed an issue of `restTime()`

# 0.9.13.3
- Now `getInput()` support the numbers on keypad.

# 0.9.13.2
- Fixed an issue of `stop_signal`
- Fixed the issue of parameter `background_image` in a lot of methods
- Added paramter `background_image` in method `restTime()`
- [beta] Added paramter `background_music` in method `restTime()`

# 0.9.13
- Added the external control of precedure via network. You can set parameter `stop_signal` in method `show()`

# 0.9.12
- Changed the default value of paramter `diag` and `angel` in `start()` to **15** and **1.6**
- Changed the default value of paramter `vsync` in `start()` to **True**

# 0.9.11.5
- Added the default value to parameter `text` of method `instruction()` 

# 0.9.11.4
- Fixed an issue that the graph cannot be remained on the screen sometimes

# 0.9.11.3
- Added method `getTrigger()`
- Modify method `sendTrigger()`, supported more *str* input and *bytes* input
- [beta] Added parameter `trigger` to the stimulus display methods
- [beta] Added method `port_watcher()` to shared.py

# 0.9.11.2
- Fixed an issue that `fill` didn't work in `drawRect()`
- Added return values (width, height) in `drawText()`
- Changed the definition of "sys.path" in all test files

# 0.9.11.1
- Fixed an issue that `fill` didn't show color in `drawCircle()`

# 0.9.11
- Changed the parameter `display` of `drawXXX` to `show_now`
- Fixed an issue of sending trigger to the parallel port
- Fixed an issue of `anchor_x` and `anchor_y`
- Fixed an issue that F12 can't recover the screen

# 0.9.10.3
- [Beta] `vsync=False` in method `start`
- [Beta] Added parameter `timeit` to all method of sound playing and figure displaying
- [Beta] Changed the executing order of flip() and sendTrigger() for the parameter `trigger`

# 0.9.10.2
- Added a test for measuring time delay (`time_delay.py`)
- The program will print the path of current Expy

# 0.9.10.1
- Added method `changeOnTracks`
- Renamed the method `mono2stereo` to `toStereoArray`
- Renamed the method `change_volume` to `changeVolume`
- Added parameter `stereo_array_format` to `loadSound`, `loadManySound`, `makeBeep`, and `makeNoise`.
- Renamed method  `normal_procedure` to `normalProcedure`
- Renamed method  `playSound` to `playBusySound`.
- New a method named `playSound`, its parameter `busy` determines the run of `playBusySound` or `playFreeSound`
- Added parameter `vsync` to method `start`
- [Beta] Added parameter `trigger` to all method of sound playing and figure displaying

# 0.9.9
- Fixed possible issues of reading setting file
- Automaticly create setting file if it doesn't exist
- Changed default value of parameter `port` to '' in method `start`
- Added plug-in method `normalProcedure`
- Added method `getSubjectID`
- Added method `playAlterableSound`
- Readded method `makeNoise`
- Separate method `playSound` by the parameter `blocking`. Now the `blocking=True` version is named as `playSound`, and the `blocking=False` version is named as `playFreeSound`

# 0.9.8.1
- Fixed an cruical issue of suspend method
- Fixed an issue of serial port

# 0.9.8
- [**Important**] Unified the units of time. Now we use SECONDs in all methods.
- Added parameter `saveas` to `saveResult`. Now the `saveResult` support Excel file.
- Now `saveResult` supported update the result.
- Fixed an issue of `restTime`

# 0.9.7.7
- Fixed an issue of reading setting file.

# 0.9.7.6
- Fixed issues of closing method on MacOSX
- Fixed an issue of suspending
- Added method `makeNoise`
- Exchanged the parameter locations of *out_time* and *allowed_keys* in `alert`, `alertAndGo`, `alertAndQuit`

# 0.9.7.5
- Added method `log` that can record current event and its time from onset.
- Added method `whilePressing` that allow something keeping while pressing.
- Added parameter `action_while_pressing` to `waitForResponse`. Now `waitForResponse` supported action while pressing and could record the pressed duration.
- Added parameter `allowed_clicks` to `waitForResponse`. Now `waitForResponse` supported mouse events.

# 0.9.7.4
- Fixed the `clear`
- Added position parameters for `textSlide` and `textSlide` based methods.

# 0.9.7.3
- Fixed the display issue of default font under MacOSX

# 0.9.7.2
- Removed parllel port module in Linux and MacOSX
- Time unit changed to millisecond in `recordSound`

# 0.9.7.1
- Fixed bugs

# 0.9.7
- [**Important**] Changed the backend! Rewrite all the code!
- Added the controller method `shared.changeState(idx, value)`
- Coordinate change: (0, 0) means lower-left at screen
- The change of position benchmark definition in `drawXXX`: 
    - [old way] anchor="upper_left"
    - [new_way] anchor_x='left',anchor_y='top'
- Added video support
    - Method `loadVideo`: it supports a lot of video format if you installed AVbin (http://avbin.github.io/AVbin/Download.html)
    - Method `playVideo`: you can control the play stream
- `environmentNoise`
    - Now `environmentNoise` measures zero-crossing rate and amplitude of noise
    - Now `environmentNoise` supports pre-defining the VAD weights via the parameter "weights"
    - Now `environmentNoise` returns the VAD parameters
- `recordSound`
    - Fixed the bug of `recordSound` about the voice activity detection
    - Added "vad_levels" to `environmentNoise` and removed the "noise_level"
    - Added the parameter "blocking" to `recordSound`, and so you can continue the experiment procedure while recording
    - Added the parameter "path" to `recordSound` and removed the method `recordSoundToFile`
    - Added the parameter "playing_track" to `recordSound`, and so you can control the recording outside.
- Changed the backend of sound playing! Now Expy supports a lot of sound file format if you installed FFmpeg (https://ffmpeg.org/download.html)
- Added the parameter "playing_track" to `playSound`, and so you can control the playing outside
- Now `saveResult` supports string and int as the value of "block_tag"
- Renamed the `drawLine` to `drawLines`
- Added the parameter "out_time" to `getInput`
- Silenced the effect of parameter "rotate" to all the `drawXXX`. I will active them in a future version.

# 0.9.6.1
- Renamed all the methods to the CamelCase

# 0.9.6
- Renamed the `tip` to `alert`
- Rewrite `recordSound` and `recordSoundToFile`
- Renamed all the parameters to the UnderlineCase

# 0.9.5.3
- Fixed an bug on parallel port

# 0.9.5.2
- `drawLine` allowed relative position
- Changed "allowed_keys" in `tip`'s default value to [key.RETURN]
- Now the `show` won't stop if you press SPACE (it only will when RETURN)
- `loadManySound` allowed mono channel

# 0.9.5.1
- Changed the default value of 'size' in the `drawText` to 'stim_font_size'

# 0.9.5
- Supported colornames: C_black, C_white, C_red, C_lime, C_blue, C_yellow, C_aqua, C_fuchsia, C_silver, C_gray, C_maroon, C_olive, C_green, C_purple, C_teal, C_navy
- Import time package while importing expy
- Added the parameters "font", "size", "rotation" and "color" to `drawText` (used Freetype as the backend)
- 1.5x row spacing when multiple lines appear.

# 0.9.4.3
- Import pandas(as pd), random while importing expy
- Added the parameter "query" to `readStimuli`

# 0.9.4.1
- Clear screen in the end of `getInput`
- Changed return value of `readStimuli` to list

# 0.9.4
- Added the parameter "has_RT" to `waitForResponse`
- Removed `waitForEvent`
- Press F12 to suspend/resume
- Added the parameter "rotate" to `drawPic`
- Modified `instruction`
- Added the parameter "display" to all the `drawXXX`. The default "display" value is True, so you needn't call the `show()` after `drawXXX()` now.
- Some tiny changes.

# 0.9.3.2
- Fixed the error when running `sendTrigger` without available port.
- Fixed the error when setting.txt doesn't exist.
- Fixed the error of `import pyglet`

# 0.9.3.1
- Added the parameter "winsize" to `start`
- fix the remained time after run `suspend` 

# 0.9.3
- Press F12 to suspend the program, and press anykey to continue.
- `recordSound_tofile` and `recordSound` allowed press F12 to suspend and ESC to quit.
- Added the parameter "blocking" to `playSound`
- Now the `getPos` method can use more position's benchmarks: center(default), upper_left, upper_right, lower_left, lower_right, upper_center, left_center, lower_center, right_center
- All the `drawXXX` methods support the "benchmark" parameter 
- Custom fonts size in setting.txt
- Removed `drawFixed`,`drawWord`
- 'sendTrigger' method
- Added the parameter "feedback" to `recordSound`

---
# 0.9.1
First released version