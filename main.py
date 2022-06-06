#!~/Coding/python/youtube_downloader/.youtube/bin/python
from typing import Generic
import yt_dlp
from sys import exit
import sys
import os
# Save paths for audio and video files
AUDIO_PATH='~/Music/'
VIDEO_PATH='~/Videos/'
errormessage='wow.. I gave you clear instructions'

# requesting input from terminal
try:
    print('ctrl + X to get back to this input')
    AudioVideo=input("Video or Audio: ").lower()


    # audio downloader
    if AudioVideo == 'audio':
        Download = input("Insert Video/playlist url: ")
        ydl_optsA = {
            'format': 'bestaudio/best',
            'writethumbnail': True,
            'outtmpl': AUDIO_PATH + '/%(title)s.%(ext)s',
            'ignoreerrors': True,
            'postprocessors':[
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': '192'},
            {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
            {'key': 'EmbedThumbnail','already_have_thumbnail': False,}
            ],
        }
        f = open("previousdownloads.txt", "a")
        f.write(f"{Download}\n")
        with yt_dlp.YoutubeDL(ydl_optsA) as ydl:
            ydl.download([Download])
            error_code = ydl.download(Download)
    else:
        print(f'{errormessage}')


    ### Video Downloader
    if AudioVideo == 'video':
        Download = input("Insert Video/playlist url: ")
        ydl_optsB = {'format': 'remux/best',
                'ignoreerrors': True,         
                'outtmpl': VIDEO_PATH + '/%(title)s.%(ext)s'}

        with yt_dlp.YoutubeDL(ydl_optsB) as ydl:
            ydl.download([Download])
except KeyboardInterrupt:
    print('\nKeyboardInterrupt')
    sys.exit(0)



if __name__ == '__main__':

    os.execl(sys.executable,*([sys.executable]+sys.argv))
