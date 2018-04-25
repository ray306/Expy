import struct
import io
import scipy
import resampy
from array import array
from expy import shared
from expy.io import sendTrigger

np = shared.np

def toStereoArray(sound):
    '''
    Force the sound data to stereo hex array

    Parameters
    ----------
    sound: array or np.array
        The original sound data

    Returns
    -------
    output: array
        The stereo hex array version of sound data
    '''
    output = b''
    if len(sound.shape) == 1:  # Mono
        interleaved = [int(sound[a]) for a in range(0,len(sound)) for _ in range(2) ]
        output = array('h', interleaved)
    # Stereo data is expressed in an interleaved format, left channel sample followed by the right channel sample
    else: # Stereo
        for a in range(0,len(sound)):
            output+=struct.pack('<hh', int(sound[a,0]), int(sound[a,1]))
    return output

def changeVolume(raw, scale):
    '''
    Change the volume

    Parameters
    ----------
    raw: np.array
        The raw sound data
    scale: num
        The change scale

    Returns
    -------
    value: np.array
        The changed sound data
    '''
    return raw * scale

def changePitch(raw, scale):
    '''
    Change the pitch

    Parameters
    ----------
    raw: np.array
        The raw sound data
    scale: num
        The change scale

    Returns
    -------
    value: np.array
        The changed sound data
    '''
    size = len(raw)

    # y_shift = scipy.signal.resample(raw, size/scale, axis=-1)

    sr = shared.setting['sample_rate']
    y_shift = resampy.resample(raw, sr, sr/scale, filter='kaiser_best', axis=-1)

    n = y_shift.shape[-1]

    if n > size:
        slices = [slice(None)] * y_shift.ndim
        slices[-1] = slice(0, size)
        return y_shift[slices]
    elif n < size:
        lengths = [(0, 0)] * y_shift.ndim
        lengths[-1] = (0, size - n)
        return np.pad(y_shift, lengths,mode='constant')
    else:
        return y_shift

