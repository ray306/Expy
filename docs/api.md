# API referrence
---
## Initiation
- ```start()```: Environment Setting

---
## Stimulus
### *Text*
- ```drawText()```
### *Shape*
- ```drawLine()```
- ```drawRect()```
- ```drawCircle()```
### *Picture*
- ```drawPic()```
### *Sound*
- ```loadSound(path)```
- ```loadManySound(dirpath, filenames, ext='wav')```
- ```makeSound(freq, duration)```
- ```playSound(wav=None, block=True)```
### *Video*
### *Display controller*
- ```show(outTime=False, cleanScreen=True, backup=None)```: Display current canvas buffer, and keep the display during a limited period.
- ```clear()```: Clear the screen
- ```getScreen(cleanScreen=True)```: Get a backup of current canvas

---
## Response
### *Keyboard & Mouse & Joystick*
- ```waitForResponse(allowedKeys=None, outTime=0, hasRT=True, suspending=False)```: Waiting for a allowed keypress event during a limited period
### *Sound Recorder*
- ```environment_noise(samplingTime)```
- ```recordSound(threshold, minRecordTime=0, maxSoundLength=60 * RATE, feedback=False)```
- ```recordSound_tofile(path, filename, threshold, min_record_duration, maxSoundLength)```

---
## IO
### *Read*
- ```readSetting(filepath='setting.txt')```: Read the setting file and put the items into a dict
- ```readStimuli(filepath, blockID=None, sheetname=0)```: Get the stimuli from a csv/excel file
- ```readDir(dirpath, shuffle=True)```: List the files in a directory
### *Save*
- ```saveResult(blockID, resp, columns=['respKey', 'RT'], stim=None, stim_columns=None)```: Save experiment result to a file named {subjID}\_{blockID}\_result.csv. If stim is not None, the stimuli data would attach to the response result.

### *Send trigger*
- ```sendTrigger(data, mode='P')```: Send trigger

---
## Other Scaffolds
- ```textSlide(text, fontname='normalFont', bgImage=None)```: Display text on a new slide
- ```getInput(preText)```: Get user input until "ENTER" pressed, then give it to a variable
- ```instruction(instructionText, hasPractice=False)```: Show the instruction of experiment
- ```tip(text, allowedKeys=[K_SPACE, K_RETURN], outTime=0)```:  Show something until "SPACE" or "RETURN" pressed
- ```alertAndGo(text, outTime=3000)```: Show something during a limited period, and continue
- ```alertAndQuit(text, outTime=3000)```: Show something during a limited period, and quit the program
- ```restTime(text='现在实验暂停一会儿，您可以放松一下\n如果休息好了请按 [空格键] 开始实验。')```: Suspend the experiment and ask participant to rest, until "SPACE" or "RETURN" pressed