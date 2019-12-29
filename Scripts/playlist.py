from youtube_dl import YoutubeDL
import requests
from configparser import ConfigParser
from checkFolders import checkSinglePlaylist

if __name__ == "__main__":
    Info = ConfigParser()
    Info.read("Data/info.ini")

    checkSinglePlaylist()

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
    while True:
        url = input("Playlist / Video from playlist URL: ")
        if url.lower() == "exit":
            exit()
        if requests.get(f"{Info['yt']['checkLink']}{url}").status_code == 200:
            if ("/watch?v=" in url and "&list=" in url) or "playlist?list=" in url:
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            break
        else:
            print("Invalid playlist URL. Try again. (CTRL+C to exit or type exit)")
    print("Playlist downloaded, check SinglePlaylist/.")