def changeOnTracks(data, func, scale_list, stereo_array_format=True):
    '''
    Change the sound on each track

    Parameters
    ----------
    data: np.array or array
        The raw sound data
    func: method name
        The action of change 
    scale: list
        The change scale of each track
    stereo_array_format: True(default), or False
        Whether return a stereo array

    Returns
    -------
    output: array
        The sound data
    '''
    if type(data) is array:
        data = np.array(data).reshape((len(data)//2,2))

    if len(scale_list) == 2:
        for ind,r in enumerate(scale_list):
            data[:,ind] = func(data[:,ind], r)
    else:
        raise Exception('Size of scale_list doesn\'t match the track count')

    if stereo_array_format:
        output = toStereoArray(data)
    return output

def loadSound(path, offset=0, duration=None, stereo_array_format=True):
    '''
    Load a sound file, and return data array (stereo format)

    Parameters
    ----------
    path: str
        The file path of target sound
    offset: number (default:0)
        The onset of target sound
    duration: number, or None(default)
        The duration of target sound
    stereo_array_format: True(default), or False
        Whether return a stereo array

    Returns
    -------
    output: array
        The sound data
    '''
    sound, sr = shared.librosa.core.load(path, sr=shared.setting['sample_rate'], offset=offset, duration=duration)
    output = (sound*32767).astype(np.int16)

    if stereo_array_format:
        output = toStereoArray(output)
    return output

def loadManySound(dirpath, filenames, ext='wav', offset=0.0, duration=None, stereo_array_format=True):
    '''
    Read a list of music file, then concatnate them and return data array (stereo format).

    Parameters
    ----------
    dirpath: str
        The directory path of target sounds
    filenames: str
        The filenames of target sounds (without filename extension)
    ext: str
        The filename extension of target sounds
    offset: number (default:0)
        The onset of target sounds
    duration: number, or None(default)
        The duration of target sounds
    stereo_array_format: True(default), or False
        Whether return a stereo array

    Returns
    -------
    output: array
        The sound data
    '''
    paths = [(dirpath + '/' + file + '.' + ext) for file in filenames]
    sounds = [shared.librosa.core.load(p, sr=shared.setting['sample_rate'], offset=offset, duration=duration)[0]
                for p in paths]
    sound = np.concatenate(sounds)
    output = (sound*32767).astype(np.int16)

    if stereo_array_format:
        output = toStereoArray(output)
    return output

def makeBeep(frequency, duration, stereo_array_format=True):
    '''
    Making a beep (pure-frequency) sound (stereo format).

    Parameters
    ----------
    frequency: number
        The frequency of sound
    duration: number
        The duration of sound
    stereo_array_format: True(default), or False
        Whether return a stereo array

    Returns
    -------
    output: array
        The sound data
    '''
    bits = 16
    sr = shared.setting['sample_rate']

    total_sample = int(sr * duration)
    # setup our numpy array to handle 16 bit ints
    output = np.zeros(total_sample, dtype=np.int16)
    max_sample = 2**(bits - 1) - 1

    # convert the frequences to sinusoid, and put them into the sound object
    for s in range(total_sample):
        t = float(s) / sr    # time in seconds
        output[s] = int(round(max_sample * shared.math.sin(2 * shared.math.pi * frequency * t)))

    # # 淡入淡出5ms
    # segment = int(sr * 0.005)
    # start = sound[:][:segment] * np.array(list(range(segment))) // segment
    # start = np.array(start, int)
    # end = sound[:][-segment:] * \
    #     np.array(list(range(segment, 0, -1))) // segment
    # end = np.array(end, int)
    # sound[:][:segment] = start
    # sound[:][-segment:] = end

    if stereo_array_format:
        output = toStereoArray(output)
    return output

def makeNoise(duration, stereo_array_format=True):
    '''
    Making a white noise (stereo format).

    Parameters
    ----------
    duration: number
        The duration of sound
    stereo_array_format: True(default), or False
        Whether return a stereo array

    Returns
    -------
    output: array
        The sound data
    '''
    bits = 16
    sr = shared.setting['sample_rate']

    sound = np.random.normal(0, 1, size=int(sr * duration))
    output = (sound*32767).astype(np.int16)

    if stereo_array_format:
        output = toStereoArray(output)
    return output

def makeSound(data):
    '''
    Read np.array object, then convert it into sound array (stereo format).

    Parameters
    ----------
    data: np.array
        The raw sound data array

    Returns
    -------
    output: array
        The sound data
    '''
    output = toStereoArray(data)
    return output


def playSound(sound, busy=True, playing_track=None, timeit=False, trigger=None, triggerbox=False):
    '''
    Play a sound array, and the experiment procedure will be blocked by this function

    Parameters
    ----------
    sound: array
        The sound data
    busy: True(default), or False
        Whether the experiment procedure will be blocked by the this function
    playing_track: int, str, or None(default)
        The name of current track
    (beta testing) timeit: True, False (default)
    (beta testing) trigger: (content, mode)

    Returns
    -------
    None
    '''
    if busy:
        playBusySound(sound, timeit, trigger, triggerbox)
    else:
        playFreeSound(sound, playing_track, timeit, trigger)


def playBusySound(sound, timeit=False, trigger=None, triggerbox=False):
    '''
    Play a sound array, and the experiment procedure will be blocked by this function

    Parameters
    ----------
    sound: array
        The sound data
    (beta testing) timeit: True, False (default)
    (beta testing) trigger: (content, mode)

    Returns
    -------
    None
    '''
    output = io.BytesIO(sound)

    chunk = 1024
    stream = shared.pa.open(format=shared.pyaudio.paInt16, channels=2, rate=shared.setting['sample_rate'],
                    output=True)

    
    first = True

    

    while 1:
        shared.win.dispatch_events()

        data = output.read(chunk)
        if data == b'':
            break

        

        if first:
            first = False
            if timeit and shared.start_tp is None:
                if triggerbox:
                    shared.check_port = True
                else:
                    shared.start_tp = shared.time.time()
            if trigger:
                sendTrigger(trigger[0], mode=trigger[1])

        stream.write(data)

    stream.stop_stream()
    stream.close()

def playFreeSound(sound, playing_track=None, timeit=False, trigger=None):
    '''
    Play a sound array, and the experiment procedure won't be blocked by this function

    Parameters
    ----------
    sound: array
        The sound data
    playing_track: int, str, or None(default)
        The name of current track
    (beta testing) timeit: True, False (default)
    (beta testing) trigger: (content, mode)

    Returns
    -------
    None
    '''
    if type(playing_track)!=str:
        playing_track=np.random.randint(99999)
        
    shared.changeState(playing_track, True)

    def playSoundSub():
        output = io.BytesIO(sound)

        chunk = 1024
        stream = shared.pa.open(format=shared.pyaudio.paInt16, channels=2, rate=shared.setting['sample_rate'],
                        output=True)

        first = True

        while 1:
            data = output.read(chunk)
            if data == b'' or shared.states[playing_track] == False:
                break

            if first:
                first = False
                if timeit and shared.start_tp is None:
                    now = shared.time.time()
                    shared.start_tp = now
                if trigger:
                    sendTrigger(trigger[0], mode=trigger[1])

            stream.write(data)

        shared.changeState(playing_track, False)

        stream.stop_stream()
        stream.close()

    td = shared.threading.Thread(target=playSoundSub)
    td.start()

import pyglet.window.key as key_
def playAlterableSound(sound, effect=changeVolume, key_up=key_.RIGHT, key_down=key_.LEFT, key_confirm=key_.ENTER, timeit=False, trigger=None):
    '''
    Play a sound array, and the sound can be modified while playingr 

    Parameters
    ----------
    sound: array
        The sound data
    effect: function (default: changeVolume)
        The function of how to change the sound by a given index.
    key_up: keyname (default: key_.RIGHT)
        The key indicating up of the index.
    key_down: keyname (default: key_.LEFT)
        The key indicating down of the index.
    key_confirm: keyname (default: key_.ENTER)
        The key indicating the end of change detection.
    (beta testing) timeit: True, False (default)
    (beta testing) trigger: (content, mode)

    Returns
    -------
    None
    '''
    output = io.BytesIO(sound)

    chunk = 1024
    if effect==changePitch: chunk = 1024*8

    stream = shared.pa.open(format=shared.pyaudio.paInt16, channels=2, rate=shared.setting['sample_rate'],
                    output=True)
    if trigger:
        sendTrigger(trigger[0], mode=trigger[1])
    changed_index = 1 # index the key-caused change

    while 1:
        shared.win.dispatch_events()

        data = output.read(chunk)

        if data == b'':
            break

        raw = np.fromstring(data, dtype=np.int16).astype(np.float32)

        for e in shared.events:
            if e['type']=='key_press':
                shared.pressing = e['key']

        if shared.figure_released:
            shared.pressing = None

        if shared.pressing==key_up:
            if effect==changeVolume and changed_index>1:
                changed_index = 1
            else:
                changed_index *= 1.01
        elif shared.pressing==key_down:
            changed_index /= 1.01
            
        elif shared.pressing==key_confirm:
            break

        raw = effect(raw.astype(np.float32), changed_index)
        
        raw = raw.astype(np.int16)
        data = raw.tobytes()

        stream.write(data)

    shared.events = []
    stream.stop_stream()
    stream.close()

    return changed_index
