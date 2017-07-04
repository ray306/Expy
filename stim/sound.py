import struct
import io
from array import array
from expy import shared

np = shared.np

def mono2stereo(sound):
    output = b''
    if len(sound.shape) == 1:  # Mono
        interleaved = [int(sound[a]) for a in range(0,len(sound)) for _ in range(2) ]
        output = array('h', interleaved)
    # Stereo data is expressed in an interleaved format, left channel sample followed by the right channel sample
    else: # Stereo
        for a in range(0,len(sound)):
            output+=struct.pack('<hh', int(sound[a,0]), int(sound[a,1]))
    return output

def loadSound(path, offset=0, duration=None):
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

    Returns
    -------
    value: array
        The sound data
    '''
    sound, sr = shared.librosa.core.load(path, sr=shared.setting['sample_rate'], offset=offset, duration=duration)
    sound = (sound*32767).astype(np.int16)

    sound = mono2stereo(sound)
    return sound

def loadManySound(dirpath, filenames, ext='wav', offset=0.0, duration=None):
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

    Returns
    -------
    value: array
        The sound data
    '''
    paths = [(dirpath + '/' + file + '.' + ext) for file in filenames]
    sounds = [shared.librosa.core.load(p, sr=shared.setting['sample_rate'], offset=offset, duration=duration)[0]
                for p in paths]
    sound = np.concatenate(sounds)
    sound = (sound*32767).astype(np.int16)

    sound = mono2stereo(sound)
    return sound

def makeBeep(frequency, duration):
    '''
    Making a beep (pure-frequency) sound (stereo format).

    Parameters
    ----------
    frequency: number
        The frequency of sound
    duration: number
        The duration of sound

    Returns
    -------
    value: array
        The sound data
    '''
    bits = 16
    sr = shared.setting['sample_rate']

    total_sample = int(sr * duration)
    # setup our numpy array to handle 16 bit ints
    sound = np.zeros(total_sample, dtype=np.int16)
    max_sample = 2**(bits - 1) - 1

    # convert the frequences to sinusoid, and put them into the sound object
    for s in range(total_sample):
        t = float(s) / sr    # time in seconds
        sound[s] = int(round(max_sample * shared.math.sin(2 * shared.math.pi * frequency * t)))

    # # 淡入淡出5ms
    # segment = int(sr * 0.005)
    # start = sound[:][:segment] * np.array(list(range(segment))) // segment
    # start = np.array(start, int)
    # end = sound[:][-segment:] * \
    #     np.array(list(range(segment, 0, -1))) // segment
    # end = np.array(end, int)
    # sound[:][:segment] = start
    # sound[:][-segment:] = end

    sound = mono2stereo(sound)
    return sound

def makeSound(data):
    '''
    Read np.array object, then convert it into sound array (stereo format).

    Parameters
    ----------
    data: np.array
        The raw sound data array

    Returns
    -------
    value: array
        The sound data
    '''
    output = mono2stereo(data)
    return output

def playSound(sound, playing_track=None, blocking=True):
    '''
    Play a sound array

    Parameters
    ----------
    sound: array
        The sound data
    playing_track: int, str, or None(default)
        The name of current track
    blocking: True(default), or False
        Whether the experiment procedure would be blocked by the current function

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
        
        while 1:
            if blocking:
                shared.win.dispatch_events()

            data = output.read(chunk)
            if data == b'' or shared.states[playing_track] == False:
                break
            stream.write(data)

        shared.changeState(playing_track, False)

        stream.stop_stream()
        stream.close()

    if blocking:
        playSoundSub()
    else:
        td = shared.threading.Thread(target=playSoundSub)
        td.start()



