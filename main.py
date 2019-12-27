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

    with open("musicURLs.txt", "r") as file:
        URLs = file.readlines()
        URLs = [url.strip("\n") for url in URLs]
    print(URLs)
    
    # Validate URLs
    URLs = [ url for url in URLs if "https://www.youtube.com/watch?v=" in url ]
    testURL = "https://www.youtube.com/oembed?format=json&url="
    URLs = [url for url in URLs if requests.get(f"{testURL}{url}").status_code == 200]
    print(URLs)

    #https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v= get json from youtube (use to validate)

    #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #    ydl.download([''])

    #with open("musicURLs.txt", "w") as file:
    #    file.write("> Give a new line for each link (link example: https://www.youtube.com/watch?v=Dqq2wXW3X2Q) <")