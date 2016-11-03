import math
import numpy as np
import scipy.io.wavfile
from expy import shared
from expy.response import *


def loadSound(path):
    '''
    Load a wav file, and return data array
    Or load a mp3/ogg file, and return None
    '''
    if path[-3:] in ['wav', 'WAV']:
        sr, sound = scipy.io.wavfile.read(path)
        if len(sound.shape) == 1:
            sound = np.require(np.tile(sound, (2, 1)).T, requirements='C')
        return sound
    else:
        try:
            shared.pg.mixer.music.load(path)
        except:
            raise ValueError('Unsupported sound format or file misssing')
        return None

def loadManySound(dirpath, filenames, ext='wav'):
    '''
    Read a list of music file, and return data array
    not support mp3/ogg files
    '''
    if ext in ['wav', 'WAV']:
        paths = [(dirpath + '/' + file + '.' + ext) for file in filenames]
        sounds = np.concatenate([scipy.io.wavfile.read(p)[1] for p in paths])
        sounds_reshaped = np.require(
            np.tile(sounds, (2, 1)).T, requirements='C')
        return sounds_reshaped
    else:
        raise ValueError('Unsupported sound format or file misssing')

def makeSound(freq, duration):
    '''
    Return a data array of certain sound freq
    '''
    sample_rate = 44100
    bits = 16
    total_sample = int(sample_rate * duration)
    # setup our numpy array to handle 16 bit ints, which is what we set our
    # mixer to expect with "bits" up above
    sound = np.zeros((total_sample, 2), dtype=np.int16)
    max_sample = 2**(bits - 1) - 1

    # convert the frequences to sinusoid, and put them into the sound object
    for s in range(total_sample):
        t = float(s) / sample_rate    # time in seconds
        sound[s] = int(round(max_sample * math.sin(2 * math.pi * freq * t)))

    # 淡入淡出背景音音轨5ms
    segment = int(44100 * 0.005)
    start = sound[:, 0][:segment] * np.array(list(range(segment))) // segment
    start = np.array(start, int)
    end = sound[:, 0][-segment:] * \
        np.array(list(range(segment, 0, -1))) // segment
    end = np.array(end, int)
    sound[:, 0][:segment] = start
    sound[:, 0][-segment:] = end
    sound[:, 1][:segment] = start
    sound[:, 1][-segment:] = end

    # pygame environment
    shared.pg.mixer.pre_init(sample_rate, -bits, 2)
    return shared.pg.sndarray.make_sound(sound)

def playSound(wav=None, block=True):
    '''
    Play a loaded file or a data array
    '''
    if wav is None:
        shared.pg.mixer.music.play()
    else:
        # indices = np.round( np.arange(0, len(wav), 16000/22050) )
        # indices = indices[indices < len(wav)].astype(int)
        # wav = wav[ indices.astype(int) ]
        shared.pg.sndarray.make_sound(wav).play()
    if block:
        while shared.pg.mixer.get_busy():
            waitForResponse({}, 100)
