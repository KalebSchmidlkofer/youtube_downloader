#!/home/kaleb/Coding/python/youtube_downloader/.youtube/bin/python3.10
import yt_dlp
from sys import exit
import sys
import os
from variables import ydl_optsA, ydl_optsB, errormessage
            
            
# requesting input from terminal

try:
    while True:
        AudioVideo=input("Video or Audio: ").lower()
        # audio downloader
        if AudioVideo == 'audio':
            Download = input("Insert Video/playlist url: ")
            f = open('previousdownloads.txt', 'a')
            f.write(f'{Download}\n')
            f.close()            
            with yt_dlp.YoutubeDL(ydl_optsA) as ydl:
                ydl.download([Download])

        
        ### Video Downloader
        elif AudioVideo == 'video':
            Download = input("Insert Video/playlist url: ")
            f = open('previousdownloads.txt', 'a')
            f.write(f'{Download}\n')
            f.close()
            with yt_dlp.YoutubeDL(ydl_optsB) as ydl:
                ydl.download([Download])

        else:
            print(f'{errormessage}')
except KeyboardInterrupt:
    sys.exit(0)


if __name__ == '__main__':
    os.execl(sys.executable,*([sys.executable]+sys.argv))
