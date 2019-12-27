from __future__ import unicode_literals
import youtube_dl
import requests

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

    #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #    ydl.download([''])

    #with open("musicURLs.txt", "w") as file:
    #    file.write("> Give a new line for each link (link example: https://www.youtube.com/watch?v=Dqq2wXW3X2Q) <")