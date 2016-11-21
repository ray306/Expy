import numpy as np
import pandas as pd
import os
import re
import os
from pygame.locals import *

from expy import shared

# http://stackoverflow.com/questions/892199/detect-record-audio-in-python
from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave


def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM) / max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i * times))
    return r


def addSilence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in range(
        int(seconds * shared.setting['sample_rate']))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds * shared.setting['sample_rate']))])
    return r


def isSilent(snd_data, threshold):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < threshold


def trim(snd_data, threshold, side='left'):
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
        snd_data0 = np.array([int(abs(i) > threshold) for i in snd_data])

        snd_started = False
        r = array('h')

        lasting = 4000
        for i in range(len(snd_data)):
            if not snd_started and snd_data0[i - lasting:i].sum() < (lasting / 20) and snd_data0[i:i + lasting].sum() > (lasting / 3):
                snd_started = True
                r.append(snd_data[i])

            elif snd_started:
                r.append(snd_data[i])
        return r

    if side == 'left':
        # Trim to the left
        snd_data = _trim(snd_data)
    elif side == 'right':
        # Trim to the right
        snd_data.reverse()
        snd_data = _trim(snd_data)
        snd_data.reverse()
    elif side == 'both':
        # Trim to the left
        snd_data = _trim(snd_data)
        # Trim to the right
        snd_data.reverse()
        snd_data = _trim(snd_data)
        snd_data.reverse()
    elif side == 'none':
        pass

    return snd_data


def environmentNoise(sampling_time, chunk=512):
    """
    Record the sound in a certain duration as the environment noise, and calcuate its power.

    Parameters
    ----------
    todo

    Returns
    -------
    todo
    """
    def calc_threshold():
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=shared.setting['sample_rate'],
                        input=True, output=True,
                        frames_per_buffer=chunk)

        r = array('h')

        noise = []
        for i in range(int(sampling_time * shared.setting['sample_rate'] // chunk)):
            # little endian, signed short
            snd_data = array('h', stream.read(chunk))
            if byteorder == 'big':
                snd_data.byteswap()
            r.extend(snd_data)
            noise.append(max(snd_data))

        return np.mean(noise[1:])

    threshold = -1
    while threshold < 0:
        threshold = calc_threshold()

    print("environment's noise level:", threshold)
    return threshold


# def recordSound(threshold, minRecordTime=0, maxSoundLength=600, feedback=False, chunk=512):
#     """
#     Record sound from the microphone and return the data as an array of signed shorts.

#     Parameters
#     ----------
#     todo

#     Returns
#     -------
#     todo
#     """
#     sr = shared.setting['sample_rate']

#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paInt16, channels=1, rate=sr,
#                     input=True, output=True,
#                     frames_per_buffer=chunk)

#     num_silent = 0
#     speech_threshold = 4 * threshold
#     num_sound = 0
#     silent_limit = 1 * sr

#     minRecordTime = minRecordTime * sr
#     maxSoundLength = maxSoundLength * sr

#     onset = 0
#     onset_detected = False

#     r = array('h')
#     while num_sound < maxSoundLength and len(r) < (minRecordTime + maxSoundLength) and num_silent < silent_limit:
#         # little endian, signed short
#         s = stream.read(chunk)
#         if feedback:
#             stream.write(s, chunk)

#         snd_data = array('h', s)
#         if byteorder == 'big':
#             snd_data.byteswap()
#         r.extend(snd_data)

#         # for e in shared.pg.event.get():
#         #     if e.type == KEYDOWN:
#         #         k = e.key
#         #         if k == 27:
#         #             shared.pg.quit()
#         #         elif k == K_F12:
#         #             suspend()

#         if onset_detected:
#             num_sound += len(snd_data)

#             if isSilent(snd_data, threshold):
#                 num_silent += len(snd_data)
#             else:
#                 num_silent = 0
#         else:
#             if max(snd_data) > speech_threshold:
#                 for idx in range(1, len(r), chunk):
#                     if np.max(r[-idx - chunk:-idx]) < threshold:
#                         onset = len(r) - idx - chunk
#                         onset_detected = True
#                         break

#     sample_width = p.get_sample_size(pyaudio.paInt16)
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     r = trim(r, threshold)
#     # r = normalize(r)
#     r = r[:maxSoundLength]
#     r = np.require(np.tile(r, (2, 1)).T, requirements='C')
#     # r = addSilence(r, 0.5)
#     return sample_width, r

def recordSound(noise_level=500, recording_min=0, recording_max=0, sounding_max=0, trim_side='left', feedback=False, chunk=512):
    # 左边的干净是trim（left）得来的，不是由计算的onset 得来的
    """
    Record sound from the microphone and return the data as an array of signed shorts.

    Parameters
    ----------
    todo

    Returns
    -------
    todo
    """
    sr = shared.setting['sample_rate']

    recording_min = recording_min * sr
    if recording_max > 0:
        recording_max = recording_max * sr
    if sounding_max > 0:
        sounding_max = sounding_max * sr

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sr,
                    input=True, output=True,
                    frames_per_buffer=chunk)

    speech_threshold = 4 * noise_level
    silence_limit = 1 * sr

    num_silent = 0
    num_sound = 0
    onset = 0
    onset_detected = False

    rec_data = array('h')
    while True:
        # little endian, signed short
        s = stream.read(chunk)

        if feedback:
            stream.write(s, chunk)

        snd_data = array('h', s)
        if byteorder == 'big':
            snd_data.byteswap()
        rec_data.extend(snd_data)

        if onset_detected:
            num_sound += len(snd_data)

            if isSilent(snd_data, noise_level):
                num_silent += len(snd_data)
            else:
                num_silent = 0
        else:
            if max(snd_data) > speech_threshold:
                for idx in range(1, len(rec_data), chunk):
                    if np.max(rec_data[-idx - chunk:-idx]) < noise_level:
                        onset = len(rec_data) - idx - chunk
                        onset_detected = True
                        break

        for e in shared.pg.event.get():
            if e.type == KEYDOWN:
                k = e.key
                if k == 27:
                    shared.pg.quit()
                elif k == K_F12:
                    suspend()

        # When to stop recording
        if (recording_max > 0 and len(rec_data) > recording_max) or \
                (sounding_max > 0 and num_sound > sounding_max) or \
                (len(rec_data) > recording_min and num_silent > silence_limit):
            rec_data = rec_data[onset:]
            rec_data = trim(rec_data, noise_level, side=trim_side)
            if sounding_max>0: 
                rec_data = rec_data[:int(sounding_max)]
            break

    sample_width = p.get_sample_size(pyaudio.paInt16)
    stream.stop_stream()
    stream.close()
    p.terminate()

    # rec_data = normalize(rec_data)
    # rec_data = addSilence(rec_data, 0.5)
    rec_data = np.require(np.tile(rec_data, (2, 1)).T, requirements='C')

    return sample_width, rec_data


def recordSoundTofile(filename, path='data', noise_level=500, recording_min=0, recording_max=0, sounding_max=0, trim_side='left', feedback=False, chunk=512):
    """
    Record from the microphone and save the sound on disk.

    Parameters
    ----------
    todo

    Returns
    -------
    todo
    """
    try:
        sample_width, data = recordSound(
            noise_level, recording_min, recording_max, sounding_max, trim_side, feedback, chunk)

        data = pack('<' + ('h' * len(data[:, 0])), *data[:, 0])

        wf = wave.open('%s/%s.wav' %(path, filename), 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(shared.setting['sample_rate'])
        wf.writeframes(data)
        wf.close()
        return True
    except:
        return False