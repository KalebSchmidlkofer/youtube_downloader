#!/bin/bash
import code
import yt_dlp
from sys import exit
import sys
import os
#Save paths for audio and video files
AUDIO_PATH = '~/Music/download'
VIDEO_PATH = '~/Videos/download/pythonhelp'
#requesting input from terminal
AudioVideo=input("Video or Audio:")
#audio downooader
if AudioVideo == "Audio":
    Download = input("Insert Video/playlist url: ")
    ydl_optsA = {'format': 'bestaudio/best',
            'outtmpl': AUDIO_PATH + '/%(title)s.%(ext)s',
            'quite': '--quite'}
    with yt_dlp.YoutubeDL(ydl_optsA) as ydl:
        ydl.download([Download])
 ###Video Downloader
if AudioVideo == "Video":
    Download = input("Insert Video/playlist url: ")
    ydl_optsB = {'format': 'remux-video/best',
            'outtmpl': VIDEO_PATH + '/%(title)s.%(ext)s'}  
    with yt_dlp.YoutubeDL(ydl_optsB) as ydl:
        ydl.download([Download])  



if __name__ == '__main__':

    os.execl(sys.executable,*([sys.executable]+sys.argv))