# Todo
- Format text draw function

# 0.9.10.1
- Added function `changeOnTracks`
- Renamed the function `mono2stereo` to `toStereoArray`
- Renamed the function `change_volume` to `changeVolume`
- Added parameter `stereo_array_format` to `loadSound`, `loadManySound`, `makeBeep`, and `makeNoise`.
- Renamed function  `normal_procedure` to `normalProcedure`
- Renamed function  `playSound` to `playBusySound`.
- New a function named `playSound`, its parameter `busy` determines the run of `playBusySound` or `playFreeSound`
- Added parameter `vsync` to function `start`
- [Beta] Added parameter `trigger` to all function of sound playing and figure displaying

# 0.9.9
- Fixed possible issues of reading setting file
- Automaticly create setting file if it doesn't exist
- Changed default value of parameter `port` to '' in function `start`
- Added plug-in function `normalProcedure`
- Added function `getSubjectID`
- Added function `playAlterableSound`
- Readded function `makeNoise`
- Separate function `playSound` by the parameter `blocking`. Now the `blocking=True` version is named as `playSound`, and the `blocking=False` version is named as `playFreeSound`

# 0.9.8.1
- Fixed a cruical issue of suspend function
- Fixed an issue of serial port

# 0.9.8
- [**Important**] Unified the units of time. Now we use SECONDs in all functions.
- Added parameter `saveas` to `saveResult`. Now the `saveResult` support Excel file.
- Now `saveResult` supported update the result.
- Fixed an issue of `restTime`

# 0.9.7.7
- Fixed an issue of reading setting file.

# 0.9.7.6
- Fixed issues of closing function on MacOSX
- Fixed an issue of suspending
- Added function `makeNoise`
- Exchanged the parameter locations of *out_time* and *allowed_keys* in `alert`, `alertAndGo`, `alertAndQuit`

# 0.9.7.5
- Added function `log` that can record current event and its time from onset.
- Added function `whilePressing` that allow something keeping while pressing.
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
- Added the controller function `shared.changeState(idx, value)`
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
- Renamed all the functions to the CamelCase

# 0.9.6
- Renamed the `tip` to `alert`
- Rewrite `recordSound` and `recordSoundToFile`
- Renamed all the parameters to the UnderlineCase

# 0.9.5.3
- Fixed a bug on parallel port

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
- Now the `getPos` function can use more position's benchmarks: center(default), upper_left, upper_right, lower_left, lower_right, upper_center, left_center, lower_center, right_center
- All the `drawXXX` functions support the "benchmark" parameter 
- Custom fonts size in setting.txt
- Removed `drawFixed`,`drawWord`
- 'sendTrigger' function
- Added the parameter "feedback" to `recordSound`

---
# 0.9.1
First released version