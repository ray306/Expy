# coding:utf-8
##### package test #####
import sys
sys.path = ['../']+sys.path
################
print(sys.version)

# from expy import *  # Import the needed functions

'Parallel Port'
start(port=0xC100)
sendTrigger(0, mode='P')

'Serial Port'
start(port='COM5')
sendTrigger('m$', mode='S')

# import serial
# import time
# ser = serial.Serial(baudrate=115200)
# ser.port = 'COM5' # set the port
# try:
#     ser.open()
# except:
#     print('Could not open port')

# time.sleep(5)
# # ser.write(chr(64))  # send a string directly
# print('1')
# for i in range(13,25):
#     print(i)
#     ser.write(b'\x4d'+bytes([i]))
#     time.sleep(1)


# print(ser.read())
# ser.write()
# ser.write(chr(64))


# tg = 'something'
# ser.write(bytes(tg,encoding='utf8')) # send a string which might change

# n=int('0b00010001',2)
# ser.write(n.to_bytes((n.bit_length()+7)//8, 'big')) # send a binary code
