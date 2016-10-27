# coding:utf-8
##### package test #####
import sys
sys.path.append('../../')
################

from expy import * # Import the needed functions
start() # Initiate the experiment environment

'Parallel Port'
shared.Objdll.Out32(0xC100,0) # 0xC100 is the port, 0 is the data

'Serial Port'
import serial
ser = serial.Serial()
ser.baudrate= 115200
ser.port = 'COM1' # set the port
ser.open()

ser.write(b'something') # send a string directly

tg = 'something'
ser.write(bytes(tg,encoding='utf8')) # send a string which might change

n=int('0b00010001',2)
ser.write(n.to_bytes((n.bit_length()+7)//8, 'big')) # send a binary code