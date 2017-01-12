import os

from expy import shared

# http://stackoverflow.com/questions/892199/detect-record-audio-in-python
from sys import byteorder
from array import array
from struct import pack

np = shared.np

def addSilence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in range(
        int(seconds * shared.setting['sample_rate']))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds * shared.setting['sample_rate']))])
    return r

# def trim(snd_data, threshold, side='both'):
#     "Trim the blank spots at the start and end"
#     def _trim(snd_data):
#         snd_data0 = np.array([int(abs(i) > threshold*3) for i in snd_data])

#         snd_started = False
#         r = array('h')

#         lasting = 4000
#         for i in range(len(snd_data)):
#             if not snd_started and snd_data0[i - lasting:i].sum() < (lasting / 20) and snd_data0[i:i + lasting].sum() > (lasting / 3):
#                 snd_started = True
#                 r.append(snd_data[i])

#             elif snd_started:
#                 r.append(snd_data[i])
#         return r

#     if side == 'left':
#         # Trim to the left
#         snd_data = _trim(snd_data)
#     elif side == 'right':
#         # Trim to the right
#         snd_data.reverse()
#         snd_data = _trim(snd_data)
#         snd_data.reverse()
#     elif side == 'both':
#         # Trim to the left
#         snd_data = _trim(snd_data)
#         # Trim to the right
#         snd_data.reverse()
#         snd_data = _trim(snd_data)
#         snd_data.reverse()
#     elif side == 'none':
#         pass

#     return snd_data

def trim(snd_data, onset_frame, end_frame, side='both'):
    if side == 'left':
        snd_data = snd_data[onset_frame:-1]
    elif side == 'right':
        snd_data = snd_data[:end_frame]
    elif side == 'both':
        snd_data = snd_data[onset_frame:end_frame]
    elif side == 'none':
        pass

    return snd_data

def measure(curFrame):
    #过零率
    tmp1 = curFrame[:-1]
    tmp2 = curFrame[1:]
    sings = (tmp1*tmp2<=0)
    diffs = (tmp1-tmp2)>0.02
    zcr = np.sum(sings*diffs)
    #短时能量
    amp = np.sum(np.abs(curFrame))
    return zcr, amp

