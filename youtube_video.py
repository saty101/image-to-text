import youtube_dl

# Replace the required link with whichever link you want to annotate
link = "https://www.youtube.com/watch?v=OZ--BAModfw"

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(link, download=False)
    video_title = info_dict.get('title', None)

# Since the above link is a news video, we'll name it as news.mp4
path = f'./news.mp4'

ydl_opts.update({'outtmpl':path})

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])