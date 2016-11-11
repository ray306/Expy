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


def normalize(sndData):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM) / max(abs(i) for i in sndData)

    r = array('h')
    for i in sndData:
        r.append(int(i * times))
    return r


def add_silence(sndData, seconds):
    "Add silence to the start and end of 'sndData' of length 'seconds' (float)"
    r = array('h', [0 for i in range(int(seconds * RATE))])
    r.extend(sndData)
    r.extend([0 for i in range(int(seconds * RATE))])
    return r


def is_silent(sndData, threshold):
    "Returns 'True' if below the 'silent' threshold"
    return max(sndData) < threshold


def trim(sndData, threshold):
    "Trim the blank spots at the start and end"
#     def _trim(sndData):
#         snd_started = False
#         r = array('h')

#         for i in sndData:
#             if not snd_started and abs(i)>threshold:
#                 snd_started = True
#                 r.append(i)

#             elif snd_started:
#                 r.append(i)
#         return r

    def _trim(sndData):
        sndData0 = np.array([int(abs(i) > threshold) for i in sndData])

        snd_started = False
        r = array('h')

        lasting = 4000
        for i in range(len(sndData)):
            if not snd_started and sndData0[i - lasting:i].sum() < (lasting / 20) and sndData0[i:i + lasting].sum() > (lasting / 3):
                snd_started = True
                r.append(sndData[i])

            elif snd_started:
                r.append(sndData[i])
        return r

    # Trim to the left
    sndData = _trim(sndData)

#     # Trim to the right
#     sndData.reverse()
#     sndData = _trim(sndData)
#     sndData.reverse()
    return sndData


def environment_noise(samplingTime):
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
        stream = p.open(format=FORMAT, channels=1, rate=RATE,
                        input=True, output=True,
                        frames_per_buffer=CHUNK_SIZE)

        r = array('h')

        noise = []
        for i in range(int(samplingTime * RATE // CHUNK_SIZE)):
            # little endian, signed short
            sndData = array('h', stream.read(CHUNK_SIZE))
            if byteorder == 'big':
                sndData.byteswap()
            r.extend(sndData)
            noise.append(max(sndData))

        return np.mean(noise[1:])

    threshold = -1
    while threshold < 0:
        threshold = calc_threshold()

    print("environment's noise level:", threshold)
    return threshold


def recordSound(threshold, minRecordTime=0, maxSoundLength=60 * RATE, feedback=False):
    """
    Record sound from the microphone and return the data as an array of signed shorts.

    Parameters
    ----------
    todo

    Returns
    -------
    todo
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
                    input=True, output=True,
                    frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    speech_threshold = 4 * threshold
    num_sound = 0
    silent_limit = 1 * RATE

    onset = 0
    onset_detected = False

    r = array('h')
    while num_sound < maxSoundLength and len(r) < (minRecordTime + maxSoundLength) and num_silent < silent_limit:
        # little endian, signed short
        s = stream.read(CHUNK_SIZE)
        if feedback:
            stream.write(s, CHUNK_SIZE)

        sndData = array('h', s)
        if byteorder == 'big':
            sndData.byteswap()
        r.extend(sndData)

        # for e in shared.pg.event.get():
        #     if e.type == KEYDOWN:
        #         k = e.key
        #         if k == 27:
        #             shared.pg.quit()
        #         elif k == K_F12:
        #             suspend()

        if onset_detected:
            num_sound += len(sndData)

            if is_silent(sndData, threshold):
                num_silent += len(sndData)
            else:
                num_silent = 0
        else:
            if max(sndData) > speech_threshold:
                for idx in range(1, len(r), CHUNK_SIZE):
                    if np.max(r[-idx - CHUNK_SIZE:-idx]) < threshold:
                        onset = len(r) - idx - CHUNK_SIZE
                        onset_detected = True
                        break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = trim(r, threshold)
    # r = normalize(r)
    r = r[:maxSoundLength]
    r = np.require(np.tile(r, (2, 1)).T, requirements='C')
    # r = add_silence(r, 0.5)
    return sample_width, r


def recordSound_tofile(path, filename, threshold, min_record_duration, maxSoundLength):
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
            threshold, min_record_duration, maxSoundLength)

        data = pack('<' + ('h' * len(data[:, 0])), *data[:, 0])

        wf = wave.open(path + '/' + filename + '.wav', 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()
        return True
    except:
        return False


def recordSound_testing(threshold, RecordTime=[0,60], maxSoundLength=60 * RATE, feedback=False):
    """
    Record a word or words from the microphone and 
    return the data as an array of signed shorts.
    """
    RecordTime = RecordTime[0]*,RecordTime[1]*shared.setting['sample_rate']
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
                    input=True, output=True,
                    frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    speech_threshold = 4 * threshold
    num_sound = 0
    silent_limit = 1 * RATE

    onset = 0
    onset_detected = False

    r = array('h')
    while num_sound < maxSoundLength and len(r) < (minRecordTime + maxSoundLength) and num_silent < silent_limit:
        # little endian, signed short
        s = stream.read(CHUNK_SIZE)
        if feedback:
            stream.write(s, CHUNK_SIZE)

        sndData = array('h', s)
        if byteorder == 'big':
            sndData.byteswap()
        r.extend(sndData)

        # for e in shared.pg.event.get():
        #     if e.type == KEYDOWN:
        #         k = e.key
        #         if k == 27:
        #             shared.pg.quit()
        #         elif k == K_F12:
        #             suspend()

        if onset_detected:
            num_sound += len(sndData)

            if is_silent(sndData, threshold):
                num_silent += len(sndData)
            else:
                num_silent = 0
        else:
            if max(sndData) > speech_threshold:
                for idx in range(1, len(r), CHUNK_SIZE):
                    if np.max(r[-idx - CHUNK_SIZE:-idx]) < threshold:
                        onset = len(r) - idx - CHUNK_SIZE
                        onset_detected = True
                        break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = trim(r, threshold)
    # r = normalize(r)
    r = r[:maxSoundLength]
    r = np.require(np.tile(r, (2, 1)).T, requirements='C')
    # r = add_silence(r, 0.5)
    return sample_width, r