def environmentNoise(sampling_time, weights=(1.1,3,5,1.1,2,3), chunk=1024):
    """
    Record the sound in a certain duration as the environment noise, and calcuate its amplitude and zero-crossing rate.

    Parameters
    ----------
    sampling_time: number
        The duration of noise sampling
    weights: tuple (default: (1.1,3,5,1.1,2,3))
        (The weight of noise threshold of zero-crossing rate,
        The weight of low threshold of zero-crossing rate,
        The weight of high threshold of zero-crossing rate,
        The weight of noise threshold of sound amplitude,
        The weight of low threshold of sound amplitude,
        The weight of high threshold of sound amplitude)
    chunk: int (default: 1024)
        The frame size

    Returns
    -------
    zcr0: number
        The noise threshold of zero-crossing rate
    zcr1: number
        The low threshold of zero-crossing rate
    zcr2: number
        The high threshold of zero-crossing rate 
    amp0: number
        The noise threshold of sound amplitude
    amp1: number
        The low threshold of sound amplitude
    amp2: number
        The high threshold of sound amplitude
    """
    def calc_threshold():
        stream = shared.pa.open(format=shared.pyaudio.paInt16, channels=1, rate=shared.setting['sample_rate'],
                        input=True,
                        frames_per_buffer=chunk)

        r = array('h')
        noise = []
        zcrs = []
        amps = []

        for i in range(int(sampling_time * shared.setting['sample_rate'] // chunk)):
            # little endian, signed short
            snd_data = array('h', stream.read(chunk))
            if byteorder == 'big':
                snd_data.byteswap()
            r.extend(snd_data)

            zcr, amp = measure(np.array(snd_data))
            zcrs.append(zcr)
            amps.append(amp)

        stream.stop_stream()
        stream.close()

        return np.mean(zcrs),np.mean(amps)

    zcr_noise, amp_noise = calc_threshold()
    zcr0 = zcr_noise*weights[0] # The noise threshold of zero-crossing rate
    zcr1 = zcr_noise*weights[1] # The low threshold of zero-crossing rate
    zcr2 = zcr_noise*weights[2] # The high threshold of zero-crossing rate 
    amp0 = amp_noise*weights[3] # The noise threshold of sound amplitude
    amp1 = amp_noise*weights[4] # The low threshold of sound amplitude
    amp2 = amp_noise*weights[5] # The high threshold of sound amplitude
    
    print("environment's noise level: (zcr %.3f, amp %.3f)" %(zcr_noise, amp_noise))
    return zcr0, zcr1, zcr2, amp0, amp1, amp2

'''https://github.com/halleytl/pyvad/blob/master/vad.py'''
def recordSound(vad_levels, rec_length_min=0, rec_length_max=None, sound_length_max=None,
    trim_side='both', feedback=False, chunk=1024, playing_track=None, blocking=True, path=''):
    """
    Record sound from the microphone.

    Parameters
    ----------
    vad_levels: tuple
        (The noise threshold of zero-crossing rate,
        The low threshold of zero-crossing rate,
        The high threshold of zero-crossing rate,
        The noise threshold of sound amplitude,
        The low threshold of sound amplitude,
        The high threshold of sound amplitude)
    rec_length_min: number(ms) (default: 0)
        The millisecond count of minimal recording time
    rec_length_max: number(ms), or None (default)
        The millisecond count of maximal recording time
    sound_length_max: number(ms), or None (default)
        The millisecond count of maximal sound length
    trim_side: str (default: 'both')
        The trimming way of recorded sound
        Options: 'both', 'left', 'right', 'none'
    feedback: True, or False(default)
        Whether the sound feedbacks while recording
    chunk: int (default: 1024)
        The frame size
    playing_track: int, str, or None(default)
        The name of current track
    blocking: True(default), or False
        Whether the recording track blocks the experiment
    path: str (default: '')
        The file path of target sound. If the path is undefined(''), the sound won't be recorded.
    Returns
    -------
    If recorded:
        rec_data: np.array
            The recorded sound array in stereo
    If recorded nothing:
        []
    If not blocking:
        None
    """
    if type(playing_track)!=str:
        playing_track=np.random.randint(99999)

    shared.changeState(playing_track, True)

    sr = shared.setting['sample_rate']
    
    rec_length_min = rec_length_min * (sr/1000)
    if rec_length_max:
        rec_length_max *=  (sr/1000)
    if sound_length_max:
        sound_length_max *= (sr/1000)

    zcr0, zcr1, zcr2, amp0, amp1, amp2 = vad_levels
    
    maxsilence = 1.5 * sr // chunk #允许最大静音长度
    minlen = 0.2 * sr // chunk  #语音的最短长度, 语音长度太短认为是噪声

    def recordSoundSub():
        #初始状态为静音
        count = 0
        silence = 0
        sound_status = 0
        speech_status = 0

        onset_detected = False
        onset_frame = 0
        end_frame = -1

        status_record = []
        status_record2 = []

        stream = shared.pa.open(format=shared.pyaudio.paInt16, channels=1, rate=sr,
                        input=True, output=True)

        rec_data = array('h')

        while True:
            if blocking:
                shared.win.dispatch_events()
            # When to stop recording
            if (rec_length_max and len(rec_data) > rec_length_max) or \
                (sound_length_max and (len(rec_data)-onset_frame) > sound_length_max) or \
                (not onset_detected and len(rec_data) > rec_length_min) or \
                shared.states[playing_track] == False:
                break

            # little endian, signed short
            s = stream.read(chunk)

            if feedback:
                stream.write(s, chunk)

            snd_data = array('h', s)
            if byteorder == 'big':
                snd_data.byteswap()
            rec_data.extend(snd_data)

            data = np.array(snd_data)
            zcr, amp = measure(data)

            status = 0
            # 0= 静音， 1= 可能开始
            if speech_status in [0, 1]: 
                # 确定进入语音段
                if amp > amp2 or zcr > zcr2:     
                    sound_status = 2
                    speech_status = 2
                    silence = 0
                    count += 1

                    onset_detected = True
                    for idx in range(len(status_record)-1, 0, -1):
                        if idx>0 and status_record[idx-1]==0:
                            onset_frame = (idx-1)*chunk
                            break

                #可能处于语音段 
                elif (amp > amp0 and zcr > zcr0) or (amp > amp1 or zcr > zcr1): 
                    sound_status = 1
                    count += 1
                #静音状态
                else:  
                    sound_status = 0
                    count = 0
            # 2 = 语音段
            elif speech_status == 2:              
                # 保持在语音段
                if (amp > amp0 and zcr > zcr0) or (amp > amp1 or zcr > zcr1):
                    count += 1
                    sound_status = 2
                #语音将结束
                else:
                    #静音还不够长，尚未结束
                    silence += 1
                    if silence < maxsilence:
                        count += 1
                        sound_status = 2
                    #语音长度太短认为是噪声
                    elif count < minlen:
                        sound_status = 0
                        silence = 0
                        count = 0
                    #语音结束
                    else:
                        end_frame = (len(status_record) - silence)*chunk
                        sound_status = 3

            status_record.append(sound_status)
            # status_record2.append('%.1f, %.1f' %(amp/amp0,zcr/zcr0))
            if sound_status == 3:
                    break

        shared.changeState(playing_track, False)
        # print(status_record)
        # print(onset_frame,status_record,status_record2)

        rec_data = trim(rec_data, onset_frame, end_frame, trim_side)
        # rec_data = rec_data[onset_frame:end_frame]
        
        if sound_length_max: 
            rec_data = rec_data[:int(sound_length_max)]
        # rec_data = trim(rec_data, noise_level[1]//chunk, side=trim_side)

        stream.stop_stream()
        stream.close()

        if len(rec_data)==0:
            print('Recorded nothing')
            return []

        # rec_data = addSilence(rec_data, 0.5)
        rec_data = np.require(np.tile(rec_data, (2, 1)).T, requirements='C')
        # rec_data = np.require(np.array([rec_data[::2], rec_data[1::2]]).T, requirements='C')
        
        if path!='':
            shared.librosa.output.write_wav(path, rec_data, sr, norm=False)

        return rec_data

    if blocking:
        rec_data = recordSoundSub()
        return rec_data
    else:
        td = shared.threading.Thread(target=recordSoundSub)
        td.start()