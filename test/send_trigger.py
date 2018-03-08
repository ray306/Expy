# coding:utf-8
##### package test #####
import sys
sys.path = ['../']+sys.path
################
print(sys.version)

from expy import *  # Import the needed functions

'Parallel Port'
# start(port=0xC100)
# sendTrigger(0, mode='P')

'Serial Port'
start(port='COM5')
sendTrigger('m$', mode='S')

# import serial
# ser = serial.Serial(baudrate=115200)
# ser.port = 'COM1' # set the port
# try:
#     ser.open()
# except:
#     print('Could not open port')

# ser.write(b'something') # send a string directly

# tg = 'something'
# ser.write(bytes(tg,encoding='utf8')) # send a string which might change

# n=int('0b00010001',2)
# ser.write(n.to_bytes((n.bit_length()+7)//8, 'big')) # send a binary code
