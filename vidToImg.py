import os
from moviepy import *

# https://www.youtube.com/watch?v=-foFaL2jeDE
def extractFrames(moviePath, imageDir, periodBetweenFrames = 0.1):
    clip = VideoFileClip(moviePath)
    times = [i * periodBetweenFrames for i in range(int(clip.duration / periodBetweenFrames))]
    if not os.path.exists(imageDir):
        os.makedirs(imageDir)
    i=0
    for t in times:
        newImgPath = os.path.join(imageDir, '{}.png'.format(i))
        i+=1
        clip.save_frame(newImgPath, t)

    nextPossibleFrame = os.path.join(imageDir, '{}.png'.format(i))
    if os.path.exists(nextPossibleFrame):
        os.remove(nextPossibleFrame)
