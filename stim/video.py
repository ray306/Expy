from expy import shared
from expy.response import *
# import pyglet
# import time

# # Load a video file
# def loadVideo(path):
#     source = pyglet.media.load(path)
#     format = source.video_format
#     if not format:
#         raise ValueError('Unsupported file type')

#     return source

# # Play a loaded file
# def playVideo(source, pauseKey={},area=None):
#     format = source.video_format
#     width=format.width
#     height=format.height

#     start = time.time()
#     duration = source.duration
    
#     while 1:
#         ts = source.get_next_video_timestamp()
#         fm = source.get_next_video_frame()
#         if fm:
#             rawimage = fm.get_image_data()
#             pixels = rawimage.get_data(rawimage.format, rawimage.pitch)
            
#             video = shared.pg.image.frombuffer(pixels, (width, height), rawimage.format)

#             #Blit the image to the screen
#             shared.win.blit(video, (10, 10))

#             ts = source.get_next_video_timestamp()

#             waitT = start+ts-time.time()
#             if waitT>0 and ts<=duration:
#                 key,rt = waitForResponse({}, waitT*1000)
#             elif ts>duration:
#                 break
#             else:
#                 print(rawimage.width, rawimage.height)
#             shared.pg.display.flip()

# # Load a MPEG file
# def loadVideo(path):
#     video = shared.pg.movie.Movie(path)
#     return video

# # 
# def getVideoInfo(video):
#     return video.get_length(),video.get_size()

# # Play a loaded file
# def playVideo(video, pauseKey={},area=None):
#     video.set_display(shared.win,area)

#     video.play()
#     while video.get_busy():
#         key,time = waitForResponse({}, 100)
#         if key==pauseKey:
#             video.pause()
#             waitForResponse(pauseKey, 100)
#             video.pause()
#         