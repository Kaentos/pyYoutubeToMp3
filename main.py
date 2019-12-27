#import youtube_dl
from youtube_dl import YoutubeDL
import requests
from configparser import ConfigParser

if __name__ == "__main__":
    Info = ConfigParser()
    Info.read("info.ini")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "Mp3/%(title)s.%(ext)s",
        "noplaylist": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    }

    basicURL = "https://www.youtube.com/watch?v="
    testURL = "https://www.youtube.com/oembed?format=json&url="
    validURLs = []
    with open("musicURLs.txt", "r") as file:
        URLs = file.readlines()
        for url in URLs:
            url = url.strip("\n")
            if basicURL in url:
                if requests.get(f"{testURL}{url}").status_code == 200:
                    validURLs.append(url)
    print(validURLs)

    #https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v= get json from youtube (use to validate)

    with YoutubeDL(ydl_opts) as ydl:
        for url in validURLs:
            ydl.download([url])

    with open("musicURLs.txt", "w") as file:
        file.write(Info["txt"]["example"])