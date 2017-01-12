''' https://groups.google.com/forum/#!topic/pyglet-users/hKj-x_LCLx8 '''

import struct
import ctypes

from expy import shared
np = shared.np
al = shared.al
alc = shared.alc

#using PyAL
##from openal import al, alc



class buffer_sound(object):
    def __init__(self, data, samplerate=44100):
##        formatmap = {
##            (1, 8) : al.AL_FORMAT_MONO8,
##            (2, 8) : al.AL_FORMAT_STEREO8,
##            (1, 16): al.AL_FORMAT_MONO16,
##            (2, 16) : al.AL_FORMAT_STEREO16,
##        }
##        alformat = formatmap[(channels, bitrate)]
        self.alformat = al.AL_FORMAT_STEREO16
        self.buf = al.ALuint(0)

        al.alGenBuffers(1, self.buf)
        al.alBufferData(self.buf, self.alformat, data, len(data)*2, samplerate)

    def delete(self):
        al.alDeleteBuffers(1, self.buf)


#load sound buffers into an openal source player to play them
class Player(object):
#load default settings
    def __init__(self):
    #load source player
        self.source = al.ALuint(0)
        al.alGenSources(1, self.source)
    #disable rolloff factor by default
        al.alSourcef(self.source, al.AL_ROLLOFF_FACTOR, 0)
    #disable source relative by default
        al.alSourcei(self.source, al.AL_SOURCE_RELATIVE,0)
    #capture player state buffer
        self.state = al.ALint(0)
    #set internal variable tracking
        self._volume = 1.0
        self._pitch = 1.0
        self._position = [0,0,0]
        self._rolloff = 1.0
        self._loop = False
        self.queue = []


#set rolloff factor, determines volume based on distance from listener
    def _set_rolloff(self,value):
        self._rolloff = value
        al.alSourcef(self.source, al.AL_ROLLOFF_FACTOR, value)

    def _get_rolloff(self):
        return self._rolloff


#set whether looping or not - true/false 1/0
    def _set_loop(self,lo):
        self._loop = lo
        al.alSourcei(self.source, al.AL_LOOPING, lo)

    def _get_loop(self):
        return self._loop
      

#set player position
    def _set_position(self,pos):
        self._position = pos
        x,y,z = map(int, pos)
        al.alSource3f(self.source, al.AL_POSITION, x, y, z)

    def _get_position(self):
        return self._position
        

#set pitch - 1.5-0.5 float range only
    def _set_pitch(self,pit):
        self._pitch = pit
        al.alSourcef(self.source, al.AL_PITCH, pit)

    def _get_pitch(self):
        return self._pitch

#set volume - 1.0 float range only
    def _set_volume(self,vol):
        self._volume = vol
        al.alSourcef(self.source, al.AL_GAIN, vol)

    def _get_volume(self):
        return self._volume

#queue a sound buffer
    def add(self,sound):
        al.alSourceQueueBuffers(self.source, 1, sound.buf) #self.buf
        self.queue.append(sound)

#remove a sound from the queue (detach & unqueue to properly remove)
    def remove(self):
        if len(self.queue) > 0:
            al.alSourceUnqueueBuffers(self.source, 1, self.queue[0].buf) #self.buf
            al.alSourcei(self.source, al.AL_BUFFER, 0)
            self.queue.pop(0)

#play sound source
    def play(self):
        al.alSourcePlay(self.source)

#get current playing state
    def playing(self):
        al.alGetSourcei(self.source, al.AL_SOURCE_STATE, self.state)
        if self.state.value == al.AL_PLAYING:
            return True
        else:
            return False

#stop playing sound
    def stop(self):
        al.alSourceStop(self.source)

#rewind player
    def rewind(self):
        al.alSourceRewind(self.source)

#pause player
    def pause(self):
        al.alSourcePause(self.source)

#delete sound source
    def delete(self):
        al.alDeleteSources(1, self.source)

#Go straight to a set point in the sound file
    def _set_seek(self,offset):#float 0.0-1.0
        al.alSourcei(self.source,al.AL_BYTE_OFFSET,int(self.queue[0].length * offset))

#returns current buffer length position (IE: 21000), so divide by the buffers self.length
    def _get_seek(self):#returns float 0.0-1.0
        al.alGetSourcei(self.source, al.AL_BYTE_OFFSET, self.state)
        return float(self.state.value)/float(self.queue[0].length)

    rolloff = property(_get_rolloff, _set_rolloff,doc="""get/set rolloff factor""")
    volume = property(_get_volume, _set_volume,doc="""get/set volume""")
    pitch = property(_get_pitch, _set_pitch, doc="""get/set pitch""")
    loop = property(_get_loop, _set_loop, doc="""get/set loop state""")
    position = property(_get_position, _set_position,doc="""get/set position""")
    seek = property(_get_seek, _set_seek, doc="""get/set the current play position""")


# #load a listener to load and play sounds.
# class Listener(object):
#     def __init__(self):
#     #load device/context/listener
#         self.device = alc.alcOpenDevice(None)
#         self.context = alc.alcCreateContext(self.device, None)
#         alc.alcMakeContextCurrent(self.context)

# #set player position
#     def _set_position(self,pos):
#         self._position = pos
#         x,y,z = map(int, pos)
#         al.alListener3f(al.AL_POSITION, x, y, z)

#     def _get_position(self):
#         return self._position

# #delete current listener
#     def delete(self):
#         alc.alcDestroyContext(self.context)
#         alc.alcCloseDevice(self.device)

#     position = property(_get_position, _set_position,doc="""get/set position""")

def mono2stereo(sound):
    output = (ctypes.c_short * (len(sound) * 2))()
    if len(sound.shape) == 1:  # Mono
        for a in range(0,len(sound)):
            output[2*a] = int(sound[a])
            output[2*a+1] = int(sound[a])
    # Stereo data is expressed in an interleaved format, left channel sample followed by the right channel sample
    else: # Stereo
        for a in range(0,len(sound)):
            output[2*a] = int(sound[a,0])
            output[2*a+1] = int(sound[a,1])
    return output

def loadSound(path, offset=0.0, duration=None):
    sound, sr = shared.librosa.core.load(path, sr=shared.setting['sample_rate'], offset=offset, duration=duration)
    sound = (sound*32767).astype(np.int16)

    output = mono2stereo(sound)
    return output

def loadManySound(dirpath, filenames, ext='wav', offset=0.0, duration=None):
    paths = [(dirpath + '/' + file + '.' + ext) for file in filenames]
    sounds = [shared.librosa.core.load(p, sr=shared.setting['sample_rate'], offset=offset, duration=duration)[0]
                for p in paths]
    sound = np.concatenate(sounds)
    sound = (sound*32767).astype(np.int16)

    output = mono2stereo(sound)
    return output

def makeBeep(frequency, duration):
    bits = 16
    sr = shared.setting['sample_rate']

    total_sample = int(sr * duration)
    # setup our numpy array to handle 16 bit ints, which is what we set our
    # mixer to expect with "bits" up above
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

    output = mono2stereo(sound)
    return output

def makeSound(data):
    output = mono2stereo(data)
    return output

def playSound(sound, blocking=True):
    sbuffer = buffer_sound(sound)

    player = Player()
    player.add(sbuffer)
    player.play()

    while player.playing():
        pass

    player.remove()
    player.delete()
    # sbuffer.delete()


# listener = Listener()
# ...Load and play...
# listener.delete()


