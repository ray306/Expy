import numpy as np
import pandas as pd
import os
import re
import os

from expy import shared


# http://stackoverflow.com/questions/892199/detect-record-audio-in-python
from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave

CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in range(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds*RATE))])
    return r

def is_silent(snd_data,threshold):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < threshold

def trim(snd_data,threshold):
    "Trim the blank spots at the start and end"
#     def _trim(snd_data):
#         snd_started = False
#         r = array('h')

#         for i in snd_data:
#             if not snd_started and abs(i)>threshold:
#                 snd_started = True
#                 r.append(i)

#             elif snd_started:
#                 r.append(i)
#         return r
    
    def _trim(snd_data):
        snd_data0 = np.array([int(abs(i)>threshold) for i in snd_data])

        snd_started = False
        r = array('h')
        
        lasting = 4000
        for i in range(len(snd_data)):
            if not snd_started and snd_data0[i-lasting:i].sum()<(lasting/20) and snd_data0[i:i+lasting].sum()>(lasting/3):
                snd_started = True
                r.append(snd_data[i])

            elif snd_started:
                r.append(snd_data[i])
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

#     # Trim to the right
#     snd_data.reverse()
#     snd_data = _trim(snd_data)
#     snd_data.reverse()
    return snd_data

def environment_noise(sample_duration):
    """
    Record a word or words from the microphone and 
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the 
    start and end, and pads with 0.5 seconds of 
    blank sound to make sure VLC et al can play 
    it without getting chopped off.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    r = array('h')
    
    noise = []
    for i in range(int(sample_duration*RATE//CHUNK_SIZE)):
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)
        noise.append(max(snd_data))

    return np.mean(noise[1:])

def recordSound(threshold,min_record_duration=0,max_sound_duration=60*RATE):
    """
    Record a word or words from the microphone and 
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the 
    start and end, and pads with 0.5 seconds of 
    blank sound to make sure VLC et al can play 
    it without getting chopped off.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    num_sound = 0
    silent_limit = 1*RATE
    
    onset = 0
    onset_detected = False

    r = array('h')
    while num_sound<max_sound_duration and len(r)<(min_record_duration+max_sound_duration) and num_silent < silent_limit:
        # little endian, signed short
        s = stream.read(CHUNK_SIZE)
        stream.write(s, CHUNK_SIZE)
        snd_data = array('h', s)
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        if onset_detected:
            num_sound += len(snd_data)
            
            if is_silent(snd_data,threshold):
                num_silent += len(snd_data)
            else:
                num_silent  = 0
        else:
            if max(snd_data)>6000:
                for idx in range(1,len(r),CHUNK_SIZE):
                    if np.max(r[-idx-CHUNK_SIZE:-idx])<threshold:
                        onset = len(r)-idx-CHUNK_SIZE
                        onset_detected = True
                        break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = trim(r,threshold)
    r = normalize(r)
    r = r[:max_sound_duration]
#     r = add_silence(r, 0.5)
    return sample_width, r

def recordSound_tofile(path,filename,threshold,min_record_duration,max_sound_duration):
    "Records from the microphone and outputs the resulting data to 'path'"
    try:
        sample_width, data = recordSound(threshold,min_record_duration,max_sound_duration)

        data = pack('<' + ('h'*len(data)), *data)

        wf = wave.open(path+filename+'.wav', 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()
        return True
    except:
        return False