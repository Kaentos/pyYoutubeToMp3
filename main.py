from __future__ import unicode_literals
import youtube_dl

if __name__ == "__main__":
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "Mp3/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    }

    with open("musicURLs.txt", "r") as file:
        URLs = file.readlines()
        URLs = [url.strip("\n") for url in URLs]
        #URLs = file.read()
        #URLs = URLs.split(";")
        print(URLs)

    #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #    ydl.download([''])