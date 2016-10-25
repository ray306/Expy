import pygame as pg

from expy import shared

# Load a MPEG file
def loadVideo(path):
    video = shared.pg.movie.Movie(path)
    return video

# 
def getVideoInfo(video):
    return video.get_length(),video.get_size()

# Play a loaded file
def playVideo(video, pauseKey={}, area=None):
    video.set_display(shared.win,area)

    video.play()
    while video.get_busy():
        key,time = waitForResponse({}, 100)
        if key==pauseKey:
            video.pause()
            waitForEvent(pauseKey, 100)
            video.pause()
        