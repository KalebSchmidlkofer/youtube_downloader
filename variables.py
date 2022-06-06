
# Single-Line Variables

AUDIO_PATH='~/Music/'
VIDEO_PATH='~/Videos/'
errormessage='wow.. I gave you clear instructions'

# Multi-Line Variables
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

ydl_optsB = {'format': 'remux/best',
                'ignoreerrors': True,         
                'outtmpl': VIDEO_PATH + '/%(title)s.%(ext)s'}

