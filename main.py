from youtube_dl import YoutubeDL
import requests
from configparser import ConfigParser
from os import path

def checkFile():
    if not path.exists("musicURLs.txt"):
        print("musicURLs.txt not found, creating a new one...")
        resetFile()
        print("musicURLs.txt created, you can now input your music URLs there.")
        exit()

def resetFile():
    with open("musicURLs.txt", "w") as file:
        file.write(Info["txt"]["example"])

if __name__ == "__main__":
    Info = ConfigParser()
    Info.read("info.ini")

    checkFile()

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
    if validURLs:
        print(f"URLs to download: {validURLs}")
        with YoutubeDL(ydl_opts) as ydl:
            for url in validURLs:
                ydl.download([url])
        print("Download completed, check Mp3/.")
    else:
        print("There are no videos to convert, did you input some in musicURLs.txt? Did you input them correctly?")
        exit()

    resetFile()