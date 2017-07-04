from expy import shared
from expy.response import *
from .draw import getPos

def loadVideo(path):
    '''
    Load a video array

    Parameters
    ----------
    path: str
        The file path of target video

    Returns
    -------
    player: pyglet.media.Player
        playVideo() could use it 
    '''
    source = shared.pyglet.media.load(path)

    format = source.video_format
    if not format:
        raise ValueError('Unsupported file type')

    player = shared.pyglet.media.Player()
    player.queue(source)

    return player

def playVideo(video, pauseKey=key_.SPACE, x=0.0, y=0.0, anchor_x='center', anchor_y='center'):
    '''
    Play a loaded video

    Parameters
    ----------
    video: pyglet.media.Player
        The player of target video
    pauseKey: (default: key_.SPACE)
        The name for pausekey
    x: int, or float (default:0.0)
        The x coordinate of text. If x is int, the coordinate would be pixel number to the left margin of screen; If x is float (-1~1), the coordinate would be percentage of half screen to the screen center.
    y: int, or float (default:0.0)
        The y coordinate of text. If y is int, the coordinate would be pixel number to the upper margin of screen; If y is float (-1~1), the coordinate would be percentage of half screen to the screen center.
    anchor_x: str (default:'center')
        The position benchmark on this object to the given x.
        Options: 'center', 'left', or 'right'.
    anchor_y: str (default:'center')
        The position benchmark on this object to the given y.
        Options: 'center', 'top', or 'bottom'.

    Returns
    -------
    None
    '''
    source = video.source
    duration = source.duration
    pos = getPos(x, y, source.video_format.width, 
        source.video_format.height, anchor_x=anchor_x,anchor_y=anchor_x)

    @shared.win.event
    def on_draw():
        shared.win.clear()
        if source and source.video_format:
            video.get_texture().blit(pos[0],pos[1])

    video.play()

    startT = shared.time.time()
    while shared.time.time() - startT < duration:
        shared.pyglet.clock.tick()
        shared.win.dispatch_events()

        if len(shared.events)>0 and shared.events[0]['type']=='key_press' and shared.events[0]['key'] == pauseKey:
            shared.events = []
            video.pause()
            key,rt = waitForResponse([pauseKey])
            video.play()
            startT += rt

        shared.win.dispatch_event('on_draw')
        shared.win.flip()

    shared.win.clear()
