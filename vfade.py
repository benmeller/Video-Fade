#!/usr/bin/env python3
"""
A quick and dirty script to add a fade in and fade out to a given clip.

To do:
- Argparse to select fade durations, filename and output name
- Clip start and end times (+ argparse)
- Multiple clips from single video (+ argparse)
"""

import sys
import moviepy
from moviepy.editor import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

def audio_fade(audioclip, fadetime=1, fadein=0, fadeout=0):
    if not fadein:
        fadein = fadetime
    if not fadeout:
        fadeout = fadetime

    audioclip = moviepy.audio.fx.all.audio_fadein(audioclip, fadein)
    audioclip = moviepy.audio.fx.all.audio_fadeout(audioclip, fadeout)
    return audioclip

def video_fade(videoclip, fadetime=2, fadein=0, fadeout=0):
    if not fadein:
        fadein = fadetime
    if not fadeout:
        fadeout = fadetime

    videoclip = moviepy.video.fx.all.fadein(videoclip, fadein)
    videoclip = moviepy.video.fx.all.fadeout(videoclip, fadeout)
    return videoclip


def main():
    if len(sys.argv) != 2:
        print("Usage: vfade.py VIDEO-FILENAME")
        return

    filename = sys.argv[1]

    try:
        clip = VideoFileClip(filename) 
        audio = AudioFileClip(filename)
    except OSError:
        print(f"File {filename} does not exist")
        return

    clip = video_fade(clip)
    clip.audio = audio_fade(audio, fadeout=3)

    clip.write_videofile(f"Faded-{filename}", audio_codec='aac')

if __name__=="__main__":
    main()