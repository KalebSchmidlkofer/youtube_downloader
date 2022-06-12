
# Single-Line Variables

AUDIO_PATH='~/Music/'
VIDEO_PATH='~/Videos/'
errormessage='wow.. I gave you clear instructions'


# Multi-Line Variables

ydl_optsA = {
            'format': 'bestaudio/best',
            'writethumbnail': True,
            'writesubtitles': True,
            'subtitle': '--write-sub --sub-lang en',
            'outtmpl': AUDIO_PATH + '/%(title)s.%(ext)s',
            'ignoreerrors': True,
            'postprocessors':[
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': '320'},
            {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
            {'key': 'EmbedThumbnail','already_have_thumbnail': False,}
            ],
        }            

ydl_optsB = {'format': 'remux/best',
            'ignoreerrors': True,
            'writesubtitles': True,
            'subtitle': '--write-sub --sub-lang en',         
            'outtmpl': VIDEO_PATH + '/%(title)s.%(ext)s'}
