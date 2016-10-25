# draw
draw(shape,size,font) 绘制刺激
pos 设定位置
show 将buffer中的内容输出到屏幕(停留的时间,最后是否清空屏幕)

# picture

# sound
loadSound
loadManySound
makeSound
loadMP3
playSound
 todo: 录音

# movie



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