# todo
- todo: format text draw function
- Added the parameter "rotate" to all the `drawXXX`
- Unit of measurement

# 0.9.6.1
- Renamed all the functions to the CamelCase

# 0.9.6
- Renamed the `tip` to `alert`
- Rewrite `recordSound` and `recordSoundToFile`
- Renamed all the parameters to the PascalCase

# 0.9.5.3
- Fixed a bug on parallel port

# 0.9.5.2
- `drawLine` allowed relative position
- Changed "allowed_keys" in `tip`'s default value to [K_RETURN]
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