import yt_dlp, sys, os
from sys import exit
from variables import *
from ytmusicapi import YTMusic
ytmusic = YTMusic()
YTMusic.setup(filepath="headers_auth.json")


try:
    while True:
        AudioVideo=input('Video or Audio or Both: ').lower()
        ### audio downloader
        if AudioVideo == 'audio':
            Download = input('Insert Video/playlist url: ')
            f = open('previousdownloadsAudio.txt', 'a')
            f.write(f'{Download}\n')
            f.close()
            with yt_dlp.YoutubeDL(ydl_optsA) as ydl:
                ydl.download([Download])
        ### Video Downloader
        elif AudioVideo == 'video':
            Download = input('Insert Video/playlist url: ')
            f = open('previousdownloadsVideo.txt', 'a')
            f.write(f'{Download}\n')
            f.close()
            with yt_dlp.YoutubeDL(ydl_optsB) as ydl:
                ydl.download([Download])
        ### Video and Audio Downloader
        elif AudioVideo == 'both':
            print('Here what your gonna do is download')
            print('both Audio and Video files at the same TIME!')
            Download = input('Instert Video/Playlist url: ')
            f = open('previousdownloads.txt', 'a')
            f.write(f'{Download}\n')
            f.close()
            with yt_dlp.YoutubeDL(ydl_optsA) as ydl:
                ydl.download([Download])
            with yt_dlp.YoutubeDL(ydl_optsB) as ydl:
                ydl.download([Download])
        else:
            print(f'{errormessage}')
except KeyboardInterrupt:
    print('\n')
    sys.exit(0)

if __name__ == '__main__':
    os.execl(sys.executable,*([sys.executable]+sys.argv))
