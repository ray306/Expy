# todo
- todo: format text draw function
- Added the parameter "rotate" to all the `drawXXX`

# 0.9.4.1
- Clear screen in the end of `getInput`

# 0.9.4
- Added the parameter "hasRT" to `waitForResponse`
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
- Added the parameter "block" to `playSound`
- Now the `getPos` function can use more position's benchmarks: center(default), upper_left, upper_right, lower_left, lower_right, upper_center, left_center, lower_center, right_center
- All the `drawXXX` functions support the "benchmark" parameter 
- Custom fonts size in setting.txt
- Removed `drawFixed`,`drawWord`
- 'sendTrigger' function
- Added the parameter "feedback" to `recordSound`

---
# 0.9.1
First released version