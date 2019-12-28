from youtube_dl import YoutubeDL
import requests
from configparser import ConfigParser

if __name__ == "__main__":
    Info = ConfigParser()
    Info.read("Data/info.ini")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "SinglePlaylist/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {
                'key': 'FFmpegMetadata'
            },
        ]
    }
    
    url = input("Playlist / Video from playlist URL: ")
    if requests.get(f"{Info['yt']['checkLink']}{url}").status_code == 200:
        if ("/watch?v=" in url and "&list=" in url) or "playlist?list=" in url:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
    print("Playlist downloaded, check SinglePlaylist/.")